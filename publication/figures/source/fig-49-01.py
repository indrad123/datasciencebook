"""Figure 49.1: weakest-link readiness and value gate."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, y, text, face, width=1.55, height=0.68, fontsize=7.2):
    patch = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                           boxstyle="round,pad=0.04,rounding_size=0.06",
                           facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY, fontsize=fontsize, weight="bold")


def arrow(ax, start, end, color=TEAL):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=11,
                                color=color, linewidth=1.35, shrinkA=3, shrinkB=3))


def main():
    with (ROOT / "data/generated/ch49_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    pilot = next(r for r in rows if r["proposal_id"] == "P49-02")
    scores = [("Data", pilot["data_readiness"]), ("Baseline", pilot["baseline_readiness"]),
              ("Operations", pilot["operations_readiness"]), ("Governance", pilot["governance_readiness"])]
    net_m = float(pilot["annual_net_value_idr"]) / 1e6

    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    box(ax, 0.85, 2.40, "Decision +\nstrong baseline", LIGHT_BLUE, width=1.45)
    arrow(ax, (1.58, 2.40), (1.92, 2.40))
    for i, (label, score) in enumerate(scores):
        x = 2.55 + i * 1.20
        box(ax, x, 2.40, f"{label}\n{float(score):.2f}", LIGHT_GOLD, width=1.00, height=0.70, fontsize=6.9)
        if i < 3:
            arrow(ax, (x + 0.51, 2.40), (x + 0.68, 2.40))
    arrow(ax, (6.66, 2.40), (6.93, 2.40))
    box(ax, 7.55, 2.40, f"Net value check\nIDR {net_m:.1f}m > 0", LIGHT_BLUE, width=1.15, fontsize=6.7)

    arrow(ax, (7.55, 2.04), (7.55, 1.55))
    box(ax, 7.55, 1.10, "Bounded\nshadow pilot", "#DCEFE9", width=1.25)
    ax.text(4.35, 1.68, "all four readiness gates ≥ 0.60", ha="center", color=TEAL, fontsize=7.4, weight="bold")
    ax.plot((2.05, 6.65), (1.52, 1.52), color=RED, linestyle=":", linewidth=1.2)
    arrow(ax, (4.35, 1.50), (4.35, 1.08), RED)
    box(ax, 4.35, 0.63, "If any gate fails: repair the blocker or retain the simpler baseline",
        "#F7DEDC", width=4.10, height=0.62, fontsize=7.1)
    arrow(ax, (6.97, 2.08), (5.95, 0.95), RED)
    ax.text(6.18, 1.43, "or net value ≤ 0", color=RED, fontsize=7, weight="bold", rotation=-31)

    ax.set(xlim=(0, 8.25), ylim=(0.15, 3.05))
    ax.axis("off")
    fig.suptitle("Deep learning earns a pilot only by passing every readiness and value gate",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.045, "Illustrated with P49-02 transfer CNN; minimum readiness is 0.78",
             ha="center", color=NAVY, fontsize=7.4)
    fig.tight_layout(rect=(0, 0.07, 1, 0.92))
    save_figure(fig, "fig-49-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
