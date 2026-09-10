"""Generate the deterministic package-risk error inventory for Chapter 58."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.responsibility import (  # noqa: E402
    error_labels,
    readiness_report,
    review_queue,
    slice_error_rates,
)

OUT = ROOT / "data/generated/ch58_sample.csv"
THRESHOLD = 0.5
REVIEW_CAPACITY = 4


def stable_descending_rank(values):
    rank = np.empty(len(values), dtype=int)
    rank[np.argsort(-np.asarray(values), kind="stable")] = np.arange(1, len(values) + 1)
    return rank


def build_rows():
    actual = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0])
    probability = np.array([0.10, 0.80, 0.70, 0.20, 0.90, 0.40, 0.55, 0.60, 0.30, 0.15, 0.75, 0.45])
    factory = np.array(["A"] * 6 + ["B"] * 6)
    camera = np.array(["CAM-A1", "CAM-A1", "CAM-A2", "CAM-A2", "CAM-A1", "CAM-A2",
                       "CAM-B1", "CAM-B2", "CAM-B1", "CAM-B2", "CAM-B1", "CAM-B2"])
    revision = np.array(["R1", "R1", "R2", "R2", "R1", "R2", "R1", "R2", "R1", "R2", "R1", "R2"])
    quality = np.array(["clear", "clear", "shadow", "glare", "clear", "blur",
                        "clear", "shadow", "glare", "clear", "clear", "blur"])
    category = np.array(["none", "seal", "none", "exposed_product", "seal", "none",
                         "dent", "none", "seal", "none", "exposed_product", "none"])
    severity = np.array(["none", "high", "none", "critical", "high", "none",
                         "medium", "none", "high", "none", "critical", "none"])
    potential_cost = np.array([300, 1200, 300, 5000, 1200, 300, 700, 300, 1200, 300, 5000, 300], dtype=float)
    reviewer = np.array(["pass", "divert", "pass", "divert", "divert", "pass",
                         "divert", "pass", "divert", "pass", "divert", "pass"])
    mechanism = np.array(["none", "none", "shadow_false_alarm", "glare_false_pass", "none", "none",
                          "none", "shadow_false_alarm", "revision_shift_false_pass", "none", "none", "none"])

    labels = error_labels(actual, probability, THRESHOLD)
    predicted = (probability >= THRESHOLD).astype(int)
    uncertainty_indices = review_queue(probability, REVIEW_CAPACITY)
    uncertainty_rank = stable_descending_rank(-np.abs(probability - THRESHOLD))
    expected_harm = probability * potential_cost
    harm_rank = stable_descending_rank(expected_harm)
    checks = {
        "owner": "Jakarta Quality Director",
        "intended_use": "inspection prioritization only",
        "test_slices": slice_error_rates(actual, probability, factory),
        "fallback": "manual inspection queue",
        "monitoring": "weekly service and delayed outcome review",
        "rollback": "",
    }
    readiness = readiness_report(checks)

    rows = []
    for i in range(len(actual)):
        rows.append(
            {
                "package_id": f"PKG58-{i + 1:02d}",
                "prediction_time": f"2026-07-{i + 1:02d}T08:00:00+07:00",
                "model_version": "pkg-risk-0.9.0",
                "factory": factory[i],
                "camera_id": camera[i],
                "packaging_revision": revision[i],
                "input_quality": quality[i],
                "defect_category": category[i],
                "actual_defect": str(int(actual[i])),
                "risk_probability": f"{probability[i]:.2f}",
                "decision_threshold": f"{THRESHOLD:.2f}",
                "predicted_defect": str(int(predicted[i])),
                "outcome_label": labels[i],
                "is_error": str(labels[i] in ("FP", "FN")).lower(),
                "false_negative": str(labels[i] == "FN").lower(),
                "error_mechanism": mechanism[i],
                "severity": severity[i],
                "potential_consequence_kidr": f"{potential_cost[i]:.0f}",
                "expected_harm_kidr": f"{expected_harm[i]:.2f}",
                "uncertainty_distance": f"{abs(probability[i] - THRESHOLD):.2f}",
                "uncertainty_review_rank": str(int(uncertainty_rank[i])),
                "uncertainty_review_flag": str(i in uncertainty_indices).lower(),
                "harm_review_rank": str(int(harm_rank[i])),
                "harm_review_flag": str(harm_rank[i] <= REVIEW_CAPACITY).lower(),
                "reviewer_outcome": reviewer[i],
                "accountable_owner": checks["owner"],
                "fallback_route": checks["fallback"],
                "rollback_defined": "false",
                "release_ready": str(readiness["ready"]).lower(),
                "blocking_control": readiness["missing"][0],
                "data_seed": "not_applicable_fixed_values",
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
