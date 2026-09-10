"""Generate deterministic derivative teaching data for Chapter 9."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch09_sample.csv"


def square(x: float) -> float:
    return x**2


def build_rows() -> list[dict[str, float]]:
    x0 = 3.0
    tangent_slope = 2 * x0
    secant_slopes = {h: (square(x0 + h) - square(x0)) / h for h in (1.0, 0.5, 0.1)}
    rows = []
    for step in range(21):
        x = step * 0.25
        h = 0.1
        rows.append(
            {
                "x": x,
                "square_value": square(x),
                "exact_derivative": 2 * x,
                "forward_difference_h_0_1": (square(x + h) - square(x)) / h,
                "central_difference_h_0_1": (square(x + h) - square(x - h)) / (2 * h),
                "tangent_at_x3": square(x0) + tangent_slope * (x - x0),
                "secant_h_1_0_at_x3": square(x0) + secant_slopes[1.0] * (x - x0),
                "secant_h_0_5_at_x3": square(x0) + secant_slopes[0.5] * (x - x0),
                "secant_h_0_1_at_x3": square(x0) + secant_slopes[0.1] * (x - x0),
            }
        )
    return rows


def main() -> None:
    rows = build_rows()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
