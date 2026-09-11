"""Figure 8.1: rows, columns, and matrix-vector multiplication."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def panel(ax, x, y, w, h, face, text, fontsize=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04", facecolor=face, edgecolor=NAVY, linewidth=1))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=NAVY, fontsize=fontsize)


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch08_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    a = [[int(r["coffee_units_per_batch"]), int(r["tea_units_per_batch"])] for r in rows]
    x = [int(rows[0]["coffee_batches_solution"]), int(rows[0]["tea_batches_solution"])]
    b = [int(r["available_units"]) for r in rows]

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")
    panel(ax, 0.45, 2.15, 3.2, 2.45, LIGHT_BLUE, f"A: coefficients (2 × 2)\ncolumns: coffee | tea\n\nIngredient A   [ {a[0][0]}   {a[0][1]} ]\nIngredient B   [ {a[1][0]}   {a[1][1]} ]", 8.3)
    panel(ax, 4.45, 2.15, 2.15, 2.45, LIGHT_GOLD, f"x: batches (2 × 1)\n\ncoffee   [ {x[0]} ]\ntea         [ {x[1]} ]", 8.3)
    panel(ax, 7.55, 2.15, 3.1, 2.45, LIGHT_BLUE, f"b: available (2 × 1)\n\nIngredient A   [ {b[0]} ]\nIngredient B   [  {b[1]} ]", 8.3)
    ax.text(4.02, 3.36, "×", fontsize=22, color=GOLD, ha="center", va="center", weight="bold")
    ax.text(7.08, 3.36, "=", fontsize=22, color=GOLD, ha="center", va="center", weight="bold")
    ax.text(6, 1.38, "(2 × 2)(2 × 1) → (2 × 1): inside dimensions match", ha="center", color=BLUE, weight="bold")
    ax.text(6, 0.62, "Row 1: 2(42) + 1(16) = 100   |   Row 2: 1(42) + 3(16) = 90", ha="center", color=NAVY, weight="bold")
    ax.set_title("Matrix rows combine product quantities into resource usage", color=NAVY, weight="bold", pad=8)
    fig.tight_layout()
    save_figure(fig, "fig-08-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
