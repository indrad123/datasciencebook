"""Figure 5.1: linear versus exponential demand growth."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch05_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    years = [int(row["year"]) for row in rows]
    linear = [int(row["linear_demand_cases"]) for row in rows]
    exponential = [float(row["exponential_demand_cases"]) for row in rows]

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.plot(years, linear, color=BLUE, marker="o", linewidth=1.5, label="Linear: add 800 cases")
    ax.plot(years, exponential, color=GOLD, marker="s", linewidth=1.5, label="Exponential: grow by 8%")
    ax.scatter([1], [10_800], color=NAVY, s=45, zorder=4)
    ax.annotate("Both equal 10,800\nafter one year", (1, 10_800), xytext=(30, 20), textcoords="offset points", color=NAVY)
    ax.annotate("Percentage growth acts\non a changing base", (8, exponential[8]), xytext=(-78, 14), textcoords="offset points", color=NAVY)
    ax.set_xlabel("Planning time (years)")
    ax.set_ylabel("Expected demand (cases)")
    ax.set_title("Equal first-year change, different long-term paths", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save_figure(fig, "fig-05-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
