"""Generate the deterministic Chapter 8 production-system dataset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch08_sample.csv"


def build_rows() -> list[dict[str, int | str]]:
    coffee_batches = 42
    tea_batches = 16
    constraints = (
        ("Ingredient A", 2, 1, 100),
        ("Ingredient B", 1, 3, 90),
    )
    rows = []
    for row_index, (resource, coffee_units, tea_units, available) in enumerate(constraints, 1):
        coffee_usage = coffee_units * coffee_batches
        tea_usage = tea_units * tea_batches
        rows.append(
            {
                "row_index": row_index,
                "resource_label": resource,
                "coffee_units_per_batch": coffee_units,
                "tea_units_per_batch": tea_units,
                "available_units": available,
                "coffee_batches_solution": coffee_batches,
                "tea_batches_solution": tea_batches,
                "coffee_resource_usage": coffee_usage,
                "tea_resource_usage": tea_usage,
                "total_resource_usage": coffee_usage + tea_usage,
                "residual_units": coffee_usage + tea_usage - available,
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
