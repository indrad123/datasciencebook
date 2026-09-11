"""Figure 54.2: feature response, pooling, and receptive-field growth."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, TEAL, apply_style, save_figure


def box(ax, x, y, text, face):
    patch = FancyBboxPatch((x - 0.78, y - 0.34), 1.56, 0.68,
                           boxstyle="round,pad=0.04,rounding_size=0.05",
                           facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY, fontsize=7, weight="bold")


def main():
    with (ROOT / "data/generated/ch54_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    image = np.array([float(r["input_intensity"]) for r in rows]).reshape(12, 12)
    feature = np.array([float(r["vertical_edge_response"]) for r in rows]).reshape(12, 12)
    pooled = np.zeros((6, 6))
    for row in rows:
        pooled[int(row["pool_row"]), int(row["pool_column"])] = float(row["pooled_max_absolute_response"])

    apply_style()
    fig = plt.figure(figsize=(7.6, 4.8))
    grid = fig.add_gridspec(2, 3, height_ratios=[1.1, 0.9])
    axes = [fig.add_subplot(grid[0, i]) for i in range(3)]
    for ax, values, title, cmap, low, high in [
        (axes[0], image, "Input: 12 × 12", "Blues", 0, 1),
        (axes[1], feature, "Vertical-edge map: 12 × 12", "coolwarm", -3, 3),
        (axes[2], pooled, "2 × 2 max pool: 6 × 6", "YlOrBr", 0, 3),
    ]:
        ax.imshow(values, cmap=cmap, vmin=low, vmax=high)
        ax.set(title=title, xticks=[], yticks=[])
    axes[1].text(0.5, -0.12, "Sign marks edge direction", transform=axes[1].transAxes,
                 ha="center", color=NAVY, fontsize=6.8)
    axes[2].text(0.5, -0.12, "Magnitude retained; position coarsened", transform=axes[2].transAxes,
                 ha="center", color=NAVY, fontsize=6.8)

    flow = fig.add_subplot(grid[1, :])
    flow.axis("off")
    xs = [0.8, 2.7, 4.6, 6.5]
    labels = ["Input activation\nRF = 1, jump = 1", "Conv 3, stride 1\nRF = 3, jump = 1",
              "Pool 2, stride 2\nRF = 4, jump = 2", "Conv 3, stride 1\nRF = 8, jump = 2"]
    for index, (x, label) in enumerate(zip(xs, labels)):
        box(flow, x, 0.62, label, LIGHT_BLUE if index % 2 == 0 else LIGHT_GOLD)
        if index:
            flow.add_patch(FancyArrowPatch((xs[index - 1] + 0.80, 0.62), (x - 0.80, 0.62),
                                           arrowstyle="-|>", mutation_scale=11, color=TEAL, linewidth=1.3))
    flow.set(xlim=(0, 7.3), ylim=(0, 1.2))
    flow.text(3.65, 0.05,
              "Pooling halves spatial dimensions, while stacked operations expand the input region seen by one activation.",
              ha="center", color=NAVY, fontsize=7.2)

    fig.suptitle("Convolution finds local changes; pooling compresses them; depth expands context",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.02, 1, 0.92), h_pad=1.2)
    save_figure(fig, "fig-54-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
