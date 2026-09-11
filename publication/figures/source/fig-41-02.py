"""Figure 41.2: scores, review capacity, and precision at k."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch41_sample.csv").open() as handle:
        rows = [r for r in csv.DictReader(handle) if r["sample_role"] == "monitoring"]
    rows.sort(key=lambda r: int(r["monitoring_review_rank"]))
    ranks = np.arange(1, len(rows) + 1)
    scores = np.array([float(r["isolation_score"]) for r in rows])
    relevant = np.array([int(r["confirmed_relevant"]) for r in rows])
    precision = np.cumsum(relevant) / ranks

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.45))
    top = 20
    colors = [RED if relevant[i] else BLUE for i in range(top)]
    axes[0].bar(ranks[:top], scores[:top], color=colors, alpha=0.85)
    axes[0].axvline(5.5, color=GOLD, ls="--", lw=1.5)
    axes[0].set(xlabel="Review rank", ylabel="Isolation score", xticks=(1, 5, 10, 15, 20), title="A score becomes a finite queue")
    axes[0].text(0.98, 0.96, "red = confirmed relevant", transform=axes[0].transAxes, ha="right", va="top", fontsize=7, color=RED)

    axes[1].plot(ranks[:20], precision[:20], color=TEAL, marker="o", ms=4)
    axes[1].axvline(5, color=GOLD, ls="--", lw=1.5)
    axes[1].scatter(5, precision[4], s=75, color=GOLD, edgecolor=NAVY, zorder=4)
    axes[1].annotate(f"Precision@5 = {precision[4]:.2f}", (5, precision[4]), xytext=(18, -22), textcoords="offset points", fontsize=7.5, arrowprops=dict(arrowstyle="->", color=NAVY))
    axes[1].set(xlabel="Investigation capacity (k)", ylabel="Confirmed precision at k", xticks=(1, 5, 10, 15, 20), ylim=(0, 1.05), title="Yield changes with capacity")
    fig.suptitle("Anomaly scores rank evidence; they are not defect probabilities", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-41-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
