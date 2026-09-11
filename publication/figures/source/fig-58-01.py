"""Figure 58.1: responsibility and incident-aware deployment flow."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, y, title, detail, face):
    ax.add_patch(FancyBboxPatch((x - 0.64, y - 0.43), 1.28, 0.86,
                               boxstyle="round,pad=0.04,rounding_size=0.05",
                               facecolor=face, edgecolor=TEAL, linewidth=1.1))
    ax.text(x, y + 0.15, title, ha="center", va="center", color=NAVY, fontsize=7, weight="bold")
    ax.text(x, y - 0.12, detail, ha="center", va="center", color=NAVY, fontsize=5.8)


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 4.5))
    ax.axis("off")
    xs = [0.75, 2.18, 3.61, 5.04, 6.47]
    stages = [
        ("Capture and join", "device owner\ndata steward"),
        ("Predict", "technical owner\nversion + threshold"),
        ("Review", "inspector\ntime + authority"),
        ("Act", "quality operations\nfallback available"),
        ("Outcome", "business owner\ndelayed evidence"),
    ]
    for i, (x, (title, detail)) in enumerate(zip(xs, stages)):
        box(ax, x, 2.75, title, detail, LIGHT_BLUE if i % 2 == 0 else LIGHT_GOLD)
        if i:
            ax.add_patch(FancyArrowPatch((xs[i - 1] + 0.66, 2.75), (x - 0.66, 2.75),
                                         arrowstyle="-|>", mutation_scale=11, color=TEAL, linewidth=1.3))
    box(ax, 2.18, 1.15, "Monitor", "service + inputs\nqueues + slices", LIGHT_GOLD)
    box(ax, 4.32, 1.15, "Incident response", "contain + preserve\nevidence + communicate", "#f7dddd")
    box(ax, 6.47, 1.15, "Controlled change", "regression tests\napproval + rollback", LIGHT_GOLD)
    ax.add_patch(FancyArrowPatch((6.47, 2.30), (4.70, 1.58), arrowstyle="-|>", mutation_scale=11,
                                 color=RED, linewidth=1.2, connectionstyle="arc3,rad=0.12"))
    ax.add_patch(FancyArrowPatch((3.67, 1.15), (2.84, 1.15), arrowstyle="-|>", mutation_scale=11,
                                 color=RED, linewidth=1.2))
    ax.add_patch(FancyArrowPatch((4.98, 1.15), (5.81, 1.15), arrowstyle="-|>", mutation_scale=11,
                                 color=TEAL, linewidth=1.2))
    ax.text(4.35, 0.35, "Release authority and responsibility remain with named people—not the model.",
            ha="center", color=NAVY, fontsize=7.2, weight="bold")
    ax.set(xlim=(0, 7.25), ylim=(0.08, 3.45))
    fig.suptitle("A reliable prediction requires a responsible and reversible operating system",
                 color=NAVY, weight="bold", fontsize=11.5)
    fig.tight_layout(rect=(0, 0.02, 1, 0.92))
    save_figure(fig, "fig-58-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
