"""Figure 9.1: secant slopes approach the tangent slope."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, RED, TEAL, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch09_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    x = [float(r["x"]) for r in rows]

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    ax.plot(x, [float(r["square_value"]) for r in rows], color=NAVY, linewidth=2, label="f(x) = x²")
    for key, colour, label in (
        ("secant_h_1_0_at_x3", RED, "secant h = 1.0, slope 7.0"),
        ("secant_h_0_5_at_x3", GOLD, "secant h = 0.5, slope 6.5"),
        ("secant_h_0_1_at_x3", TEAL, "secant h = 0.1, slope 6.1"),
    ):
        ax.plot(x, [float(r[key]) for r in rows], color=colour, linestyle="--", linewidth=1.2, label=label)
    ax.plot(x, [float(r["tangent_at_x3"]) for r in rows], color=BLUE, linewidth=1.8, label="tangent at x = 3, slope 6.0")
    ax.scatter([3], [9], color=NAVY, edgecolor="white", linewidth=0.7, s=65, zorder=5)
    ax.annotate("Anchor point (3, 9)", (3, 9), xytext=(-78, -28), textcoords="offset points", arrowprops=dict(arrowstyle="->", color=NAVY), color=NAVY)
    ax.set_xlim(1.5, 4.5)
    ax.set_ylim(0, 22)
    ax.set_xlabel("Input x")
    ax.set_ylabel("Function value f(x)")
    ax.set_title("Shrinking secant intervals approach the tangent", color=NAVY, weight="bold")
    ax.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, loc="upper left", fontsize=6.8)
    fig.tight_layout()
    save_figure(fig, "fig-09-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
