"""Figure 6.2: indices, inclusive bounds, terms, and cumulative sum."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch06_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["example_id"] == "warehouse_shipments"]
    cumulative = 0
    cells = []
    for r in rows:
        cumulative += int(r["term_value"])
        cells.append([r["outer_index"], r["term_label"], f"q{r['outer_index']} = {int(r['term_value']):,}", f"{cumulative:,}"])

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.axis("off")
    table = ax.table(cellText=cells, colLabels=["Index i", "Warehouse", "Term qᵢ (cases)", "Running sum"], cellLoc="center", colLoc="center", loc="center", colWidths=[0.13, 0.27, 0.28, 0.22])
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1, 1.45)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor(NAVY)
        cell.set_linewidth(0.7)
        if r == 0:
            cell.set_facecolor(LIGHT_BLUE)
            cell.set_text_props(weight="bold", color=NAVY)
        elif r == len(cells):
            cell.set_facecolor(LIGHT_GOLD)
    ax.text(0.5, 0.08, "Lower bound i = 1   |   Upper bound i = 4   |   Both bounds are included", transform=ax.transAxes, ha="center", color=BLUE, weight="bold")
    ax.text(0.5, 0.015, "Four index values produce four terms and a final sum of 500 cases.", transform=ax.transAxes, ha="center", color=GOLD)
    ax.set_title("Indices select the terms included by the bounds", color=NAVY, weight="bold", pad=10)
    fig.tight_layout()
    save_figure(fig, "fig-06-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
