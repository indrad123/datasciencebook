"""Figure 40.1: original variables, loadings, and product scores."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure

FEATURES = ("weekly_unit_volume", "weekly_order_count", "stockout_rate", "contribution_margin_pct", "promotion_share", "supplier_lead_days")
SHORT = ("unit volume", "order count", "stockout rate", "margin", "promotion", "lead time")


def main():
    with (ROOT / "data/generated/ch40_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    values = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    training = np.array([r["evaluation_split"] == "training" for r in rows])
    scaler = StandardScaler().fit(values[training])
    scaled = scaler.transform(values)
    pca = PCA(n_components=2, svd_solver="full").fit(scaled[training])
    scores = pca.transform(scaled)

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.65))
    colors = {"training": BLUE, "test": GOLD}
    for split in ("training", "test"):
        mask = np.array([r["evaluation_split"] == split for r in rows])
        axes[0].scatter(scores[mask, 0], scores[mask, 1], s=24, alpha=0.72, color=colors[split], label=split)
    axes[0].axhline(0, color="#B9C1C7", lw=0.7)
    axes[0].axvline(0, color="#B9C1C7", lw=0.7)
    axes[0].set(xlabel="Principal component 1 score", ylabel="Principal component 2 score", title="Scores locate products")
    axes[0].legend(frameon=False)

    loading_colors = (BLUE, BLUE, RED, TEAL, TEAL, GOLD)
    label_positions = {"unit volume": (0.56, -0.42), "order count": (0.56, -0.34)}
    for j, (label, color) in enumerate(zip(SHORT, loading_colors)):
        x, y = pca.components_[0, j], pca.components_[1, j]
        axes[1].arrow(0, 0, x, y, color=color, width=0.008, head_width=0.055, length_includes_head=True)
        lx, ly = label_positions.get(label, (x * 1.12, y * 1.12))
        axes[1].text(lx, ly, label, ha="center", va="center", fontsize=7.2, color=NAVY)
    axes[1].axhline(0, color="#B9C1C7", lw=0.7)
    axes[1].axvline(0, color="#B9C1C7", lw=0.7)
    axes[1].set(xlim=(-0.8, 0.8), ylim=(-0.8, 0.8), xlabel="PC1 loading", ylabel="PC2 loading", title="Loadings describe contributions", aspect="equal")
    fig.suptitle("PCA replaces six measured features with new coordinates", color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.015, "Scaler and component directions fitted on 180 training products; 60 test products are transformed only", ha="center", fontsize=7.2, color=NAVY)
    fig.tight_layout(rect=(0, 0.055, 1, 0.92))
    save_figure(fig, "fig-40-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
