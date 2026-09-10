"""Generate the deterministic Chapter 5 reader dataset."""

from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch05_sample.csv"


def build_rows() -> list[dict[str, int | float]]:
    rows = []
    for year in range(11):
        exponential = 10_000 * 1.08**year
        rows.append(
            {
                "year": year,
                "initial_demand_cases": 10_000,
                "annual_growth_rate": 0.08,
                "linear_demand_cases": 10_000 + 800 * year,
                "exponential_demand_cases": round(exponential, 2),
                "growth_factor_power": round(1.08**year, 6),
                "log_recovered_year": round(math.log(exponential / 10_000, 1.08), 6),
                "retained_inventory_pct": round(100 * 0.88**year, 2),
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
