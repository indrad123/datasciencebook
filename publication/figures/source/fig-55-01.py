"""Figure 55.1: scaled dot-product attention from queries to output."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, y, text, face, width=1.25, height=0.84, fontsize=7):
    patch = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                           boxstyle="round,pad=0.04,rounding_size=0.05",
                           facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY,
            fontsize=fontsize, weight="bold")


def arrow(ax, start, end, color=TEAL):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=11,
                                color=color, linewidth=1.3, shrinkA=3, shrinkB=3))


def main():
    with (ROOT / "data/generated/ch55_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    query_rows = [r for r in rows if r["query_token"] == "tiba"]
    strongest = max(query_rows, key=lambda r: float(r["causal_attention_weight"]))
    out_1 = float(query_rows[0]["causal_output_component_1"])
    out_2 = float(query_rows[0]["causal_output_component_2"])

    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    ax.axis("off")
    xs = [0.70, 2.20, 3.70, 5.20, 6.70]
    labels = [
        "Token vectors\n5 × model width",
        "Learned projections\nQ, K, V",
        "Scaled scores\nQKᵀ / √2",
        "Causal mask\nthen softmax",
        "Weighted values\nattention output",
    ]
    faces = [LIGHT_BLUE, LIGHT_GOLD, LIGHT_BLUE, "#F7DEDC", LIGHT_GOLD]
    for index, (x, label, face) in enumerate(zip(xs, labels, faces)):
        box(ax, x, 2.55, label, face, width=1.24)
        if index:
            arrow(ax, (xs[index - 1] + 0.63, 2.55), (x - 0.63, 2.55), RED if index == 3 else TEAL)

    box(ax, 2.20, 1.10, "Query: what this\nposition needs", LIGHT_BLUE, width=1.42, height=0.72, fontsize=6.7)
    box(ax, 3.85, 1.10, "Keys: source\ncompatibility", LIGHT_BLUE, width=1.42, height=0.72, fontsize=6.7)
    box(ax, 5.50, 1.10, "Values: content\nto be mixed", LIGHT_BLUE, width=1.42, height=0.72, fontsize=6.7)
    arrow(ax, (2.20, 1.48), (2.20, 2.11))
    arrow(ax, (3.85, 1.48), (3.25, 2.11))
    arrow(ax, (5.50, 1.48), (6.15, 2.11))

    ax.text(3.70, 3.35, "Every softmax row is non-negative and sums to 1",
            ha="center", color=NAVY, fontsize=7.4, weight="bold")
    ax.text(3.70, 0.30,
            f"Example query ‘tiba’: strongest permitted source = ‘{strongest['source_token']}’ "
            f"(weight {float(strongest['causal_attention_weight']):.3f}); output = [{out_1:.3f}, {out_2:.3f}]",
            ha="center", color=NAVY, fontsize=7.2)
    ax.set(xlim=(0, 7.4), ylim=(0, 3.75))
    fig.suptitle("Attention converts query–key compatibility into a weighted value mixture",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.025,
             "The mask is part of the information contract: future tokens receive exactly zero weight.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.06, 1, 0.92))
    save_figure(fig, "fig-55-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
