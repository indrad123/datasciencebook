"""Generate deterministic component data for Chapter 7."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch07_sample.csv"


def build_rows() -> list[dict[str, int | str]]:
    rows = []
    products = ("Coffee", "Tea", "Noodles")
    warehouse_a = (4, 3, 5)
    warehouse_b = (2, 4, 6)
    for position, (product, a, b) in enumerate(zip(products, warehouse_a, warehouse_b), 1):
        difference = a - b
        rows.append(
            {
                "example_id": "warehouse_profiles",
                "component_position": position,
                "component_label": product,
                "vector_a_value": a,
                "vector_b_value": b,
                "difference_a_minus_b": difference,
                "absolute_difference": abs(difference),
                "squared_difference": difference**2,
                "component_product": a * b,
            }
        )
    for position, value in enumerate((3, 4), 1):
        rows.append(
            {
                "example_id": "magnitude_unit_vector",
                "component_position": position,
                "component_label": ("horizontal", "vertical")[position - 1],
                "vector_a_value": value,
                "vector_b_value": 0,
                "difference_a_minus_b": value,
                "absolute_difference": value,
                "squared_difference": value**2,
                "component_product": 0,
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
