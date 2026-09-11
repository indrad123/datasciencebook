"""Figure 1.1: quantity, unit, and measurement chain."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    boxes = [
        (0.3, 2.0, 2.1, 1.25, "Real property", "Mass of one pack", LIGHT_GOLD, GOLD),
        (3.0, 2.0, 2.1, 1.25, "Measurement", "Scale reading", LIGHT_BLUE, BLUE),
        (5.7, 2.0, 1.65, 1.25, "Number", "84.9", "white", NAVY),
        (8.0, 2.0, 1.65, 1.25, "Unit", "grams (g)", "white", NAVY),
    ]
    for x, y, width, height, heading, detail, fill, edge in boxes:
        patch = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.08", facecolor=fill, edgecolor=edge, linewidth=1.3)
        ax.add_patch(patch)
        ax.text(x + width / 2, y + 0.82, heading, ha="center", va="center", weight="bold", color=NAVY)
        ax.text(x + width / 2, y + 0.38, detail, ha="center", va="center", color=NAVY)

    for start, end in [((2.4, 2.62), (3.0, 2.62)), ((5.1, 2.62), (5.7, 2.62)), ((7.35, 2.62), (8.0, 2.62))]:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12, color=NAVY, linewidth=1.1))

    ax.text(6.52, 1.28, "Quantity value = numerical value × unit", ha="center", color=NAVY, weight="bold")
    ax.text(6.52, 0.78, "84.9 g describes the measurement; 84.9 alone does not.", ha="center", color=NAVY)
    ax.set_title("A useful number keeps its meaning and unit", color=NAVY, weight="bold", pad=8)
    fig.tight_layout()
    save_figure(fig, "fig-01-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()

