"""Figure 39.2: candidate cluster-count diagnostics."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch39_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    x = np.array([[float(r["orders_scaled"]), float(r["mix_scaled"])] for r in rows])
    ks = np.arange(2, 7)
    inertia, silhouette, stability, minimum_size = [], [], [], []
    for k in ks:
        reference = KMeans(n_clusters=k, n_init=20, random_state=3900 + k).fit(x)
        inertia.append(reference.inertia_)
        silhouette.append(silhouette_score(x, reference.labels_))
        minimum_size.append(min(np.bincount(reference.labels_)))
        scores = []
        for seed in range(10):
            jitter = np.column_stack((0.012 * np.sin(np.arange(len(x)) + seed), 0.012 * np.cos(2 * np.arange(len(x)) + seed)))
            candidate = KMeans(n_clusters=k, n_init=10, random_state=seed).fit(x + jitter)
            scores.append(adjusted_rand_score(reference.labels_, candidate.labels_))
        stability.append(np.mean(scores))

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.45))
    axes[0].plot(ks, np.array(inertia) / inertia[0], marker="o", color=BLUE, label="relative inertia")
    axes[0].plot(ks, silhouette, marker="s", color=RED, label="mean silhouette")
    axes[0].axvline(3, color=GOLD, ls="--", lw=1.5)
    axes[0].set(xlabel="Candidate number of clusters (k)", ylabel="Diagnostic value", xticks=ks, ylim=(0, 1.05), title="Geometry offers several signals")
    axes[0].legend(frameon=False)
    axes[1].bar(ks - 0.15, stability, width=0.3, color=TEAL, label="perturbation stability")
    axes[1].bar(ks + 0.15, np.array(minimum_size) / len(x), width=0.3, color=GOLD, label="smallest segment share")
    axes[1].axvline(3, color=NAVY, ls="--", lw=1.2)
    axes[1].set(xlabel="Candidate number of clusters (k)", ylabel="Proportion or agreement", xticks=ks, ylim=(0, 1.05), title="Stability and viability also matter")
    axes[1].legend(frameon=False, fontsize=7.5)
    fig.suptitle("Cluster count is a governed choice, not one automatic answer", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-39-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
