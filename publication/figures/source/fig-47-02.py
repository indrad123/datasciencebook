"""Figure 47.2: repeated permutation importance and interpretation limits."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def raw_score(model, x):
    probability = np.clip(model.predict_proba(x)[:, 1], 0.02, 0.98)
    return 1 / (1 + np.exp(-(1.30 * np.log(probability / (1 - probability)) - 0.15)))


def main():
    with (ROOT / "data/generated/ch47_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    x = np.array([[float(r["route_distance_km"]), float(r["port_congestion_index"]), int(r["fragile_product"])] for r in rows])
    y = np.array([int(r["actual_late"]) for r in rows])
    split = np.array([r["split"] for r in rows])
    train, calibration, test = split == "train", split == "calibration", split == "test"
    model = RandomForestClassifier(n_estimators=240, min_samples_leaf=8, max_features=None,
                                   random_state=47, n_jobs=1).fit(x[train], y[train])
    calibrator = LogisticRegression(C=1e6, solver="lbfgs", random_state=47).fit(
        raw_score(model, x[calibration])[:, None], y[calibration])

    def predict(values):
        return calibrator.predict_proba(raw_score(model, values)[:, None])[:, 1]

    base = brier_score_loss(y[test], predict(x[test]))
    repeated = []
    for j in range(x.shape[1]):
        changes = []
        for seed in range(47, 77):
            shuffled = x[test].copy()
            rng = np.random.default_rng(seed + 100 * j)
            shuffled[:, j] = rng.permutation(shuffled[:, j])
            changes.append(brier_score_loss(y[test], predict(shuffled)) - base)
        repeated.append(changes)
    repeated = np.array(repeated)
    means, spreads = repeated.mean(axis=1), repeated.std(axis=1)
    labels = ["Route distance", "Port congestion", "Fragile product"]

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.2), gridspec_kw={"width_ratios": [1.12, 0.88]})
    order = np.argsort(means)
    axes[0].barh(np.arange(3), means[order], xerr=spreads[order], color=[BLUE, TEAL, "#6C83A2"],
                 alpha=0.9, capsize=3)
    axes[0].axvline(0, color=NAVY, linewidth=0.9)
    axes[0].set(yticks=np.arange(3), yticklabels=np.array(labels)[order],
                xlabel="Increase in test Brier score after shuffling\nMean ± SD across 30 shuffles",
                title="Repeated permutation importance")

    axes[1].axis("off")
    cards = [
        (0.80, "Specific, not universal", "Importance depends on this model,\ntest population and Brier metric.", LIGHT_BLUE),
        (0.49, "Correlated inputs can substitute", "Shuffling can hide shared signal or\ncreate unrealistic combinations.", LIGHT_GOLD),
        (0.18, "Association is not causation", "Reliance does not prove a cause, a fair\nprocess or a useful intervention.", "#F7DEDC"),
    ]
    for y0, heading, body, color in cards:
        axes[1].text(0.04, y0, heading, transform=axes[1].transAxes, color=NAVY, weight="bold", fontsize=8.1,
                     bbox=dict(boxstyle="round,pad=0.45", facecolor=color, edgecolor="none"))
        axes[1].text(0.04, y0 - 0.13, body, transform=axes[1].transAxes, color=NAVY, fontsize=7.2, va="top")
    axes[1].set_title("Read importance as governed evidence", color=NAVY, weight="bold")
    fig.suptitle("Global importance shows model reliance—and requires validation cautions", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.02, 1, 0.93))
    save_figure(fig, "fig-47-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
