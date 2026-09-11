"""Figure 6.1: repeated addition compressed into sigma notation."""

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
    with (ROOT / "data/generated/ch06_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["example_id"] == "warehouse_shipments"]

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    x_positions = (1.25, 3.75, 6.25, 8.75)
    for x, r in zip(x_positions, rows):
        patch = FancyBboxPatch((x - 0.9, 4.0), 1.8, 1.0, boxstyle="round,pad=0.04", facecolor=LIGHT_BLUE, edgecolor=NAVY)
        ax.add_patch(patch)
        ax.text(x, 4.63, f"q{r['outer_index']}", ha="center", color=NAVY, weight="bold")
        ax.text(x, 4.28, f"{int(r['term_value']):,} cases", ha="center", color=NAVY)
    ax.text(5, 3.38, "120 + 150 + 90 + 140 = 500 cases", ha="center", color=NAVY, fontsize=10)
    ax.add_patch(FancyArrowPatch((5, 3.05), (5, 2.15), arrowstyle="-|>", mutation_scale=14, color=GOLD, linewidth=1.7))
    patch = FancyBboxPatch((2.65, 0.72), 4.7, 1.15, boxstyle="round,pad=0.06", facecolor=LIGHT_GOLD, edgecolor=NAVY)
    ax.add_patch(patch)
    ax.text(5, 1.29, r"$\sum_{i=1}^{4} q_i = 500$ cases", ha="center", va="center", color=NAVY, fontsize=13, weight="bold")
    ax.text(5, 0.35, "The compact notation gives the same addition rule.", ha="center", color=BLUE)
    ax.set_title("Repeated addition becomes one precise instruction", color=NAVY, weight="bold", pad=8)
    fig.tight_layout()
    save_figure(fig, "fig-06-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
