"""Figure 46.2: propensity overlap and covariate balance."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
from datasciencebook.causal import difference_in_means, standardized_mean_difference, weighted_effect
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch46_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    treatment = np.array([int(r["coached"]) for r in rows])
    propensity = np.array([float(r["estimated_propensity"]) for r in rows])
    weights = np.array([float(r["ipw_ate"]) for r in rows])
    outcome = np.array([float(r["observed_next_90d_sales_kidr"]) for r in rows])
    covariates = {
        "Prior sales": np.array([float(r["prior_90d_sales_kidr"]) for r in rows]),
        "Tenure": np.array([float(r["tenure_years"]) for r in rows]),
    }
    before = [standardized_mean_difference(x, treatment) for x in covariates.values()]
    after = [standardized_mean_difference(x, treatment, weights) for x in covariates.values()]
    raw = difference_in_means(outcome, treatment)
    adjusted = weighted_effect(outcome, treatment, weights)

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.8))
    bins = np.linspace(0, 1, 22)
    axes[0].hist(propensity[treatment == 0], bins=bins, alpha=0.62, color=BLUE, label="not coached")
    axes[0].hist(propensity[treatment == 1], bins=bins, alpha=0.62, color=GOLD, label="coached")
    axes[0].set(xlabel="Estimated coaching propensity", ylabel="Distributors", title="Overlap before weighting", xlim=(0, 1))
    axes[0].legend(frameon=False)

    y = np.arange(len(covariates))
    axes[1].scatter(np.abs(before), y, color=RED, marker="s", s=55, label="before")
    axes[1].scatter(np.abs(after), y, color=TEAL, marker="o", s=55, label="after IPW")
    for i, (a, b) in enumerate(zip(before, after)):
        axes[1].plot((abs(a), abs(b)), (i, i), color="#B7C0C7", linewidth=1)
    axes[1].axvline(0.10, color=NAVY, linestyle=":", linewidth=1.2, label="0.10 guide")
    axes[1].set(yticks=y, yticklabels=covariates, xlabel="Absolute standardized mean difference", title="Measured balance improves", xlim=(-0.015, 0.52), ylim=(-0.55, 1.55))
    axes[1].legend(frameon=False, loc="upper right")
    fig.text(0.5, 0.02, f"Observed mean difference: {raw:.2f} kIDR   |   IPW estimate: {adjusted:.2f} kIDR   |   simulated effect: 8.00 kIDR", ha="center", color=NAVY, fontsize=7.6, weight="bold")
    fig.suptitle("Propensity weighting targets balance, not treatment prediction", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.07, 1, 0.92))
    save_figure(fig, "fig-46-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
