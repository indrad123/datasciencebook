"""Figure 4.2: fixed charge, slope, and break-even comparison."""

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
    plan_a = [int(row["plan_a_cost_idr"]) / 1000 for row in rows]
    plan_b = [int(row["plan_b_cost_idr"]) / 1000 for row in rows]
    cross = next((x, a) for x, a, b in zip(q, plan_a, plan_b) if a == b)

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.plot(q, plan_a, color=BLUE, marker="o", linewidth=1.5, label="Plan A: 300,000 + 4,000q")
    ax.plot(q, plan_b, color=GOLD, marker="s", linewidth=1.5, linestyle="--", label="Plan B: 180,000 + 6,000q")
    ax.scatter(*cross, s=70, color="white", edgecolor=NAVY, linewidth=1.5, zorder=5)
    ax.annotate("Break-even\n60 cases, IDR 540,000", cross, xytext=(12, 20), textcoords="offset points", color=NAVY, weight="bold")
    ax.text(4, 330, "Higher intercept", color=BLUE, fontsize=8)
    ax.text(108, 850, "Steeper slope", color=GOLD, fontsize=8, weight="bold")
    ax.set_xlabel("Shipment quantity (cases)")
    ax.set_ylabel("Freight cost (thousand IDR)")
    ax.set_title("Intercept sets the start; slope sets the rate of change", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save_figure(fig, "fig-04-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
