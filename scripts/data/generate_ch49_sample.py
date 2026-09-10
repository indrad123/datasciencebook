"""Generate deterministic deep-learning value and readiness scenarios for Chapter 49."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch49_sample.csv"
ANNUAL_PACKAGES = 500_000
BASELINE_ERROR = 0.08
VALUE_PER_CORRECTION = 18_000
MINIMUM_GATE = 0.60

PROPOSALS = [
    ("P49-01", "Custom CNN cloud", "images", 0.060, 12, 2_500_000, 35, 190_000_000, 0.82, 0.90, 0.64, 0.76),
    ("P49-02", "Transfer CNN cloud", "images", 0.055, 6, 1_200_000, 22, 110_000_000, 0.84, 0.90, 0.78, 0.81),
    ("P49-03", "Compressed edge CNN", "images", 0.058, 8, 1_500_000, 12, 135_000_000, 0.80, 0.90, 0.86, 0.74),
    ("P49-04", "Large vision transformer", "images", 0.052, 15, 5_000_000, 80, 235_000_000, 0.86, 0.90, 0.70, 0.75),
    ("P49-05", "Low-data custom CNN", "images", 0.065, 10, 1_800_000, 35, 120_000_000, 0.48, 0.90, 0.72, 0.73),
    ("P49-06", "Third-party vision API", "images", 0.054, 0, 0, 110, 95_000_000, 0.78, 0.90, 0.83, 0.35),
    ("P49-07", "Quantized edge transfer", "images", 0.057, 6, 1_000_000, 8, 105_000_000, 0.84, 0.90, 0.88, 0.82),
    ("P49-08", "Maximum-accuracy ensemble", "images", 0.048, 20, 6_000_000, 120, 270_000_000, 0.88, 0.90, 0.68, 0.72),
]


def build_rows():
    rows = []
    for proposal in PROPOSALS:
        (proposal_id, approach, modality, candidate_error, training_runs, training_cost,
         inference_cost, engineering_cost, data, baseline, operations, governance) = proposal
        reduction = BASELINE_ERROR - candidate_error
        gross_value = ANNUAL_PACKAGES * reduction * VALUE_PER_CORRECTION
        lifecycle_cost = training_runs * training_cost + ANNUAL_PACKAGES * inference_cost + engineering_cost
        net_value = gross_value - lifecycle_cost
        readiness = min(data, baseline, operations, governance)
        recommendation = "pilot" if net_value > 0 and readiness >= MINIMUM_GATE else "simpler-baseline"
        rows.append(
            {
                "proposal_id": proposal_id,
                "model_approach": approach,
                "input_modality": modality,
                "annual_packages": str(ANNUAL_PACKAGES),
                "baseline_error_rate": f"{BASELINE_ERROR:.3f}",
                "candidate_error_rate": f"{candidate_error:.3f}",
                "absolute_error_reduction": f"{reduction:.3f}",
                "corrected_decisions": str(round(ANNUAL_PACKAGES * reduction)),
                "value_per_corrected_decision_idr": str(VALUE_PER_CORRECTION),
                "gross_incremental_value_idr": f"{gross_value:.0f}",
                "training_runs": str(training_runs),
                "training_cost_per_run_idr": str(training_cost),
                "annual_inferences": str(ANNUAL_PACKAGES),
                "inference_cost_per_case_idr": str(inference_cost),
                "engineering_monitoring_cost_idr": str(engineering_cost),
                "annual_lifecycle_cost_idr": f"{lifecycle_cost:.0f}",
                "annual_net_value_idr": f"{net_value:.0f}",
                "data_readiness": f"{data:.2f}",
                "baseline_readiness": f"{baseline:.2f}",
                "operations_readiness": f"{operations:.2f}",
                "governance_readiness": f"{governance:.2f}",
                "minimum_readiness": f"{readiness:.2f}",
                "recommendation": recommendation,
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
