"""Figure 40.2: explained variance and reconstruction trade-off."""

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


def main():
    with (ROOT / "data/generated/ch40_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    values = np.array([[float(r[f]) for f in FEATURES] for r in rows])
    training = np.array([r["evaluation_split"] == "training" for r in rows])
    scaler = StandardScaler().fit(values[training])
    scaled = scaler.transform(values)
    full = PCA(svd_solver="full").fit(scaled[training])
    components = np.arange(1, len(FEATURES) + 1)
    cumulative = np.cumsum(full.explained_variance_ratio_)
    train_rmse, test_rmse = [], []
    for k in components:
        model = PCA(n_components=k, svd_solver="full").fit(scaled[training])
        reconstructed = model.inverse_transform(model.transform(scaled))
        row_rmse = np.sqrt(np.mean((scaled - reconstructed) ** 2, axis=1))
        train_rmse.append(row_rmse[training].mean())
        test_rmse.append(row_rmse[~training].mean())

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.45))
    axes[0].bar(components, full.explained_variance_ratio_, color=BLUE, alpha=0.8, label="component share")
    axes[0].plot(components, cumulative, color=RED, marker="o", label="cumulative share")
    axes[0].axhline(0.90, color=GOLD, ls="--", lw=1.2, label="90% guide")
    axes[0].set(xlabel="Number of components", ylabel="Share of training variance", xticks=components, ylim=(0, 1.05), title="Input variance has diminishing returns")
    axes[0].legend(frameon=False, fontsize=7.2)
    axes[1].plot(components - 0.025, train_rmse, color=TEAL, marker="o", ls="--", label="training", zorder=3)
    axes[1].plot(components + 0.025, test_rmse, color=GOLD, marker="s", label="test", zorder=2)
    axes[1].axvline(2, color=NAVY, ls="--", lw=1.2)
    axes[1].set(xlabel="Number of components", ylabel="Mean row reconstruction RMSE", xticks=components, title="Reconstruction checks information loss")
    axes[1].set_ylim(bottom=0)
    axes[1].legend(frameon=False)
    fig.suptitle("Component count follows purpose and validation evidence", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-40-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
