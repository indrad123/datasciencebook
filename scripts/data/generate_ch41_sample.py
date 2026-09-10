"""Generate deterministic batch-monitoring data for Chapter 41."""

import csv
from pathlib import Path

import numpy as np
from sklearn.ensemble import IsolationForest

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch41_sample.csv"
FEATURES = ("fill_weight_g", "ph", "viscosity_cp")


def measurements(rng, n, offset=0):
    index = np.arange(offset, offset + n)
    family_b = index % 2 == 1
    line_2 = index % 3 == 2
    fill = 500 + 4.8 * rng.normal(size=n) + 1.2 * line_2
    ph = 4.02 + 0.43 * family_b + 0.035 * rng.normal(size=n)
    viscosity = 2180 + 115 * family_b + 42 * line_2 + 55 * rng.normal(size=n)
    return np.column_stack((fill, ph, viscosity)), family_b, line_2


def build_rows():
    rng = np.random.default_rng(4101)
    reference, ref_family_b, ref_line_2 = measurements(rng, 300)
    monitoring, mon_family_b, mon_line_2 = measurements(rng, 100, offset=300)

    anomaly_type = np.full(100, "ordinary", dtype=object)
    monitoring[8] += np.array([42.0, 0.0, 0.0])
    anomaly_type[8] = "point"
    monitoring[24, 1] = 4.43  # globally plausible, unusual for family A
    anomaly_type[24] = "contextual"
    for i, lift in zip((51, 52, 53), (185.0, 205.0, 225.0)):
        monitoring[i, 2] += lift
        anomaly_type[i] = "collective"

    # Quantise released measurements before fitting so published scores can be
    # reconstructed exactly from the CSV values.
    for values in (reference, monitoring):
        values[:, 0] = np.round(values[:, 0], 3)
        values[:, 1] = np.round(values[:, 1], 4)
        values[:, 2] = np.round(values[:, 2], 2)

    centre = np.median(reference, axis=0)
    scale = 1.4826 * np.median(np.abs(reference - centre), axis=0)
    all_values = np.vstack((reference, monitoring))
    robust_score = np.max(np.abs((all_values - centre) / scale), axis=1)
    detector = IsolationForest(n_estimators=250, contamination=0.05, random_state=41).fit(reference)
    isolation_score = -detector.score_samples(all_values)
    monitored_scores = isolation_score[300:]
    order = np.argsort(-monitored_scores, kind="stable")
    ranks = np.empty(100, dtype=int)
    ranks[order] = np.arange(1, 101)

    rows = []
    for i in range(400):
        is_reference = i < 300
        j = i if is_reference else i - 300
        family_b = ref_family_b[j] if is_reference else mon_family_b[j]
        line_2 = ref_line_2[j] if is_reference else mon_line_2[j]
        kind = "ordinary" if is_reference else anomaly_type[j]
        values = all_values[i]
        rows.append(
            {
                "batch_id": f"B41-{i + 1:03d}",
                "sample_role": "reference" if is_reference else "monitoring",
                "product_family": "sauce_b" if family_b else "sauce_a",
                "production_line": "line_2" if line_2 else "line_1",
                "sequence_index": str(i + 1),
                "fill_weight_g": f"{values[0]:.3f}",
                "ph": f"{values[1]:.4f}",
                "viscosity_cp": f"{values[2]:.2f}",
                "confirmed_relevant": "1" if kind != "ordinary" else "0",
                "anomaly_type": kind,
                "robust_max_abs_z": f"{robust_score[i]:.6f}",
                "isolation_score": f"{isolation_score[i]:.6f}",
                "monitoring_review_rank": "" if is_reference else str(ranks[j]),
                "selected_at_capacity_5": "1" if not is_reference and ranks[j] <= 5 else "0",
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
