"""Generate the Chapter 1 reader dataset."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch01_sample.csv"


ROWS = [
    {"pack_id": "NRG-P001", "label_mass_g": 85.0, "measured_mass_g": 84.7, "scale_resolution_g": 0.1},
    {"pack_id": "NRG-P002", "label_mass_g": 85.0, "measured_mass_g": 85.1, "scale_resolution_g": 0.1},
    {"pack_id": "NRG-P003", "label_mass_g": 85.0, "measured_mass_g": 84.9, "scale_resolution_g": 0.1},
    {"pack_id": "NRG-P004", "label_mass_g": 85.0, "measured_mass_g": 85.0, "scale_resolution_g": 0.1},
    {"pack_id": "NRG-P005", "label_mass_g": 85.0, "measured_mass_g": 85.3, "scale_resolution_g": 0.1},
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

