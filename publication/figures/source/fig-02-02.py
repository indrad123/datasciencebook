"""Figure 2.2: absolute totals and relative acceptance rates."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch02_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["example_id"].startswith("LINE-")]
    labels = [row["example_id"].replace("LINE-", "Line ") for row in rows]
    accepted = [int(row["first_value"]) for row in rows]
    rates = [100 * int(row["first_value"]) / int(row["second_value"]) for row in rows]

    fig, axes = plt.subplots(1, 2, figsize=(5.2, 3.0))
    axes[0].bar(labels, accepted, color=[BLUE, GOLD], edgecolor=NAVY, linewidth=0.7)
    axes[0].set_ylabel("Acceptable packs")
    axes[0].set_title("Absolute total")
    axes[0].set_ylim(0, 1600)
    axes[1].bar(labels, rates, color=[BLUE, GOLD], edgecolor=NAVY, linewidth=0.7)
    axes[1].set_ylabel("Acceptance rate (%)")
    axes[1].set_title("Relative result")
    axes[1].set_ylim(90, 100)
    for ax, values, fmt in ((axes[0], accepted, "{:.0f}"), (axes[1], rates, "{:.1f}%")):
        ax.grid(axis="y", color=GREY, alpha=0.18, linewidth=0.7)
        for index, value in enumerate(values):
            ax.text(index, value + (35 if ax is axes[0] else 0.2), fmt.format(value), ha="center", color=NAVY, weight="bold")
    fig.suptitle("Totals and percentages answer different questions", color=NAVY, weight="bold")
    fig.tight_layout()
    save_figure(fig, "fig-02-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
