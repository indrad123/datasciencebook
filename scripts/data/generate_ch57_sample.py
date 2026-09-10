"""Generate the deterministic cross-modality comparison for Chapter 57."""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.modality import relative_improvement, value_per_compute  # noqa: E402

OUT = ROOT / "data/generated/ch57_sample.csv"


SCENARIOS = [
    {
        "modality": "Table",
        "decision": "late-delivery prediction",
        "data_unit": "one shipment row",
        "baseline_model": "gradient-boosted trees",
        "deep_model": "tabular neural network",
        "split_unit": "shipment date and distributor group",
        "baseline_quality": 0.84,
        "deep_quality": 0.83,
        "baseline_training_hours": 0.5,
        "deep_training_hours": 2.0,
        "baseline_inference_ms": 2.0,
        "deep_inference_ms": 3.0,
        "architecture_or_representation": "named numeric and categorical columns",
        "leakage_control": "exclude identifiers and split groups before preprocessing",
        "monitoring_focus": "schema categories and missingness",
        "missing_input_fallback": "validated tree baseline",
    },
    {
        "modality": "Text",
        "decision": "route distributor messages",
        "data_unit": "one conversation thread",
        "baseline_model": "TF-IDF logistic regression",
        "deep_model": "pretrained transformer encoder",
        "split_unit": "conversation or distributor thread",
        "baseline_quality": 0.86,
        "deep_quality": 0.90,
        "baseline_training_hours": 0.6,
        "deep_training_hours": 14.0,
        "baseline_inference_ms": 4.0,
        "deep_inference_ms": 18.0,
        "architecture_or_representation": "ordered subword tokens and context",
        "leakage_control": "keep every message from one thread in one partition",
        "monitoring_focus": "language token fragmentation and truncation",
        "missing_input_fallback": "rules or TF-IDF classifier with review",
    },
    {
        "modality": "Image",
        "decision": "inspect package defects",
        "data_unit": "all frames from one package",
        "baseline_model": "engineered vision features",
        "deep_model": "transfer convolutional network",
        "split_unit": "package identity",
        "baseline_quality": 0.78,
        "deep_quality": 0.87,
        "baseline_training_hours": 1.5,
        "deep_training_hours": 28.0,
        "baseline_inference_ms": 8.0,
        "deep_inference_ms": 35.0,
        "architecture_or_representation": "local pixels shared kernels and transferred features",
        "leakage_control": "keep every frame from one package in one partition",
        "monitoring_focus": "camera factory lighting blur and occlusion",
        "missing_input_fallback": "manual inspection or metadata-only rule",
    },
    {
        "modality": "Time series",
        "decision": "filling-line early warning",
        "data_unit": "one historical sensor window",
        "baseline_model": "boosted trees on lag features",
        "deep_model": "temporal convolutional network",
        "split_unit": "forecast origin before window construction",
        "baseline_quality": 0.81,
        "deep_quality": 0.84,
        "baseline_training_hours": 1.0,
        "deep_training_hours": 18.0,
        "baseline_inference_ms": 5.0,
        "deep_inference_ms": 12.0,
        "architecture_or_representation": "ordered lag window with local temporal patterns",
        "leakage_control": "split by time before windows and exclude future repaired values",
        "monitoring_focus": "timestamp frequency lag freshness and regime",
        "missing_input_fallback": "lag-feature baseline or safe process limit",
    },
]


def build_rows():
    rows = []
    for scenario in SCENARIOS:
        gain = relative_improvement(scenario["baseline_quality"], scenario["deep_quality"])
        score = value_per_compute(max(gain, 0.0), scenario["deep_training_hours"], scenario["deep_inference_ms"])
        preferred = scenario["deep_model"] if gain > 0 else scenario["baseline_model"]
        recommendation = "retain_strong_baseline" if gain <= 0 else "deep_candidate_for_bounded_validation"
        rows.append(
            {
                "modality": scenario["modality"],
                "decision": scenario["decision"],
                "data_unit": scenario["data_unit"],
                "baseline_model": scenario["baseline_model"],
                "deep_model": scenario["deep_model"],
                "split_unit": scenario["split_unit"],
                "primary_metric": "illustrative held-out quality; higher is better",
                "baseline_quality": f'{scenario["baseline_quality"]:.2f}',
                "deep_quality": f'{scenario["deep_quality"]:.2f}',
                "absolute_gain_points": f'{100 * (scenario["deep_quality"] - scenario["baseline_quality"]):.1f}',
                "relative_improvement_pct": f"{100 * gain:.6f}",
                "baseline_training_hours": f'{scenario["baseline_training_hours"]:.1f}',
                "deep_training_hours": f'{scenario["deep_training_hours"]:.1f}',
                "baseline_inference_ms": f'{scenario["baseline_inference_ms"]:.1f}',
                "deep_inference_ms": f'{scenario["deep_inference_ms"]:.1f}',
                "deep_value_per_compute": f"{score:.12f}",
                "preferred_quality_model": preferred,
                "recommendation": recommendation,
                "architecture_or_representation": scenario["architecture_or_representation"],
                "leakage_control": scenario["leakage_control"],
                "monitoring_focus": scenario["monitoring_focus"],
                "missing_input_fallback": scenario["missing_input_fallback"],
                "comparison_seed": "not_applicable_fixed_values",
                "evidence_scope": "synthetic teaching comparison; not a production benchmark",
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
