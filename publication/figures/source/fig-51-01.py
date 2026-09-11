"""Figure 51.1: dense-layer shapes through a multiclass forward pass."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, TEAL, apply_style, save_figure


def box(ax, x, y, text, face, width=1.30, height=1.00, fontsize=7.0):
    patch = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                           boxstyle="round,pad=0.04,rounding_size=0.06",
                           facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY,
            fontsize=fontsize, weight="bold")


def arrow(ax, x1, x2, y=1.85):
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>", mutation_scale=11,
                                color=TEAL, linewidth=1.35, shrinkA=3, shrinkB=3))


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    box(ax, 0.75, 1.85, "Input batch $X$\n32 packages ×\n4 features", LIGHT_BLUE, 1.25)
    box(ax, 2.35, 1.85, "Dense hidden\n$Z^{(1)}=XW^{(1)}+b^{(1)}$\nshape (32, 6)", LIGHT_GOLD, 1.55)
    box(ax, 4.00, 1.85, "ReLU\n" + r"$A^{(1)}=\max(0,Z^{(1)})$" + "\nshape (32, 6)", "#DCEFE9", 1.45)
    box(ax, 5.65, 1.85, "Output logits\n$Z^{(2)}=A^{(1)}W^{(2)}+b^{(2)}$\nshape (32, 3)", LIGHT_GOLD, 1.55)
    box(ax, 7.25, 1.85, "Softmax\nnormal · inspect · reject\nrows sum to 1", LIGHT_BLUE, 1.30, fontsize=6.4)
    for x1, x2 in [(1.38, 1.57), (3.13, 3.27), (4.73, 4.87), (6.43, 6.60)]:
        arrow(ax, x1, x2)
    ax.text(1.48, 2.52, "$W^{(1)}$: (4, 6)\n$b^{(1)}$: (6,)", ha="center", color=NAVY, fontsize=6.7)
    ax.text(4.80, 2.52, "$W^{(2)}$: (6, 3)\n$b^{(2)}$: (3,)", ha="center", color=NAVY, fontsize=6.7)
    ax.text(2.35, 0.75, "Layer 1: 4×6 + 6 = 30 parameters", ha="center",
            color=NAVY, fontsize=7.2, weight="bold")
    ax.text(5.65, 0.75, "Layer 2: 6×3 + 3 = 21 parameters", ha="center",
            color=NAVY, fontsize=7.2, weight="bold")
    ax.text(4.00, 0.30, "Total: 51 trainable parameters · forward propagation evaluates them but does not update them",
            ha="center", color=TEAL, fontsize=7.4, weight="bold")
    ax.set(xlim=(0, 8), ylim=(0.05, 3.05))
    ax.axis("off")
    fig.suptitle("Forward propagation preserves one observation per row through every layer",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.03, 1, 0.92))
    save_figure(fig, "fig-51-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
