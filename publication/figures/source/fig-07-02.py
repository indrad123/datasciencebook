"""Figure 7.2: Euclidean, Manhattan, and cosine geometry."""

from pathlib import Path
import csv
import math
import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Arc

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, RED, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch07_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["example_id"] == "warehouse_profiles"][:2]
    a = tuple(int(r["vector_a_value"]) for r in rows)
    b = tuple(int(r["vector_b_value"]) for r in rows)
    euclidean = math.dist(a, b)
    manhattan = sum(abs(x - y) for x, y in zip(a, b))
    cosine = sum(x * y for x, y in zip(a, b)) / (math.hypot(*a) * math.hypot(*b))
    angle_a = math.degrees(math.atan2(a[1], a[0]))
    angle_b = math.degrees(math.atan2(b[1], b[0]))

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.annotate("A: coffee 4, tea 3", xy=a, xytext=(3.2, 4.55), arrowprops=dict(arrowstyle="->", color=BLUE), color=NAVY, weight="bold")
    ax.annotate("B: coffee 2, tea 4", xy=b, xytext=(0.45, 4.7), arrowprops=dict(arrowstyle="->", color=GOLD), color=NAVY, weight="bold")
    ax.plot([a[0], b[0]], [a[1], b[1]], color=RED, linewidth=2, label=f"Euclidean = √5 ≈ {euclidean:.2f}")
    ax.plot([a[0], b[0], b[0]], [a[1], a[1], b[1]], color=NAVY, linestyle="--", linewidth=1.6, label=f"Manhattan = {manhattan:.0f}")
    ax.annotate("", xy=a, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.8, mutation_scale=13))
    ax.annotate("", xy=b, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.8, mutation_scale=13))
    start, end = sorted((angle_a, angle_b))
    ax.add_patch(Arc((0, 0), 2.2, 2.2, theta1=start, theta2=end, color=GREY, linewidth=1.4))
    ax.text(0.9, 0.92, f"cosine similarity\n= {cosine:.3f}", color=NAVY)
    ax.scatter([a[0], b[0]], [a[1], b[1]], color=[BLUE, GOLD], s=55, zorder=4)
    ax.set_xlim(-0.2, 5.2)
    ax.set_ylim(-0.2, 5.4)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("Coffee demand (hundreds of cases)")
    ax.set_ylabel("Tea demand (hundreds of cases)")
    ax.set_title("Distance measures separation; cosine measures direction", color=NAVY, weight="bold", pad=25)
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, loc="lower right")
    ax.text(0.5, 1.01, "Coffee-and-tea projection; full vectors also include noodles", transform=ax.transAxes, ha="center", color=GREY, fontsize=7.2)
    fig.tight_layout()
    save_figure(fig, "fig-07-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
