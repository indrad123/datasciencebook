"""Generate the Chapter 3 reader dataset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch03_sample.csv"


def build_rows() -> list[dict[str, int | bool]]:
    rows = []
    for cartons_per_pallet in (0, 20, 40, 60, 80, 100):
        pallet_cartons = 18 * cartons_per_pallet
        shipment_total = pallet_cartons + 120
        rows.append(
            {
                "cartons_per_pallet": cartons_per_pallet,
                "pallet_count": 18,
                "sample_cartons": 120,
                "pallet_cartons": pallet_cartons,
                "shipment_total_cartons": shipment_total,
                "meets_1200_carton_plan": shipment_total == 1200,
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
