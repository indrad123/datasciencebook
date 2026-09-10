"""Generate deterministic order data for Chapter 15 chart selection examples."""
from __future__ import annotations
import csv
from datetime import date, timedelta
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data/generated/ch15_sample.csv"
SEED = 1515


def build_rows():
    rng = np.random.default_rng(SEED)
    categories = np.array(["Noodles", "Coffee", "Tea", "Spices", "Ready-to-drink"])
    probabilities = np.array([0.31, 0.24, 0.19, 0.14, 0.12])
    regions = np.array(["Jakarta", "West Java", "Central Java", "East Java"])
    start = date(2026, 4, 1)
    day_weights = np.array([1 + 0.018 * d + (0.22 if d % 7 in (3, 4) else 0) for d in range(30)])
    day_weights = day_weights / day_weights.sum()
    rows = []
    for i in range(120):
        category = rng.choice(categories, p=probabilities)
        delivery_days = int(np.clip(np.rint(rng.gamma(3.1, 1.05)), 1, 9))
        promised_days = 4
        units = int(rng.integers(1, 7))
        rows.append({
            "order_id": f"ORD-{i + 1:03d}",
            "order_date": (start + timedelta(days=int(rng.choice(30, p=day_weights)))).isoformat(),
            "region": regions[i % len(regions)],
            "product_category": category,
            "units": units,
            "delivery_days": delivery_days,
            "promised_days": promised_days,
            "delivery_status": "On time" if delivery_days <= promised_days else "Late",
        })
    return rows


def main():
    rows = build_rows()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
