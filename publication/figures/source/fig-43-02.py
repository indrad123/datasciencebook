"""Figure 43.2: popularity and latent-factor ranking comparison."""

import csv
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def metrics(rows, rank_field):
    groups = {}
    for row in rows:
        groups.setdefault(row["distributor_id"], []).append(row)
    recalls, ndcgs = [], []
    for group in groups.values():
        target = next((r for r in group if r["held_out_relevant"] == "1"), None)
        if target is None:
            continue
        rank = int(target[rank_field])
        recalls.append(rank <= 5)
        ndcgs.append(1 / math.log2(rank + 1) if rank <= 5 else 0)
    recall = float(np.mean(recalls))
    return recall / 5, recall, float(np.mean(ndcgs)), len(recalls)


def main():
    with (ROOT / "data/generated/ch43_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    pop = metrics(rows, "popularity_unseen_rank")
    latent = metrics(rows, "latent_unseen_rank")
    example = [r for r in rows if r["distributor_id"] == "D43-002" and r["seen_in_training"] == "0"]
    pop_top = sorted(example, key=lambda r: int(r["popularity_unseen_rank"]))[:5]
    latent_top = sorted(example, key=lambda r: int(r["latent_unseen_rank"]))[:5]

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.3, 3.5))
    x = np.arange(3); width = 0.34
    axes[0].bar(x - width / 2, pop[:3], width, color=BLUE, label="popularity")
    axes[0].bar(x + width / 2, latent[:3], width, color=TEAL, label="latent factors")
    axes[0].set(xticks=x, xticklabels=("Precision@5", "Recall@5", "NDCG@5"), ylabel="Mean across held-out distributors", ylim=(0, 1.0), title=f"Offline relevance ({pop[3]} holdouts)")
    axes[0].legend(frameon=False)

    y = np.arange(1, 6)
    axes[1].scatter(np.zeros(5), y, color=BLUE, s=55, marker="s")
    axes[1].scatter(np.ones(5), y, color=GOLD, s=55, marker="s")
    for rank, (pop_row, latent_row) in enumerate(zip(pop_top, latent_top), 1):
        axes[1].plot((0, 1), (rank, rank), color="#D5DCE1", lw=0.8, zorder=0)
        axes[1].text(0.08, rank, pop_row["product_id"], va="center", fontsize=7.5, color=NAVY)
        axes[1].text(1.08, rank, latent_row["product_id"], va="center", fontsize=7.5, color=NAVY)
    axes[1].set(xlim=(-0.15, 1.42), ylim=(5.55, 0.45), xticks=(0, 1), xticklabels=("Popularity", "Latent factors"), yticks=y, yticklabels=[f"rank {i}" for i in y], title="D43-002 top-five lists differ")
    axes[1].spines["bottom"].set_visible(False)
    axes[1].tick_params(axis="x", length=0)
    fig.suptitle("Personalized ranking must beat strong baselines and broader checks", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-43-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
