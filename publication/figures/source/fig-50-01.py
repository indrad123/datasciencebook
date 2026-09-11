"""Figure 50.1: inputs, weighted sum, activation, and separate decision rule."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, TEAL, apply_style, save_figure


def node(ax, x, y, text, face, width, height=0.72, fontsize=7.3):
    patch = FancyBboxPatch(
        (x - width / 2, y - height / 2), width, height,
        boxstyle="round,pad=0.04,rounding_size=0.06",
        facecolor=face, edgecolor=NAVY, linewidth=1,
    )
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY,
            fontsize=fontsize, weight="bold")


def arrow(ax, start, end, label=""):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=11,
                                color=TEAL, linewidth=1.35, shrinkA=3, shrinkB=3))
    if label:
        ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.13,
                label, ha="center", color=NAVY, fontsize=7.1, weight="bold")


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    node(ax, 0.85, 2.55, "Impact score\n$x_1=0.8$", LIGHT_BLUE, 1.35)
    node(ax, 0.85, 1.25, "Moisture score\n$x_2=0.4$", LIGHT_BLUE, 1.35)
    node(ax, 3.05, 1.90, "Weighted sum\n$z=b+w_1x_1+w_2x_2$\n$=-1.4+1.8(0.8)+1.1(0.4)=0.48$",
         LIGHT_GOLD, 2.35, 1.08, 7.0)
    arrow(ax, (1.53, 2.55), (1.86, 2.15), "$w_1=1.8$")
    arrow(ax, (1.53, 1.25), (1.86, 1.65), "$w_2=1.1$")
    ax.text(3.05, 2.72, "bias $b=-1.4$ moves the boundary", ha="center",
            color=NAVY, fontsize=6.9)
    node(ax, 5.15, 1.90, "Sigmoid activation\n" + r"$p=\sigma(z)=0.618$", "#DCEFE9", 1.65)
    arrow(ax, (4.24, 1.90), (4.31, 1.90))
    node(ax, 7.05, 1.90, "Decision rule\ninspect if " + r"$p\geq0.50$", LIGHT_BLUE, 1.55)
    arrow(ax, (5.99, 1.90), (6.27, 1.90), "probability")

    ax.text(5.15, 0.78, "Activation estimates risk", ha="center", color=TEAL,
            fontsize=7.3, weight="bold")
    ax.text(7.05, 0.78, "Threshold selects an action", ha="center", color=NAVY,
            fontsize=7.3, weight="bold")
    ax.plot((6.08, 6.08), (0.57, 1.10), color=NAVY, linestyle=":", linewidth=1)
    ax.set(xlim=(0, 7.9), ylim=(0.35, 3.20))
    ax.axis("off")
    fig.suptitle("A binary neuron is a weighted sum followed by a smooth activation",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.045,
             "Predictive weights describe the fitted model; they do not establish causal effects.",
             ha="center", color=NAVY, fontsize=7.4)
    fig.tight_layout(rect=(0, 0.07, 1, 0.92))
    save_figure(fig, "fig-50-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
