"""Figure 52.1: cached forward values and backward gradients."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def node(ax, x, y, text, face, width=1.12, height=0.72, fontsize=6.7):
    patch = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                           boxstyle="round,pad=0.04,rounding_size=0.05",
                           facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY,
            fontsize=fontsize, weight="bold")


def arrow(ax, start, end, color, direction="right"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=10,
                                color=color, linewidth=1.25, shrinkA=3, shrinkB=3))


def main():
    with (ROOT / "data/generated/ch52_sample.csv").open(encoding="utf-8") as handle:
        first = next(csv.DictReader(handle))
    difference = float(first["absolute_gradient_check_difference"])

    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    xs = [0.65, 1.96, 3.27, 4.58, 5.89, 7.20]
    forward_text = [
        "Inputs\n$X$, labels $Y$", r"$Z_1=XW_1+b_1$", r"$A_1=\tanh(Z_1)$",
        r"$Z_2=A_1W_2+b_2$", r"$P=\sigma(Z_2)$", "Binary cross-\nentropy $L$",
    ]
    for i, (x, label) in enumerate(zip(xs, forward_text)):
        node(ax, x, 2.75, label, LIGHT_BLUE if i in (0, 5) else LIGHT_GOLD, width=1.08)
        if i:
            arrow(ax, (xs[i - 1] + 0.55, 2.75), (x - 0.55, 2.75), TEAL)
    ax.text(3.93, 3.42, "FORWARD: compute and cache values", ha="center",
            color=TEAL, fontsize=8, weight="bold")

    backward_text = [
        r"$\nabla W_1=X^T dZ_1$", r"$dZ_1=dA_1(1-A_1^2)$",
        r"$dA_1=dZ_2W_2^T$", r"$\nabla W_2=A_1^T dZ_2$",
        r"$dZ_2=(P-Y)/n$",
    ]
    back_x = [1.20, 2.55, 3.90, 5.25, 6.60]
    for i, (x, label) in enumerate(zip(back_x, backward_text)):
        node(ax, x, 1.35, label, "#F7DEDC", width=1.20, height=0.66, fontsize=6.4)
        if i:
            arrow(ax, (x - 0.61, 1.35), (back_x[i - 1] + 0.61, 1.35), RED)
    arrow(ax, (7.20, 2.38), (6.60, 1.69), RED)
    ax.text(3.90, 0.72, "BACKWARD: reuse caches and apply the chain rule from loss to inputs",
            ha="center", color=RED, fontsize=8, weight="bold")
    ax.text(3.90, 0.25,
            f"Gradient check for $W_1[0,0]$: analytical and central difference agree within {difference:.1e}",
            ha="center", color=NAVY, fontsize=7.2)
    ax.set(xlim=(0, 7.85), ylim=(0.02, 3.75))
    ax.axis("off")
    fig.suptitle("Backpropagation assigns credit by reversing the cached forward graph",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.02, 1, 0.92))
    save_figure(fig, "fig-52-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
