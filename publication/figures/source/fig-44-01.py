"""Figure 44.1: governed text-to-routing pipeline."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def stage(ax, x, heading, detail, face):
    patch = FancyBboxPatch(
        (x, 0.48), 1.32, 0.88, boxstyle="round,pad=0.04,rounding_size=0.05",
        facecolor=face, edgecolor=NAVY, linewidth=1.0
    )
    ax.add_patch(patch)
    ax.text(x + 0.66, 1.08, heading, ha="center", va="center", color=NAVY, fontsize=8, weight="bold")
    ax.text(x + 0.66, 0.77, detail, ha="center", va="center", color=NAVY, fontsize=6.8, linespacing=1.25)


def main():
    with (ROOT / "data/generated/ch44_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    training = sum(r["split"] == "train" for r in rows)
    testing = len(rows) - training
    reviews = sum(r["split"] == "test" and r["review_required"] == "1" for r in rows)

    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 3.0))
    ax.set(xlim=(0, 8.55), ylim=(0, 1.95)); ax.axis("off")
    stages = (
        (0.03, "Govern text", "immutable raw record\nredaction + access", LIGHT_BLUE),
        (1.76, "Split safely", f"conversation + time\n{training} train / {testing} test", LIGHT_BLUE),
        (3.49, "Represent", "tokenize; fit TF-IDF\non training only", LIGHT_GOLD),
        (5.22, "Classify", "four-route linear\nmodel + confidence", LIGHT_GOLD),
        (6.95, "Act or review", f"route if confident\n{reviews} test reviews", LIGHT_BLUE),
    )
    for args in stages:
        stage(ax, *args)
    for x in (1.40, 3.13, 4.86, 6.59):
        ax.add_patch(FancyArrowPatch((x, 0.92), (x + 0.31, 0.92), arrowstyle="-|>", mutation_scale=12, color=TEAL, linewidth=1.5))
    ax.text(4.27, 0.20, "Log representation, model, threshold, route, reviewer correction, and outcome", ha="center", color=RED, fontsize=7.2, weight="bold")
    fig.suptitle("Text becomes an operational decision through governed choices", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-44-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
