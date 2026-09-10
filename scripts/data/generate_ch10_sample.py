"""Generate deterministic accumulation teaching data for Chapter 10."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch10_sample.csv"


def rate(t: float) -> float:
    """NRG net inventory flow in cases per hour."""
    return 12.0 - 3.0 * t


def antiderivative(t: float) -> float:
    return 12.0 * t - 1.5 * t**2


def absolute_accumulation(t: float) -> float:
    """Integral of abs(rate) from zero to t; rate changes sign at hour four."""
    if t <= 4.0:
        return antiderivative(t)
    return 24.0 + (antiderivative(4.0) - antiderivative(t))


def build_rows() -> list[dict[str, float]]:
    width = 0.5
    rows = []
    cumulative_left = cumulative_right = cumulative_trapezoid = 0.0
    for step in range(12):
        start = step * width
        end = start + width
        left = rate(start) * width
        right = rate(end) * width
        trapezoid = 0.5 * (rate(start) + rate(end)) * width
        cumulative_left += left
        cumulative_right += right
        cumulative_trapezoid += trapezoid
        rows.append(
            {
                "interval_start_hour": start,
                "interval_end_hour": end,
                "interval_width_hour": width,
                "start_rate_cases_per_hour": rate(start),
                "end_rate_cases_per_hour": rate(end),
                "left_contribution_cases": left,
                "right_contribution_cases": right,
                "trapezoid_contribution_cases": trapezoid,
                "cumulative_left_cases": cumulative_left,
                "cumulative_right_cases": cumulative_right,
                "cumulative_trapezoid_cases": cumulative_trapezoid,
                "exact_net_change_cases": antiderivative(end),
                "exact_absolute_movement_cases": absolute_accumulation(end),
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
