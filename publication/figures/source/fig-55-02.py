"""Figure 55.2: unmasked and causal attention with position encodings."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, TEAL, apply_style, save_figure

TOKENS = ["stok", "kopi", "belum", "tiba", "jakarta"]


def annotate(ax, matrix):
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            value = matrix[row, column]
            ax.text(column, row, f"{value:.2f}", ha="center", va="center",
                    fontsize=6.1, color="white" if value > 0.38 else NAVY)


def main():
    with (ROOT / "data/generated/ch55_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    unmasked = np.array([float(r["unmasked_attention_weight"]) for r in rows]).reshape(5, 5)
    causal = np.array([float(r["causal_attention_weight"]) for r in rows]).reshape(5, 5)
    source_zero = [r for r in rows if r["query_position"] == "0"]
    positions = np.array([[float(r[f"position_{kind}_{pair}"]) for pair in range(1, 4) for kind in ("sin", "cos")]
                          for r in source_zero])

    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 4.2), gridspec_kw={"width_ratios": [1, 1, 1.18]})
    for ax, matrix, title in [(axes[0], unmasked, "Unmasked self-attention"),
                              (axes[1], causal, "Causal self-attention")]:
        ax.imshow(matrix, cmap="Blues", vmin=0, vmax=1)
        annotate(ax, matrix)
        ax.set(xticks=range(5), yticks=range(5), xticklabels=TOKENS,
               yticklabels=TOKENS, xlabel="Source token", ylabel="Query token", title=title)
        ax.tick_params(axis="x", rotation=45)
    colors = [BLUE, BLUE, TEAL, TEAL, GOLD, GOLD]
    styles = ["-", "--"] * 3
    for component in range(6):
        axes[2].plot(range(5), positions[:, component], color=colors[component],
                     linestyle=styles[component], marker="o", markersize=3,
                     label=f"component {component + 1}")
    axes[2].set(xticks=range(5), xticklabels=TOKENS, xlabel="Token position",
                ylabel="Encoding value", title="Six-dimensional positions")
    axes[2].tick_params(axis="x", rotation=45)
    axes[2].axhline(0, color=NAVY, linewidth=0.7, alpha=0.4)
    axes[2].legend(frameon=False, fontsize=6.1, ncol=2, loc="lower left")

    fig.suptitle("Masks enforce information boundaries; position encodings restore order",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.02,
             "Each attention row still sums to 1 after masking; blocked future mass is exactly zero.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.07, 1, 0.92), w_pad=1.4)
    save_figure(fig, "fig-55-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
