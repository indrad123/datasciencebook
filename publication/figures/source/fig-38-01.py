"""Figure 38.1: neighbours, margins, and kernel similarity."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch38_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    x = np.array([[float(r["distance_scaled"]), float(r["wait_scaled"])] for r in rows])
    y = np.array([int(r["late_label"]) for r in rows])
    ranks = np.array([int(r["query_neighbor_rank"]) for r in rows])
    query = np.array([1.05, 0.40])
    grid = np.linspace(-1.85, 1.85, 220)
    xx, yy = np.meshgrid(grid, grid)

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 3.25))
    for ax in axes:
        ax.scatter(x[y == 0, 0], x[y == 0, 1], s=24, color=BLUE, label="ordinary")
        ax.scatter(x[y == 1, 0], x[y == 1, 1], s=27, marker="^", color=RED, label="late")
        ax.set(xlim=(-1.85, 1.85), ylim=(-1.85, 1.85), xlabel="Scaled distance", ylabel="Scaled wait")
        ax.set_aspect("equal")

    axes[0].scatter(*query, marker="*", s=145, color=GOLD, edgecolor=NAVY, zorder=5)
    for point in x[ranks <= 5]:
        axes[0].plot([query[0], point[0]], [query[1], point[1]], color=GOLD, lw=1)
    axes[0].set_title("Five nearest neighbours")

    margin_model = SVC(kernel="rbf", C=3.0, gamma=1.0).fit(x, y)
    scores = margin_model.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    axes[1].contour(xx, yy, scores, levels=[-1, 0, 1], colors=[TEAL, NAVY, TEAL], linestyles=["--", "-", "--"], linewidths=[1, 1.6, 1])
    axes[1].scatter(margin_model.support_vectors_[:, 0], margin_model.support_vectors_[:, 1], s=72, facecolors="none", edgecolors=GOLD, linewidths=1.3)
    axes[1].set_title("SVM boundary and margins")

    similarity = np.exp(-((xx - query[0]) ** 2 + (yy - query[1]) ** 2))
    axes[2].contourf(xx, yy, similarity, levels=np.linspace(0, 1, 9), cmap="Blues", alpha=0.75)
    axes[2].scatter(*query, marker="*", s=145, color=GOLD, edgecolor=NAVY, zorder=5)
    axes[2].set_title("RBF similarity to query")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False)
    fig.suptitle("Geometry defines neighbours, margins, and kernel similarity", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.09, 1, 0.91))
    save_figure(fig, "fig-38-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
