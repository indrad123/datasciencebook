"""Figure 8.2: two production equations and their intersection."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch08_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    solution_x = int(rows[0]["coffee_batches_solution"])
    solution_y = int(rows[0]["tea_batches_solution"])
    xs = list(range(0, 91))
    ingredient_a = [100 - 2 * x for x in xs]
    ingredient_b = [(90 - x) / 3 for x in xs]

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.plot(xs, ingredient_a, color=BLUE, linewidth=1.8, label="Ingredient A: 2x + y = 100")
    ax.plot(xs, ingredient_b, color=GOLD, linewidth=1.8, label="Ingredient B: x + 3y = 90")
    ax.scatter([solution_x], [solution_y], color=NAVY, edgecolor="white", linewidth=0.8, s=75, zorder=5)
    ax.axvline(solution_x, ymin=0, ymax=solution_y / 55, color=GREY, linestyle="--", linewidth=1)
    ax.axhline(solution_y, xmin=0, xmax=solution_x / 55, color=GREY, linestyle="--", linewidth=1)
    ax.annotate("Unique solution\n(42 coffee, 16 tea)", (solution_x, solution_y), xytext=(-92, 22), textcoords="offset points", arrowprops=dict(arrowstyle="->", color=NAVY), color=NAVY, weight="bold")
    ax.set_xlim(0, 55)
    ax.set_ylim(0, 55)
    ax.set_xlabel("Coffee-blend production, x (batches)")
    ax.set_ylabel("Tea-blend production, y (batches)")
    ax.set_title("The intersection satisfies both resource equations", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    save_figure(fig, "fig-08-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
