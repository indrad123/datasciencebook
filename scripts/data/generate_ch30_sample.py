"""Generate a deterministic data-quality register for Chapter 30."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch30_sample.csv"


def build_rows():
    specs = [
        ("Q-01", "uniqueness", "shipment_id", "all shipments", 180, 10000, 0.000, "blocker", "fail", "Fix status-history join; retain latest pre-dispatch record"),
        ("Q-02", "completeness", "sensor_temp_c", "all shipments", 400, 10000, 0.050, "warning", "pass", "Monitor overall coverage and inspect subgroups"),
        ("Q-03", "completeness", "sensor_temp_c", "affected warehouse-period", 310, 1000, 0.050, "warning", "fail", "Open sensor incident and restrict temperature-based use"),
        ("Q-04", "consistency", "delivered_at", "all shipments", 12, 10000, 0.000, "error", "fail", "Convert timestamps using recorded source timezones"),
        ("Q-05", "validity", "weight_kg", "all shipments", 0, 10000, 0.000, "error", "pass", "Quarantine values outside 0 to 30000 kg"),
        ("Q-06", "validity", "route_code", "all shipments", 0, 10000, 0.000, "error", "pass", "Validate against the dated route master"),
        ("Q-07", "freshness", "extract_age_hours", "analytical snapshot", 0, 1, 0.000, "blocker", "pass", "Reject input when extract age is 26 hours or more"),
        ("Q-08", "reconciliation", "shipment_sensor_join", "all shipments", 0, 10000, 0.000, "error", "pass", "Report unmatched keys and join cardinality"),
    ]
    rows = []
    for qid, dimension, field, scope, violations, denominator, threshold, severity, status, response in specs:
        rows.append({
            "check_id": qid, "quality_dimension": dimension, "field_or_table": field,
            "scope": scope, "violation_count": violations, "denominator": denominator,
            "violation_rate": f"{violations/denominator:.3f}",
            "maximum_allowed_rate": f"{threshold:.3f}", "severity": severity,
            "status": status, "response": response,
        })
    return rows


def main():
    rows = build_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
