"""Figure 48.1: production ML service and control architecture."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, y, text, face=LIGHT_BLUE, width=1.35, height=0.55):
    patch = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                           boxstyle="round,pad=0.04,rounding_size=0.06",
                           facecolor=face, edgecolor=NAVY, linewidth=1.0)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY, fontsize=7.4, weight="bold")


def arrow(ax, start, end, color=TEAL, style="-|>"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=11,
                                color=color, linewidth=1.35, shrinkA=3, shrinkB=3))


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    y = 2.65
    nodes = [(0.75, "Orders +\noperations"), (2.35, "Shared feature\nservice"),
             (3.95, "Versioned model\nservice"), (5.55, "Intervention\nqueue"), (7.15, "Actions + later\noutcomes")]
    for x, label in nodes:
        box(ax, x, y, label, LIGHT_BLUE if x != 3.95 else LIGHT_GOLD)
    for left, right in zip(nodes, nodes[1:]):
        arrow(ax, (left[0] + 0.69, y), (right[0] - 0.69, y))

    box(ax, 1.45, 1.38, "Immutable logs\nIDs · versions\nscores · actions", "#E8ECEF", width=2.20)
    box(ax, 3.95, 1.38, "Layered monitoring\nsystem · data · model\nbusiness", "#E8ECEF", width=2.20)
    box(ax, 6.45, 1.38, "Owned response\ninvestigate · degrade\nroll back", "#F7DEDC", width=2.20)
    arrow(ax, (3.95, 2.36), (2.15, 1.68), BLUE)
    arrow(ax, (5.55, 2.36), (3.95, 1.68), BLUE)
    arrow(ax, (7.15, 2.36), (6.45, 1.68), BLUE)
    arrow(ax, (2.55, 1.38), (2.85, 1.38))
    arrow(ax, (5.05, 1.38), (5.35, 1.38))

    box(ax, 3.95, 0.35, "Model registry: candidate → validated → approved → deployed → superseded\nPrevious compatible version retained as rollback target",
        LIGHT_GOLD, width=6.20, height=0.60)
    arrow(ax, (3.95, 0.63), (3.95, 1.07), GOLD)

    ax.set(xlim=(0, 7.9), ylim=(-0.05, 3.25))
    ax.axis("off")
    fig.suptitle("A deployed model is a versioned decision service with an owned control loop",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    save_figure(fig, "fig-48-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
