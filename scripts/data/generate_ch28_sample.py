"""Generate deterministic shipment-risk and decision examples for Chapter 28."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch28_sample.csv"


def build_rows():
    probabilities = (0.03, 0.05, 0.08, 0.10, 0.12, 0.14, 0.15, 0.16, 0.18, 0.20,
                     0.24, 0.28, 0.34, 0.40, 0.48, 0.56, 0.65, 0.74, 0.84, 0.92)
    actual_late = (0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1)
    rows = []
    for i, (p, late) in enumerate(zip(probabilities, actual_late), 1):
        expedite_loss = 12.0
        standard_loss = round(80 * p, 2)
        rows.append({
            "shipment_id": f"S-{i:03d}",
            "weather_alert": "yes" if i % 3 == 0 or p >= 0.48 else "no",
            "loading_minutes": 38 + ((i * 7) % 39),
            "predicted_late_probability": f"{p:.2f}",
            "actual_late": late,
            "expedite_cost_units": f"{expedite_loss:.2f}",
            "late_loss_units": "80.00",
            "expected_loss_expedite": f"{expedite_loss:.2f}",
            "expected_loss_standard": f"{standard_loss:.2f}",
            "recommended_action": "expedite" if standard_loss > expedite_loss else "standard",
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
