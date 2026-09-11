"""Figure 38.2: KNN, linear SVM, and RBF SVM boundaries."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch38_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    x = np.array([[float(r["distance_scaled"]), float(r["wait_scaled"])] for r in rows])
    y = np.array([int(r["late_label"]) for r in rows])
    grid = np.linspace(-1.9, 1.9, 240)
    xx, yy = np.meshgrid(grid, grid)
    mesh = np.c_[xx.ravel(), yy.ravel()]
    models = [
        ("KNN: k = 5", KNeighborsClassifier(n_neighbors=5, weights="distance")),
        ("Linear SVM: C = 1", SVC(kernel="linear", C=1.0)),
        ("RBF SVM: C = 3; γ = 1", SVC(kernel="rbf", C=3.0, gamma=1.0)),
    ]

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 3.15))
    for ax, (title, model) in zip(axes, models):
        model.fit(x, y)
        pred = model.predict(mesh).reshape(xx.shape)
        ax.contourf(xx, yy, pred, levels=[-0.5, 0.5, 1.5], colors=[LIGHT_BLUE, LIGHT_GOLD], alpha=0.8)
        ax.contour(xx, yy, pred, levels=[0.5], colors=[NAVY], linewidths=1.4)
        ax.scatter(x[y == 0, 0], x[y == 0, 1], s=23, color=BLUE, label="ordinary")
        ax.scatter(x[y == 1, 0], x[y == 1, 1], s=27, marker="^", color=RED, label="late")
        ax.set(title=title, xlabel="Scaled distance", ylabel="Scaled wait", xlim=(-1.9, 1.9), ylim=(-1.9, 1.9))
        ax.set_aspect("equal")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False)
    fig.suptitle("The same scaled data produce different decision boundaries", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.09, 1, 0.91))
    save_figure(fig, "fig-38-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
