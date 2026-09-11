"""Figure 42.1: level, seasonality, irregular variation, and events."""

import csv
import sys
from datetime import date
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch42_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    dates = [date.fromisoformat(r["week_start"]) for r in rows]
    actual = [float(r["cases_shipped"]) for r in rows]
    trend = [float(r["trend_level_cases"]) for r in rows]
    seasonal = [float(r["seasonal_component_cases"]) for r in rows]
    irregular = [float(r["irregular_component_cases"]) for r in rows]
    event = [float(r["event_adjustment_cases"]) for r in rows]

    apply_style()
    fig, axes = plt.subplots(2, 1, figsize=(7.4, 4.25), sharex=True, gridspec_kw={"height_ratios": (1.25, 1)})
    axes[0].plot(dates, actual, color=BLUE, lw=1.25, label="observed shipments")
    axes[0].plot(dates, trend, color=NAVY, ls="--", lw=1.2, label="trend level")
    axes[0].scatter([d for d, v in zip(dates, event) if v], [y for y, v in zip(actual, event) if v], color=RED, s=28, label="event weeks", zorder=4)
    axes[0].set(ylabel="Cases shipped", title="Observed demand combines several time structures")
    axes[0].legend(frameon=False, ncol=3, fontsize=7.2)
    axes[1].plot(dates, seasonal, color=TEAL, label="annual seasonality")
    axes[1].plot(dates, irregular, color=GOLD, alpha=0.72, label="irregular variation")
    axes[1].stem(dates, event, linefmt=RED, markerfmt=" ", basefmt=" ", label="event adjustment")
    axes[1].axhline(0, color="#AAB4BB", lw=0.7)
    axes[1].set(ylabel="Component (cases)", xlabel="Week", title="Components have different interpretations")
    axes[1].legend(frameon=False, ncol=3, fontsize=7.2)
    axes[1].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    fig.suptitle("Plot the series before choosing a forecasting method", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save_figure(fig, "fig-42-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
