"""Figure 49.2: candidate value versus cost and quality sensitivity."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch49_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    cost = np.array([float(r["annual_lifecycle_cost_idr"]) / 1e6 for r in rows])
    value = np.array([float(r["gross_incremental_value_idr"]) / 1e6 for r in rows])
    readiness = np.array([float(r["minimum_readiness"]) for r in rows])
    pilot = np.array([r["recommendation"] == "pilot" for r in rows])

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.3))
    limit = 475
    axes[0].plot((0, limit), (0, limit), color=NAVY, linestyle=":", linewidth=1.2, label="gross value = cost")
    axes[0].scatter(cost[~pilot], value[~pilot], s=70 + 90 * readiness[~pilot], color=RED,
                    alpha=0.82, marker="s", label="retain simpler baseline")
    axes[0].scatter(cost[pilot], value[pilot], s=70 + 90 * readiness[pilot], color=TEAL,
                    alpha=0.9, marker="o", label="pilot")
    offsets = [(5, -10), (5, 7), (5, 7), (5, 7), (5, -10), (5, 7), (5, -10), (-44, 7)]
    for r, x, y, offset in zip(rows, cost, value, offsets):
        axes[0].annotate(r["proposal_id"], (x, y), xytext=offset, textcoords="offset points",
                         fontsize=6.5, color=NAVY)
    axes[0].set(xlim=(0, limit), ylim=(0, 320), xlabel="Annual lifecycle cost (million IDR)",
                ylabel="Gross incremental value (million IDR)", title="Eight candidate proposals")
    axes[0].legend(frameon=False, fontsize=6.7, loc="upper left")

    example = rows[0]
    annual_packages = float(example["annual_packages"])
    value_per_correction = float(example["value_per_corrected_decision_idr"])
    example_cost = float(example["annual_lifecycle_cost_idr"]) / 1e6
    gains = np.linspace(0, 0.045, 100)
    gross = annual_packages * gains * value_per_correction / 1e6
    break_even = example_cost * 1e6 / (annual_packages * value_per_correction)
    axes[1].plot(gains * 100, gross, color=BLUE, linewidth=2, label="gross incremental value")
    axes[1].axhline(example_cost, color=RED, linestyle="--", label=f"lifecycle cost: {example_cost:.1f}m")
    axes[1].axvline(break_even * 100, color=GOLD, linestyle=":", label=f"break-even: {break_even * 100:.2f} pp")
    axes[1].scatter(2.0, 180, color=RED, marker="s", s=65, zorder=3)
    axes[1].annotate("P49-01\n2.00 pp, −57.5m net", (2.0, 180), xytext=(8, -25),
                     textcoords="offset points", fontsize=6.8, color=NAVY)
    axes[1].set(xlim=(0, 4.5), ylim=(0, 420), xlabel="Absolute error reduction (percentage points)",
                ylabel="Annual amount (million IDR)", title="Quality gain must repay full cost")
    axes[1].legend(frameon=False, fontsize=6.7, loc="upper left")

    fig.suptitle("Incremental quality is valuable only after full lifecycle cost and readiness",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    save_figure(fig, "fig-49-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
