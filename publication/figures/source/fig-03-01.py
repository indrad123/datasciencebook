"""Figure 3.1: solving an equation while preserving equality."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def equation_box(ax, y, left, right, operation, fill, edge):
    ax.add_patch(FancyBboxPatch((0.7, y), 3.25, 0.95, boxstyle="round,pad=0.08", facecolor=fill, edgecolor=edge, linewidth=1.2))
    ax.add_patch(FancyBboxPatch((6.05, y), 3.25, 0.95, boxstyle="round,pad=0.08", facecolor=fill, edgecolor=edge, linewidth=1.2))
    ax.text(2.325, y + 0.48, left, ha="center", va="center", color=NAVY, fontsize=11, weight="bold")
    ax.text(7.675, y + 0.48, right, ha="center", va="center", color=NAVY, fontsize=11, weight="bold")
    ax.text(5, y + 0.48, "=", ha="center", va="center", color=NAVY, fontsize=13, weight="bold")
    if operation:
        ax.text(5, y - 0.28, operation, ha="center", va="center", color=NAVY, fontsize=8)


def main() -> None:
    apply_style()
    fig, ax = plt.subplots(figsize=(5.2, 3.35))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    equation_box(ax, 4.35, "18x + 120", "1,200", "subtract 120 from both sides", LIGHT_GOLD, GOLD)
    equation_box(ax, 2.55, "18x", "1,080", "divide both sides by 18", LIGHT_BLUE, BLUE)
    equation_box(ax, 0.75, "x", "60 cartons", "check: 18(60) + 120 = 1,200", "white", NAVY)
    for y in (4.2, 2.4):
        ax.add_patch(FancyArrowPatch((5, y), (5, y - 0.65), arrowstyle="-|>", mutation_scale=12, color=NAVY, linewidth=1.1))
    ax.set_title("Apply the same operation to both sides", color=NAVY, weight="bold", pad=8)
    fig.tight_layout()
    save_figure(fig, "fig-03-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
