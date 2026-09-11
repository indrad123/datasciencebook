"""Figure 43.1: recommendation candidate-to-reranking pipeline."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, title, detail, face):
    patch = FancyBboxPatch((x, 0.33), 1.34, 0.72, boxstyle="round,pad=0.04,rounding_size=0.05", facecolor=face, edgecolor=NAVY, linewidth=1.0)
    ax.add_patch(patch)
    ax.text(x + 0.67, 0.82, title, ha="center", va="center", weight="bold", color=NAVY, fontsize=8)
    ax.text(x + 0.67, 0.57, detail, ha="center", va="center", color=NAVY, fontsize=6.9, linespacing=1.25)


def main():
    with (ROOT / "data/generated/ch43_sample.csv").open() as handle:
        rows = [r for r in csv.DictReader(handle) if r["distributor_id"] == "D43-002"]
    unseen = [r for r in rows if r["seen_in_training"] == "0"]
    eligible = [r for r in unseen if r["stock_available"] == "1" and r["market_eligible"] == "1"]
    final = [r for r in eligible if r["recommended_top_5"] == "1"]
    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 2.65))
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 1.55); ax.axis("off")
    stages = [
        (0.05, "Catalogue", "12 products\nand metadata", LIGHT_BLUE),
        (1.78, "Retrieve", f"{len(unseen)} unseen\ncandidates", LIGHT_BLUE),
        (3.51, "Score", "popularity +\nlatent compatibility", LIGHT_GOLD),
        (5.24, "Apply hard rules", f"{len(eligible)} in stock\nand market eligible", LIGHT_GOLD),
        (6.97, "Rerank", f"{len(final)} displayed\nwith diversity goal", LIGHT_BLUE),
    ]
    for x, title, detail, face in stages:
        box(ax, x, title, detail, face)
    for x in (1.42, 3.15, 4.88, 6.61):
        ax.add_patch(FancyArrowPatch((x, 0.69), (x + 0.31, 0.69), arrowstyle="-|>", mutation_scale=12, color=TEAL, linewidth=1.5))
    ax.text(4.25, 0.18, "Log every exclusion reason, score, position, exposure, and outcome", ha="center", color=RED, fontsize=7.4, weight="bold")
    fig.suptitle("Recommendation is a governed decision pipeline", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    save_figure(fig, "fig-43-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
