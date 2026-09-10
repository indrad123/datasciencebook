"""Generate deterministic calibration and explanation data for Chapter 47."""

import csv
from datetime import date, timedelta
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch47_sample.csv"
N = 1200
TRAIN_END = 700
CALIBRATION_END = 950


def _logistic(values):
    return 1 / (1 + np.exp(-values))


def _raw_score(model, features):
    model_probability = np.clip(model.predict_proba(features)[:, 1], 0.02, 0.98)
    log_odds = np.log(model_probability / (1 - model_probability))
    return _logistic(1.30 * log_odds - 0.15)


def build_rows():
    rng = np.random.default_rng(47)
    distance = np.round(np.clip(rng.normal(620, 210, N), 80, 1400), 1)
    congestion = np.round(np.clip(rng.beta(2.2, 2.7, N), 0.02, 0.98), 3)
    fragile = rng.binomial(1, 0.27, N)
    features = np.column_stack([distance, congestion, fragile])

    log_odds = -4.30 + 0.003 * distance + 3.0 * congestion + 0.90 * fragile
    true_probability = _logistic(log_odds)
    late = rng.binomial(1, true_probability)

    model = RandomForestClassifier(
        n_estimators=240,
        min_samples_leaf=8,
        max_features=None,
        random_state=47,
        n_jobs=1,
    ).fit(features[:TRAIN_END], late[:TRAIN_END])
    raw = _raw_score(model, features)
    calibrator = LogisticRegression(C=1e6, solver="lbfgs", random_state=47).fit(
        raw[TRAIN_END:CALIBRATION_END, None],
        late[TRAIN_END:CALIBRATION_END],
    )
    calibrated = calibrator.predict_proba(raw[:, None])[:, 1]
    baseline = late[:TRAIN_END].mean()

    rows = []
    start = date(2023, 1, 1)
    for i in range(N):
        split = "train" if i < TRAIN_END else "calibration" if i < CALIBRATION_END else "test"
        rows.append(
            {
                "shipment_id": f"S47-{i + 1:04d}",
                "prediction_date": (start + timedelta(days=i)).isoformat(),
                "split": split,
                "route_distance_km": f"{distance[i]:.1f}",
                "port_congestion_index": f"{congestion[i]:.3f}",
                "fragile_product": str(fragile[i]),
                "actual_late": str(late[i]),
                "true_late_probability": f"{true_probability[i]:.6f}",
                "train_prevalence_baseline": f"{baseline:.6f}",
                "raw_probability": f"{raw[i]:.6f}",
                "calibrated_probability": f"{calibrated[i]:.6f}",
                "raw_predicted_late": str(int(raw[i] >= 0.5)),
                "calibrated_predicted_late": str(int(calibrated[i] >= 0.5)),
                "raw_brier_contribution": f"{(raw[i] - late[i]) ** 2:.6f}",
                "calibrated_brier_contribution": f"{(calibrated[i] - late[i]) ** 2:.6f}",
            }
        )
    return rows


def main():
    rows = build_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
