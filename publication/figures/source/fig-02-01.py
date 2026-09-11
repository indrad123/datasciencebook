"""Figure 2.1: four equivalent forms of one part-to-whole relationship."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch02_sample.csv").open(encoding="utf-8", newline="") as handle:
        row = next(csv.DictReader(handle))
    part, whole = int(row["first_value"]), int(row["second_value"])
    decimal = part / whole

    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    boxes = [
        (0.3, "Fraction", f"{part}/{whole}", LIGHT_GOLD, GOLD),
        (2.8, "Simplified", "3/4", "white", NAVY),
        (5.3, "Decimal", f"{decimal:.2f}", LIGHT_BLUE, BLUE),
        (7.8, "Percentage", f"{decimal * 100:.0f}%", "white", NAVY),
    ]
    for x, heading, value, fill, edge in boxes:
        ax.add_patch(FancyBboxPatch((x, 2.0), 1.9, 1.25, boxstyle="round,pad=0.08", facecolor=fill, edgecolor=edge, linewidth=1.3))
        ax.text(x + 0.95, 2.82, heading, ha="center", va="center", weight="bold", color=NAVY)
        ax.text(x + 0.95, 2.37, value, ha="center", va="center", color=NAVY, fontsize=11)
    for x in (2.2, 4.7, 7.2):
        ax.add_patch(FancyArrowPatch((x, 2.62), (x + 0.6, 2.62), arrowstyle="-|>", mutation_scale=12, color=NAVY, linewidth=1.1))
    ax.text(5, 1.15, "150 selected cartons out of 200 total cartons", ha="center", color=NAVY, weight="bold")
    ax.text(5, 0.68, "The notation changes; the represented share stays the same.", ha="center", color=NAVY)
    ax.set_title("One relationship can be written in four equivalent forms", color=NAVY, weight="bold", pad=8)
    fig.tight_layout()
    save_figure(fig, "fig-02-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
