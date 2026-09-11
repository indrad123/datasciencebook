"""Figure 54.1: one local patch, one shared kernel, and one response."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import GOLD, NAVY, apply_style, save_figure


def annotate_grid(ax, values, fmt=".1f", color_threshold=None):
    for row in range(values.shape[0]):
        for column in range(values.shape[1]):
            color = "white" if color_threshold is not None and values[row, column] > color_threshold else NAVY
            ax.text(column, row, format(values[row, column], fmt), ha="center", va="center",
                    fontsize=7.2, color=color, weight="bold")


def main():
    with (ROOT / "data/generated/ch54_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    image = np.array([float(r["input_intensity"]) for r in rows]).reshape(12, 12)
    response = np.array([float(r["vertical_edge_response"]) for r in rows]).reshape(12, 12)
    padded = np.pad(image, 1)
    output_row, output_column = 4, 3
    patch = padded[output_row:output_row + 3, output_column:output_column + 3]
    kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    product = patch * kernel

    apply_style()
    fig, axes = plt.subplots(1, 4, figsize=(7.6, 3.6), gridspec_kw={"width_ratios": [1.4, 1, 1, 1]})
    axes[0].imshow(image, cmap="Blues", vmin=0, vmax=1)
    axes[0].add_patch(Rectangle((1.5, 2.5), 3, 3, fill=False, edgecolor=GOLD, linewidth=2.2))
    axes[0].set(title="Synthetic package image", xticks=[], yticks=[])
    axes[0].text(0.5, -0.10, "Highlighted padded patch", transform=axes[0].transAxes,
                 ha="center", color=NAVY, fontsize=7)

    panels = [(patch, "Local 3 × 3 patch", "Blues"), (kernel, "Shared edge kernel", "coolwarm"),
              (product, "Elementwise products", "coolwarm")]
    for ax, (values, title, cmap) in zip(axes[1:], panels):
        limit = max(1.0, float(np.max(np.abs(values))))
        ax.imshow(values, cmap=cmap, vmin=-limit if cmap == "coolwarm" else 0, vmax=limit)
        annotate_grid(ax, values)
        ax.set(title=title, xticks=[], yticks=[])
    axes[1].text(-0.16, 0.5, "×", transform=axes[1].transAxes, ha="center", va="center",
                 fontsize=18, color=NAVY)
    axes[2].text(-0.16, 0.5, "=", transform=axes[2].transAxes, ha="center", va="center",
                 fontsize=18, color=NAVY)
    axes[3].text(0.5, -0.10, f"Sum = {product.sum():.1f} = feature[{output_row}, {output_column}]",
                 transform=axes[3].transAxes, ha="center", color=NAVY, fontsize=7)
    assert np.isclose(product.sum(), response[output_row, output_column])

    fig.suptitle("A shared kernel turns each local image patch into one feature response",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.02,
             "The framework operation shown is cross-correlation: the learned kernel is not flipped.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.06, 1, 0.91), w_pad=1.5)
    save_figure(fig, "fig-54-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
