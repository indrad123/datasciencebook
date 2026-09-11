"""Figure 5.2: powers, roots, and logarithms as inverse operations."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def box(ax, x: float, y: float, text: str, colour: str) -> None:
    patch = FancyBboxPatch((x - 0.85, y - 0.34), 1.7, 0.68, boxstyle="round,pad=0.04", facecolor=colour, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY, weight="bold")


def arrow(ax, start, end, text: str, colour: str, offset: float) -> None:
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12, color=colour, linewidth=1.5, connectionstyle=f"arc3,rad={offset}"))
    ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + (0.42 if offset < 0 else -0.42), text, ha="center", color=NAVY)


def main() -> None:
    apply_style()
    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    box(ax, 2.2, 4.35, "exponent 3", LIGHT_BLUE)
    box(ax, 7.8, 4.35, "value 1,000", LIGHT_GOLD)
    arrow(ax, (3.1, 4.55), (6.9, 4.55), "power, with base 10: 10³ = 1,000", BLUE, -0.18)
    arrow(ax, (6.9, 4.12), (3.1, 4.12), "logarithm: log₁₀(1,000) = 3", GOLD, -0.18)

    box(ax, 2.2, 1.55, "root 7", LIGHT_BLUE)
    box(ax, 7.8, 1.55, "value 49", LIGHT_GOLD)
    arrow(ax, (3.1, 1.75), (6.9, 1.75), "power: 7² = 49", BLUE, -0.18)
    arrow(ax, (6.9, 1.32), (3.1, 1.32), "root: √49 = 7", GOLD, -0.18)
    ax.set_title("Inverse operations recover a missing base or exponent", color=NAVY, weight="bold", pad=8)
    fig.tight_layout()
    save_figure(fig, "fig-05-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
