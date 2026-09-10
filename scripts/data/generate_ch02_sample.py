"""Generate the Chapter 2 reader dataset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch02_sample.csv"


ROWS = [
    {"example_id": "ORDER-001", "context": "cartons selected", "first_value": 150, "second_value": 200, "first_label": "selected cartons", "second_label": "all cartons", "unit": "cartons"},
    {"example_id": "LINE-A", "context": "quality acceptance", "first_value": 960, "second_value": 1000, "first_label": "acceptable packs", "second_label": "inspected packs", "unit": "packs"},
    {"example_id": "LINE-B", "context": "quality acceptance", "first_value": 1425, "second_value": 1500, "first_label": "acceptable packs", "second_label": "inspected packs", "unit": "packs"},
    {"example_id": "DEMAND-01", "context": "weekly demand change", "first_value": 920, "second_value": 800, "first_label": "new demand", "second_label": "original demand", "unit": "cases"},
    {"example_id": "DELIVERY-01", "context": "on-time delivery", "first_value": 1170, "second_value": 1250, "first_label": "on-time deliveries", "second_label": "all deliveries", "unit": "deliveries"},
]


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROWS[0].keys())
        writer.writeheader()
        writer.writerows(ROWS)
    print(f"Wrote {len(ROWS)} rows to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
