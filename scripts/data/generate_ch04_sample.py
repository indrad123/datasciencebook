"""Generate the Chapter 4 reader dataset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch04_sample.csv"


def build_rows() -> list[dict[str, int | str]]:
    rows = []
    for quantity in (0, 25, 50, 60, 75, 100, 150):
        plan_a = 300_000 + 4_000 * quantity
        plan_b = 180_000 + 6_000 * quantity
        if plan_a == plan_b:
            cheaper = "equal"
        else:
            cheaper = "Plan A" if plan_a < plan_b else "Plan B"
        rows.append(
            {
                "quantity_cases": quantity,
                "plan_a_fixed_idr": 300_000,
                "plan_a_rate_idr_per_case": 4_000,
                "plan_a_cost_idr": plan_a,
                "plan_b_fixed_idr": 180_000,
                "plan_b_rate_idr_per_case": 6_000,
                "plan_b_cost_idr": plan_b,
                "cheaper_plan": cheaper,
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
