"""Figure 7.1: components, magnitude, direction, and unit vector."""

from pathlib import Path
import csv
import math
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch07_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["example_id"] == "magnitude_unit_vector"]
    x, y = (int(r["vector_a_value"]) for r in rows)
    magnitude = math.hypot(x, y)

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.annotate("", xy=(x, y), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2, mutation_scale=16))
    ax.plot([0, x], [0, 0], color=GOLD, linestyle="--", linewidth=1.4)
    ax.plot([x, x], [0, y], color=GOLD, linestyle="--", linewidth=1.4)
    ax.text(x / 2, -0.42, "horizontal component = 3", ha="center", color=NAVY)
    ax.text(x + 0.18, y / 2, "vertical\ncomponent = 4", va="center", color=NAVY)
    ax.text(1.05, 2.55, r"magnitude $=\sqrt{3^2+4^2}=5$", color=NAVY, weight="bold")
    ax.text(0.35, 4.35, r"unit direction $=(3/5,4/5)=(0.6,0.8)$", color=BLUE)
    ax.scatter([0, x], [0, y], color=[NAVY, GOLD], s=45, zorder=4)
    ax.set_xlim(-0.5, 5.2)
    ax.set_ylim(-0.8, 5.2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("First component")
    ax.set_ylabel("Second component")
    ax.set_title("Components determine a vector's magnitude and direction", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    fig.tight_layout()
    save_figure(fig, "fig-07-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
