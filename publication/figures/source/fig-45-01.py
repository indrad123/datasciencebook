"""Figure 45.1: risk-set timelines with events, censoring, and delayed entry."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, GREY, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch45_sample.csv").open(encoding="utf-8") as handle:
        all_rows = list(csv.DictReader(handle))
    chosen_ids = ("D45-001", "D45-006", "D45-012", "D45-037", "D45-042", "D45-048")
    rows = [next(r for r in all_rows if r["distributor_id"] == key) for key in chosen_ids]

    apply_style()
    fig, ax = plt.subplots(figsize=(7.4, 3.8))
    y_positions = list(range(len(rows), 0, -1))
    for y, row in zip(y_positions, rows):
        entry = float(row["entry_month"])
        end = float(row["exit_month"])
        ax.hlines(y, entry, end, color=BLUE, linewidth=3)
        ax.scatter(entry, y, marker=">", s=55, color=TEAL, zorder=3)
        if row["event_observed"] == "1":
            ax.scatter(end, y, marker="X", s=65, color=RED, zorder=3)
        else:
            ax.scatter(end, y, marker="|", s=130, linewidth=2.4, color=GOLD, zorder=3)
    ax.axvline(12, color=GREY, linestyle="--", linewidth=1)
    ax.text(12.25, 6.32, "decision horizon", color=GREY, fontsize=7)
    ax.scatter([], [], marker=">", s=55, color=TEAL, label="enters risk set")
    ax.scatter([], [], marker="X", s=65, color=RED, label="observed churn")
    ax.scatter([], [], marker="|", s=130, linewidth=2.4, color=GOLD, label="right censored")
    ax.set(
        xlabel="Months from common cohort origin",
        ylabel="Distributor record",
        yticks=y_positions,
        yticklabels=chosen_ids,
        xlim=(-0.8, max(float(r["exit_month"]) for r in rows) + 2),
        ylim=(0.4, 6.7),
    )
    ax.legend(frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, -0.33))
    ax.set_title("Risk sets change through entry, events, and censoring", color=NAVY, weight="bold")
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    save_figure(fig, "fig-45-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
