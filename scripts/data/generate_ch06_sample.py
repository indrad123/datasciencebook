"""Generate the deterministic Chapter 6 summation examples."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch06_sample.csv"
FIELDS = ["example_id", "outer_index", "inner_index", "term_label", "term_value", "weight", "weighted_term", "included"]


def row(example_id: str, outer: int, inner: int | None, label: str, value: int, weight: int | None = None) -> dict[str, str | int]:
    return {
        "example_id": example_id,
        "outer_index": outer,
        "inner_index": "" if inner is None else inner,
        "term_label": label,
        "term_value": value,
        "weight": "" if weight is None else weight,
        "weighted_term": "" if weight is None else value * weight,
        "included": "yes",
    }


def build_rows() -> list[dict[str, str | int]]:
    rows = []
    for i, (warehouse, quantity) in enumerate(zip(("Jakarta", "Singapore", "Sydney", "Rotterdam"), (120, 150, 90, 140)), 1):
        rows.append(row("warehouse_shipments", i, None, warehouse, quantity))
    for i in range(1, 5):
        rows.append(row("odd_number_summand", i, None, f"2({i}) + 1", 2 * i + 1))
    for i, (product, price, quantity) in enumerate(zip(("Coffee", "Tea", "Spices"), (20, 30, 25), (10, 5, 8)), 1):
        rows.append(row("weighted_revenue", i, None, product, price, quantity))
    matrix = ((10, 12, 8), (7, 9, 11))
    for i, values in enumerate(matrix, 1):
        for j, value in enumerate(values, 1):
            rows.append(row("product_region_matrix", i, j, f"q_{i}{j}", value))
    return rows


def main() -> None:
    rows = build_rows()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
