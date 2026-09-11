"""Figure 9.2: derivative as a changing slope."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, TEAL, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch09_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    x = [float(r["x"]) for r in rows]
    f = [float(r["square_value"]) for r in rows]
    exact = [float(r["exact_derivative"]) for r in rows]
    forward = [float(r["forward_difference_h_0_1"]) for r in rows]
    central = [float(r["central_difference_h_0_1"]) for r in rows]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.2, 3.15))
    ax1.plot(x, f, color=NAVY, linewidth=2)
    for point in (1, 3, 5):
        value = point**2
        slope = 2 * point
        dx = 0.45
        ax1.plot([point - dx, point + dx], [value - slope * dx, value + slope * dx], color=GOLD, linewidth=1.5)
        ax1.scatter([point], [value], color=BLUE, s=30, zorder=4)
        ax1.text(point - 0.35, value + 1.5, f"slope {slope}", color=NAVY, fontsize=7)
    ax1.set_title("Tangent slope changes with x", color=NAVY, weight="bold", fontsize=9)
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x) = x²")
    ax1.grid(color=GREY, alpha=0.18, linewidth=0.7)

    ax2.plot(x, exact, color=BLUE, linewidth=2, label="exact: 2x")
    ax2.plot(x, forward, color=GOLD, linestyle="--", linewidth=1.4, label="forward, h = 0.1")
    ax2.plot(x, central, color=TEAL, linestyle=":", linewidth=1.8, label="central, h = 0.1")
    ax2.set_title("Derivative and finite differences", color=NAVY, weight="bold", fontsize=9)
    ax2.set_xlabel("x")
    ax2.set_ylabel("Rate of change")
    ax2.grid(color=GREY, alpha=0.18, linewidth=0.7)
    ax2.legend(frameon=False, fontsize=6.8)
    fig.suptitle("The derivative records the local slope at each input", color=NAVY, weight="bold", fontsize=11)
    fig.tight_layout()
    save_figure(fig, "fig-09-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
