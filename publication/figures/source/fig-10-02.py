"""Figure 10.2: rate and cumulative inventory change."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, RED, TEAL, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch10_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    time = [0.0] + [float(r["interval_end_hour"]) for r in rows]
    rate = [12.0] + [float(r["end_rate_cases_per_hour"]) for r in rows]
    exact = [0.0] + [float(r["exact_net_change_cases"]) for r in rows]
    trap = [0.0] + [float(r["cumulative_trapezoid_cases"]) for r in rows]
    absolute = [0.0] + [float(r["exact_absolute_movement_cases"]) for r in rows]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.2, 3.15))
    ax1.plot(time, rate, color=BLUE, linewidth=2)
    ax1.fill_between(time, rate, 0, where=[v >= 0 for v in rate], color=TEAL, alpha=0.25, interpolate=True, label="inbound contribution")
    ax1.fill_between(time, rate, 0, where=[v <= 0 for v in rate], color=RED, alpha=0.20, interpolate=True, label="outbound contribution")
    ax1.axhline(0, color=GREY, linewidth=0.8)
    ax1.set_title("Net flow rate", color=NAVY, weight="bold", fontsize=9)
    ax1.set_xlabel("Time (hours)")
    ax1.set_ylabel("Cases per hour")
    ax1.legend(frameon=False, fontsize=6.5)

    ax2.plot(time, exact, color=BLUE, linewidth=2, label="exact net change")
    ax2.plot(time, trap, color=GOLD, linestyle="--", linewidth=1.4, label="cumulative trapezoids")
    ax2.plot(time, absolute, color=TEAL, linestyle=":", linewidth=2, label="total movement")
    ax2.scatter([4, 6], [24, 18], color=[NAVY, RED], s=28, zorder=4)
    ax2.annotate("peak: 24 cases", (4, 24), xytext=(1.8, 27), arrowprops=dict(arrowstyle="->", color=NAVY), color=NAVY, fontsize=7)
    ax2.set_title("Accumulated quantities", color=NAVY, weight="bold", fontsize=9)
    ax2.set_xlabel("Time (hours)")
    ax2.set_ylabel("Cases")
    ax2.legend(frameon=False, fontsize=6.5)

    for ax in (ax1, ax2):
        ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
        ax.set_xlim(0, 6)
    fig.suptitle("Integration turns a rate into a cumulative trajectory", color=NAVY, weight="bold", fontsize=11)
    fig.tight_layout()
    save_figure(fig, "fig-10-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
