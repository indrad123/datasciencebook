"""Figure 10.1: accumulation with rectangles and trapezoids."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, RED, TEAL, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch10_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    starts = [float(r["interval_start_hour"]) for r in rows]
    ends = [float(r["interval_end_hour"]) for r in rows]
    start_rates = [float(r["start_rate_cases_per_hour"]) for r in rows]
    end_rates = [float(r["end_rate_cases_per_hour"]) for r in rows]
    time = starts + [ends[-1]]
    rates = start_rates + [end_rates[-1]]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.2, 3.15), sharey=True)
    for start, end, value in zip(starts, ends, start_rates):
        colour = BLUE if value >= 0 else RED
        ax1.add_patch(Rectangle((start, 0), end - start, value, facecolor=colour, alpha=0.24, edgecolor=colour, linewidth=0.7))
    ax1.plot(time, rates, color=NAVY, linewidth=2)
    ax1.axhline(0, color=GREY, linewidth=0.8)
    ax1.set_title("Left rectangles", color=NAVY, weight="bold", fontsize=9)

    for start, end, left, right in zip(starts, ends, start_rates, end_rates):
        colour = TEAL if (left + right) / 2 >= 0 else GOLD
        ax2.add_patch(Polygon([(start, 0), (start, left), (end, right), (end, 0)], closed=True, facecolor=colour, alpha=0.27, edgecolor=colour, linewidth=0.7))
    ax2.plot(time, rates, color=NAVY, linewidth=2)
    ax2.axhline(0, color=GREY, linewidth=0.8)
    ax2.set_title("Trapezoids", color=NAVY, weight="bold", fontsize=9)

    for ax in (ax1, ax2):
        ax.set_xlim(0, 6)
        ax.set_xlabel("Time (hours)")
        ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax1.set_ylabel("Net flow (cases per hour)")
    ax2.annotate("rate crosses zero", (4, 0), xytext=(3.1, -5.2), arrowprops=dict(arrowstyle="->", color=NAVY), color=NAVY, fontsize=7)
    fig.suptitle("Rate × interval width accumulates signed change", color=NAVY, weight="bold", fontsize=11)
    fig.tight_layout()
    save_figure(fig, "fig-10-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
