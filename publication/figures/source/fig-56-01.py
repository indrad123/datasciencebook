"""Figure 56.1: encoder, latent representation, and decoder."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def box(ax, x, y, text, face, width=1.45):
    patch = FancyBboxPatch((x - width / 2, y - 0.34), width, 0.68,
                           boxstyle="round,pad=0.04,rounding_size=0.05",
                           facecolor=face, edgecolor=NAVY, linewidth=1)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", color=NAVY, fontsize=7, weight="bold")


def main():
    with (ROOT / "data/generated/ch56_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    routine = rows[:-1]
    unusual = rows[-1]
    z = np.array([[float(r["latent_1"]), float(r["latent_2"])] for r in routine])
    errors = np.array([float(r["reconstruction_mse"]) for r in routine])
    unusual_z = [float(unusual["latent_1"]), float(unusual["latent_2"])]

    apply_style()
    fig = plt.figure(figsize=(7.6, 4.8))
    grid = fig.add_gridspec(2, 1, height_ratios=[0.72, 1.28])
    flow = fig.add_subplot(grid[0])
    flow.axis("off")
    xs = [0.8, 2.55, 4.3, 6.05]
    labels = ["Package signals\nx ∈ ℝ³", "Encoder\nz = f(x)", "Bottleneck\nz ∈ ℝ²", "Decoder\nx̂ = g(z)"]
    faces = [LIGHT_BLUE, LIGHT_GOLD, LIGHT_BLUE, LIGHT_GOLD]
    for i, (x, label, face) in enumerate(zip(xs, labels, faces)):
        box(flow, x, 0.62, label, face)
        if i:
            flow.add_patch(FancyArrowPatch((xs[i - 1] + 0.73, 0.62), (x - 0.73, 0.62),
                                           arrowstyle="-|>", mutation_scale=11, color=TEAL, linewidth=1.3))
    flow.text(6.95, 0.62, "compare\nx and x̂", ha="center", va="center", color=RED, fontsize=7, weight="bold")
    flow.add_patch(FancyArrowPatch((6.78, 0.37), (0.98, 0.20), connectionstyle="arc3,rad=-0.08",
                                   arrowstyle="-|>", mutation_scale=10, color=RED, linewidth=1.1))
    flow.set(xlim=(0, 7.4), ylim=(0.05, 1.15))

    ax = fig.add_subplot(grid[1])
    scatter = ax.scatter(z[:, 0], z[:, 1], c=errors, cmap="viridis", s=28,
                         edgecolor="white", linewidth=0.4, label="routine packages")
    ax.scatter(*unusual_z, marker="*", s=150, color=RED, edgecolor=NAVY,
               linewidth=0.7, label="unusual package scored after fit", zorder=4)
    path = np.linspace(z[0], z[1], 5)
    ax.plot(path[:, 0], path[:, 1], color=GOLD, marker="o", markersize=3,
            linewidth=1.4, label="five-step latent interpolation")
    ax.set(xlabel="Latent coordinate 1", ylabel="Latent coordinate 2",
           title="The bottleneck preserves a two-dimensional subspace")
    ax.legend(frameon=False, fontsize=6.8, loc="best")
    colorbar = fig.colorbar(scatter, ax=ax, fraction=0.03, pad=0.02)
    colorbar.set_label("Routine reconstruction MSE", fontsize=7)
    ax.grid(alpha=0.15)
    fig.suptitle("An autoencoder compresses observations and reconstructs them through a bottleneck",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.018,
             "Latent interpolation is a mathematical path; decoded points still require physical and domain validation.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.05, 1, 0.92), h_pad=0.6)
    save_figure(fig, "fig-56-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
