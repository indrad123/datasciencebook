"""Figure 4.1: input-output coordinates for a linear freight function."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch04_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    q = [int(row["quantity_cases"]) for row in rows]
    costs = [int(row["plan_a_cost_idr"]) / 1000 for row in rows]

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.plot(q, costs, color=BLUE, marker="o", linewidth=1.5, label="C(q) = 300,000 + 4,000q")
    ax.scatter([0], [300], s=65, color=GOLD, edgecolor=NAVY, zorder=4)
    ax.annotate("Intercept: IDR 300,000\n(cost when q = 0)", (0, 300), xytext=(28, -4), textcoords="offset points", color=NAVY)
    ax.annotate("Input q = 100\nOutput C(q) = IDR 700,000", (100, 700), xytext=(-42, 24), textcoords="offset points", color=NAVY, weight="bold")
    ax.set_xlabel("Shipment quantity, q (cases)")
    ax.set_ylabel("Freight cost, C(q) (thousand IDR)")
    ax.set_title("A function maps each permitted input to one output", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(["C(q) = 300,000 + 4,000q"], frameon=False, loc="lower right")
    fig.tight_layout()
    save_figure(fig, "fig-04-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
