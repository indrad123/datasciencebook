"""Figure 56.2: reconstruction error as a capacity-aware review signal."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch56_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    routine = rows[:-1]
    unusual = rows[-1]
    errors = np.array([float(r["reconstruction_mse"]) for r in routine])
    threshold = float(routine[0]["routine_error_p95"])
    unusual_error = float(unusual["reconstruction_mse"])
    all_errors = np.append(errors, unusual_error)
    order = np.argsort(all_errors)

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.3))
    axes[0].hist(errors, bins=12, color=BLUE, edgecolor="white")
    axes[0].axvline(threshold, color=GOLD, linestyle="--", linewidth=2,
                    label=f"routine 95th percentile = {threshold:.6f}")
    axes[0].set(xlabel="Routine-package reconstruction MSE", ylabel="Package count",
                title="Threshold must be fitted on reference data")
    axes[0].legend(frameon=False, fontsize=6.8)
    axes[0].grid(axis="y", alpha=0.15)

    colors = [RED if index == 60 else TEAL for index in order]
    axes[1].scatter(range(1, 62), all_errors[order], c=colors, s=25,
                    edgecolor="white", linewidth=0.4)
    axes[1].axhline(threshold, color=GOLD, linestyle="--", linewidth=1.5)
    axes[1].set_yscale("log")
    axes[1].set(xlabel="Packages ordered by reconstruction error", ylabel="Reconstruction MSE (log scale)",
                title="High error prioritizes review—not defect probability")
    axes[1].annotate(f"unusual package\nMSE = {unusual_error:.3f}",
                     xy=(61, unusual_error), xytext=(38, unusual_error / 25), color=RED,
                     arrowprops={"arrowstyle": "->", "color": RED}, fontsize=7)
    axes[1].grid(alpha=0.15, which="both")

    fig.suptitle("Reconstruction error can rank unusual packages without proving a defect",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.02,
             "A deployment threshold needs labeled validation, subgroup checks, workload limits, and expert review.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.06, 1, 0.92), w_pad=1.5)
    save_figure(fig, "fig-56-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
