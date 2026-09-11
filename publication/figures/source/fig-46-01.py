"""Figure 46.1: causal roles and adjustment decisions."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def node(ax, xy, label, face=LIGHT_BLUE, width=1.24, fontsize=7.2):
    x, y = xy
    patch = FancyBboxPatch((x - width / 2, y - 0.18), width, 0.36, boxstyle="round,pad=0.03,rounding_size=0.04", facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, label, ha="center", va="center", fontsize=fontsize, color=NAVY, weight="bold")


def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=11, color=TEAL, linewidth=1.35, shrinkA=2, shrinkB=2))


def main():
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 3.3))

    ax = axes[0]
    node(ax, (1.2, 1.62), "Prior sales\n(confounder)", LIGHT_GOLD)
    node(ax, (0.72, 0.66), "Coaching\n(treatment)")
    node(ax, (1.70, 0.66), "Future sales\n(outcome)")
    arrow(ax, (1.1, 1.43), (0.82, 0.85)); arrow(ax, (1.31, 1.43), (1.59, 0.85)); arrow(ax, (0.95, 0.66), (1.47, 0.66))
    ax.text(1.2, 0.16, "Adjust to block the\nbackdoor path", ha="center", color=RED, fontsize=7, weight="bold")
    ax.set_title("Confounder", color=NAVY, weight="bold")

    ax = axes[1]
    node(ax, (0.40, 1.25), "Coaching", width=0.60, fontsize=6.6)
    node(ax, (1.20, 1.25), "Engagement\n(mediator)", LIGHT_GOLD, width=0.70, fontsize=6.4)
    node(ax, (2.00, 1.25), "Future sales", width=0.65, fontsize=6.6)
    arrow(ax, (0.71, 1.25), (0.84, 1.25)); arrow(ax, (1.56, 1.25), (1.67, 1.25)); arrow(ax, (0.42, 0.96), (1.97, 0.96))
    ax.text(1.2, 0.40, "Do not adjust when estimating\nthe total coaching effect", ha="center", color=RED, fontsize=7, weight="bold")
    ax.set_title("Mediator", color=NAVY, weight="bold")

    ax = axes[2]
    node(ax, (0.62, 1.56), "Poor service")
    node(ax, (1.78, 1.56), "Manager attention")
    node(ax, (1.2, 0.72), "Escalation\n(collider)", LIGHT_GOLD)
    arrow(ax, (0.78, 1.37), (1.08, 0.91)); arrow(ax, (1.62, 1.37), (1.32, 0.91))
    ax.text(1.2, 0.16, "Conditioning can open a\nspurious association", ha="center", color=RED, fontsize=7, weight="bold")
    ax.set_title("Collider", color=NAVY, weight="bold")

    for ax in axes:
        ax.set(xlim=(0, 2.4), ylim=(0, 2.0)); ax.axis("off")
    fig.suptitle("Adjustment depends on a variable's assumed causal role", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-46-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
