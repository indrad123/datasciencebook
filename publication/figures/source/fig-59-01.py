"""Figure 59.1: auditable forecast-to-decision workflow."""
import sys
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, y, title, detail, face):
    ax.add_patch(FancyBboxPatch((x-.58, y-.42), 1.16, .84, boxstyle="round,pad=.04,rounding_size=.05",
                               facecolor=face, edgecolor=TEAL, linewidth=1.1))
    ax.text(x, y+.14, title, ha="center", va="center", color=NAVY, fontsize=7, weight="bold")
    ax.text(x, y-.12, detail, ha="center", va="center", color=NAVY, fontsize=5.8)


def main():
    apply_style(); fig, ax = plt.subplots(figsize=(8, 4.5)); ax.axis("off")
    xs = [.7, 2.05, 3.4, 4.75, 6.1]
    stages = [("Contract", "weekly product × DC\nknown-at-origin data"),
              ("Rolling origins", "same horizons\nbaselines + candidates"),
              ("Uncertainty", "lead-time errors\nscenarios + quantiles"),
              ("Feasible action", "inventory position\ncase packs + capacity"),
              ("Planner approval", "reason code\ncut-off + ownership")]
    for i, (x, stage) in enumerate(zip(xs, stages)):
        box(ax, x, 2.7, *stage, LIGHT_BLUE if i % 2 == 0 else LIGHT_GOLD)
        if i: ax.add_patch(FancyArrowPatch((xs[i-1]+.60, 2.7), (x-.60, 2.7), arrowstyle="-|>", mutation_scale=11, color=TEAL))
    box(ax, 2.05, 1.15, "Observe outcomes", "demand + service\nshortage + waste", LIGHT_GOLD)
    box(ax, 4.05, 1.15, "Monitor and learn", "error by horizon\ncost + overrides", LIGHT_BLUE)
    box(ax, 6.1, 1.15, "Fallback / rollback", "seasonal naive\nmanual exceptional plan", "#f7dddd")
    ax.add_patch(FancyArrowPatch((6.1, 2.26), (6.1, 1.59), arrowstyle="-|>", mutation_scale=11, color=RED))
    ax.add_patch(FancyArrowPatch((5.5, 1.15), (4.65, 1.15), arrowstyle="-|>", mutation_scale=11, color=TEAL))
    ax.add_patch(FancyArrowPatch((3.45, 1.15), (2.65, 1.15), arrowstyle="-|>", mutation_scale=11, color=TEAL))
    ax.add_patch(FancyArrowPatch((1.45, 1.15), (.7, 2.24), arrowstyle="-|>", mutation_scale=11, color=TEAL, connectionstyle="arc3,rad=-.2"))
    ax.text(3.4, .35, "Forecast quality is one gate in a governed replenishment system.", ha="center", color=NAVY, fontsize=7.5, weight="bold")
    ax.set(xlim=(0, 6.8), ylim=(.08, 3.35)); fig.suptitle("NRG turns time-aware evidence into a reversible inventory decision", color=NAVY, weight="bold", fontsize=11.5)
    fig.tight_layout(rect=(0, .01, 1, .92)); save_figure(fig, "fig-59-01", ROOT); plt.close(fig)


if __name__ == "__main__": main()
