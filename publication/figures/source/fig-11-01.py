"""Figure 11.1: two-parameter loss surface and gradient path."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch11_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["scenario"] == "two_parameter"]
    path_x = np.array([float(r["parameter_x"]) for r in rows])
    path_y = np.array([float(r["parameter_y"]) for r in rows])
    x = np.linspace(-4, 5, 240); y = np.linspace(-4, 5, 240)
    xx, yy = np.meshgrid(x, y); loss = (xx - 2) ** 2 + (yy + 1) ** 2

    fig, ax = plt.subplots(figsize=(5.2, 3.15))
    contour = ax.contourf(xx, yy, loss, levels=[0, 1, 4, 9, 16, 25, 50, 80], cmap="Blues", alpha=0.8)
    ax.contour(xx, yy, loss, levels=[1, 4, 9, 16, 25, 50], colors=NAVY, linewidths=0.5, alpha=0.45)
    ax.plot(path_x, path_y, color=GOLD, linewidth=1.8, marker="o", markersize=3, label="gradient-descent path")
    ax.scatter([-3], [4], color=RED, s=45, zorder=5, label="start (-3, 4)")
    ax.scatter([2], [-1], color=NAVY, marker="*", s=90, zorder=5, label="minimum (2, -1)")
    ax.annotate("updates follow -gradient", (path_x[2], path_y[2]), xytext=(-2.2, -2.7), arrowprops=dict(arrowstyle="->", color=NAVY), color=NAVY, fontsize=7)
    ax.set_xlabel("Parameter x"); ax.set_ylabel("Parameter y")
    ax.set_title("Local gradients guide the path down the loss surface", color=NAVY, weight="bold")
    ax.legend(frameon=False, fontsize=6.8, loc="upper right")
    fig.colorbar(contour, ax=ax, label="Loss", fraction=0.046, pad=0.04)
    fig.tight_layout(); save_figure(fig, "fig-11-01", ROOT); plt.close(fig)


if __name__ == "__main__": main()
