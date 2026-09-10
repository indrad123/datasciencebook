"""Generate deterministic route examples for Chapter 23."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data/generated/ch23_sample.csv"

def build_rows():
    rows = []
    residuals = (-7, 3, -2, 6, -4, 1, 5, -5, 2, -1) * 3
    for scenario in ("linear", "curvature", "unequal_spread"):
        values = []
        for i in range(30):
            x = 5 + i
            if scenario == "linear":
                y = 28 + 1.6 * x + residuals[i]
            elif scenario == "curvature":
                y = 35 + 0.055 * (x - 8) ** 2 + residuals[i] * 0.35
            else:
                y = 28 + 1.6 * x + residuals[i] * (0.25 + i / 16)
            values.append((x, round(y, 3)))
        xb = sum(x for x, _ in values) / len(values); yb = sum(y for _, y in values) / len(values)
        slope = sum((x-xb)*(y-yb) for x,y in values) / sum((x-xb)**2 for x,_ in values)
        intercept = yb - slope * xb
        for i, (x, y) in enumerate(values, 1):
            fitted = intercept + slope * x
            rows.append({"scenario": scenario, "route_id": f"{scenario[:3].upper()}-{i:02d}",
                "distance_km": x, "delivery_time_minutes": round(y, 3),
                "fitted_time_minutes": round(fitted, 6), "residual_minutes": round(y-fitted, 6),
                "is_influential_demo": "No"})
    rows.append({"scenario":"influence","route_id":"INF-01","distance_km":70,
        "delivery_time_minutes":75,"fitted_time_minutes":"","residual_minutes":"","is_influential_demo":"Yes"})
    return rows

def main():
    rows=build_rows(); OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}")
if __name__ == "__main__": main()
