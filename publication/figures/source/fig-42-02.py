"""Figure 42.2: rolling origins and issued forecast uncertainty."""

import csv
import sys
from datetime import date
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure

SEASON = 52


def seasonal_naive(history, horizon):
    return np.resize(history[-SEASON:], horizon)


def main():
    with (ROOT / "data/generated/ch42_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    dates = np.array([date.fromisoformat(r["week_start"]) for r in rows])
    actual = np.array([float(r["cases_shipped"]) for r in rows])
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.6))

    axes[0].plot(dates[65:143], actual[65:143], color=NAVY, lw=1.1, label="actual")
    origin_colors = (BLUE, TEAL, GOLD, RED)
    for end, color in zip((91, 104, 117, 130), origin_colors):
        horizon = 13
        forecast = seasonal_naive(actual[:end], horizon)
        axes[0].plot(dates[end:end + horizon], forecast, color=color, lw=1.5, marker="o", ms=2.7, label=f"origin {end}")
        axes[0].axvline(dates[end - 1], color=color, alpha=0.25, lw=0.7)
    axes[0].set(xlabel="Target week", ylabel="Cases shipped", title="Rolling origins repeat the real task")
    axes[0].legend(frameon=False, fontsize=6.7, ncol=2)
    axes[0].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))

    holdout = rows[130:]
    hd = dates[130:]
    point = np.array([float(r["seasonal_naive_forecast_cases"]) for r in holdout])
    lower = np.array([float(r["seasonal_naive_lower_80"]) for r in holdout])
    upper = np.array([float(r["seasonal_naive_upper_80"]) for r in holdout])
    axes[1].fill_between(hd, lower, upper, color=GOLD, alpha=0.25, label="illustrative 80% interval")
    axes[1].plot(hd, point, color=GOLD, lw=1.5, label="issued seasonal naive")
    axes[1].plot(hd, actual[130:], color=NAVY, marker="o", ms=3, lw=1.1, label="actual")
    covered = int(np.sum((actual[130:] >= lower) & (actual[130:] <= upper)))
    axes[1].text(0.97, 0.06, f"Holdout coverage: {covered}/26\n(nominal 80%)", transform=axes[1].transAxes, ha="right", va="bottom", fontsize=7.2, color=RED)
    axes[1].set(xlabel="Target week", ylabel="Cases shipped", title="Uncertainty belongs with the vintage")
    axes[1].legend(frameon=False, fontsize=6.7)
    axes[1].xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    fig.suptitle("Forecast origin and horizon define the information boundary", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-42-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
