"""Figure 45.2: Kaplan-Meier curves, uncertainty, and risk counts."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, NAVY, TEAL, apply_style, save_figure
from src.datasciencebook.survival import kaplan_meier, restricted_mean_survival, survival_at


def curve_and_interval(duration, event):
    curve = kaplan_meier(duration, event)
    variance_sum = 0.0
    lower, upper = [], []
    for n, d, survival in zip(curve["at_risk"], curve["events"], curve["survival"]):
        if n > d:
            variance_sum += d / (n * (n - d))
        if 0 < survival < 1 and variance_sum > 0:
            transform = np.log(-np.log(survival))
            se = np.sqrt(variance_sum) / abs(np.log(survival))
            lower.append(np.exp(-np.exp(transform + 1.96 * se)))
            upper.append(np.exp(-np.exp(transform - 1.96 * se)))
        else:
            lower.append(survival)
            upper.append(survival)
    return curve, np.asarray(lower), np.asarray(upper)


def main():
    with (ROOT / "data/generated/ch45_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    apply_style()
    fig = plt.figure(figsize=(7.4, 5.0))
    grid = fig.add_gridspec(2, 1, height_ratios=(4, 1), hspace=0.16)
    ax = fig.add_subplot(grid[0])
    table = fig.add_subplot(grid[1], sharex=ax)
    colors = {"standard": BLUE, "enhanced": TEAL}
    horizons = np.array([0, 6, 12, 18, 24, 30])
    for group in ("standard", "enhanced"):
        subset = [r for r in rows if r["retention_program"] == group]
        duration = np.array([float(r["observed_followup_months"]) for r in subset])
        event = np.array([int(r["event_observed"]) for r in subset])
        curve, lower, upper = curve_and_interval(duration, event)
        x = np.r_[0, curve["time"]]
        ax.step(x, np.r_[1, curve["survival"]], where="post", color=colors[group], linewidth=1.8, label=group)
        ax.fill_between(x, np.r_[1, lower], np.r_[1, upper], step="post", color=colors[group], alpha=0.14)
        counts = [int(np.sum(duration >= h)) for h in horizons]
        y = 1 if group == "standard" else 0
        for h, count in zip(horizons, counts):
            table.text(h, y, str(count), ha="center", va="center", color=colors[group], fontsize=8)
        s24 = float(survival_at(curve, [24])[0])
        rmst = restricted_mean_survival(curve, 24)
        ax.text(31.3, 0.77 if group == "enhanced" else 0.45, f"{group}\nS(24)={s24:.3f}\nRMST\u2082\u2084={rmst:.2f} mo", color=colors[group], fontsize=7.2)
    ax.set(xlim=(0, 37), ylim=(0, 1.03), ylabel="Estimated churn-free survival")
    ax.legend(frameon=False, loc="lower left")
    ax.set_title("Kaplan–Meier comparison with 95% log–log intervals", color=NAVY, weight="bold")
    ax.tick_params(axis="x", labelbottom=False)
    table.set(ylim=(-0.6, 1.6), yticks=(), xticks=horizons, xlabel="Months after distributor entry")
    table.text(-0.035, 1, "standard", transform=table.get_yaxis_transform(), ha="right", va="center", fontsize=8)
    table.text(-0.035, 0, "enhanced", transform=table.get_yaxis_transform(), ha="right", va="center", fontsize=8)
    table.text(0, 1.52, "Number at risk", ha="left", va="center", fontsize=8, weight="bold")
    table.spines[["left", "right", "top"]].set_visible(False)
    table.tick_params(axis="y", length=0)
    fig.subplots_adjust(left=0.15, right=0.97, bottom=0.12, top=0.91)
    save_figure(fig, "fig-45-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
