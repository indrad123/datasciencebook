"""Figure 3.2: a shipment equation under changing inputs."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch03_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    x = [int(row["cartons_per_pallet"]) for row in rows]
    totals = [int(row["shipment_total_cartons"]) for row in rows]
    solution = next((a, b) for a, b in zip(x, totals) if b == 1200)

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.plot(x, totals, color=BLUE, marker="o", linewidth=1.5, label="Shipment total: 18x + 120")
    ax.axhline(1200, color=GOLD, linestyle="--", linewidth=1.4, label="Required total: 1,200")
    ax.axvline(solution[0], color=NAVY, linestyle=":", linewidth=1.2)
    ax.scatter(*solution, s=65, color=GOLD, edgecolor=NAVY, zorder=4)
    ax.annotate("x = 60", solution, xytext=(8, -28), textcoords="offset points", color=NAVY, weight="bold")
    ax.set_xlabel("Cartons per pallet (x)")
    ax.set_ylabel("Total shipment cartons")
    ax.set_title("Changing x changes the shipment total predictably", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save_figure(fig, "fig-03-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
