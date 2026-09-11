"""Figure 47.1: reliability before and after separate recalibration."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
from datasciencebook.model_trust import brier_score, expected_calibration_error, reliability_table
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, NAVY, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch47_sample.csv").open(encoding="utf-8") as handle:
        rows = [r for r in csv.DictReader(handle) if r["split"] == "test"]
    y = np.array([int(r["actual_late"]) for r in rows])
    raw = np.array([float(r["raw_probability"]) for r in rows])
    calibrated = np.array([float(r["calibrated_probability"]) for r in rows])
    raw_table = reliability_table(y, raw, n_bins=8)
    calibrated_table = reliability_table(y, calibrated, n_bins=8)

    apply_style()
    fig, axes = plt.subplots(2, 1, figsize=(7.4, 5.2), gridspec_kw={"height_ratios": [3.3, 1]})
    ax = axes[0]
    ax.plot((0, 1), (0, 1), color=NAVY, linestyle=":", linewidth=1.2, label="perfect calibration")
    for table, color, marker, label in (
        (raw_table, GOLD, "s", "raw score"),
        (calibrated_table, TEAL, "o", "Platt calibrated"),
    ):
        means = np.array([r[2] for r in table])
        observed = np.array([r[3] for r in table])
        counts = np.array([r[1] for r in table])
        ax.plot(means, observed, color=color, linewidth=1.5, alpha=0.85)
        ax.scatter(means, observed, s=18 + 1.15 * counts, color=color, marker=marker,
                   edgecolor="white", linewidth=0.7, label=label, zorder=3)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Mean predicted late-delivery probability",
           ylabel="Observed late-delivery frequency", title="Untouched test set: 250 shipments")
    ax.legend(frameon=False, loc="upper left")

    bins = np.linspace(0, 1, 9)
    axes[1].hist(raw, bins=bins, color=GOLD, alpha=0.62, label="raw")
    axes[1].hist(calibrated, bins=bins, color=BLUE, alpha=0.62, label="calibrated")
    axes[1].set(xlim=(0, 1), xlabel="Probability bin", ylabel="Count", title="Bin support changes after recalibration")
    axes[1].legend(frameon=False, ncol=2)

    raw_brier = brier_score(y, raw)
    calibrated_brier = brier_score(y, calibrated)
    raw_ece = expected_calibration_error(y, raw, 8)
    calibrated_ece = expected_calibration_error(y, calibrated, 8)
    fig.suptitle("Recalibration improves probability meaning without changing the ranking", color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.012,
             f"Brier: {raw_brier:.3f} → {calibrated_brier:.3f}   |   8-bin ECE: {raw_ece:.3f} → {calibrated_ece:.3f}   |   bubble area reflects bin count",
             ha="center", color=NAVY, fontsize=7.5, weight="bold")
    fig.tight_layout(rect=(0, 0.06, 1, 0.94))
    save_figure(fig, "fig-47-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
