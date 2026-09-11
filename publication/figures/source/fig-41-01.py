"""Figure 41.1: point, contextual, and collective anomalies."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch41_sample.csv").open() as handle:
        rows = [r for r in csv.DictReader(handle) if r["sample_role"] == "monitoring"]
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(7.8, 3.25))

    ordinary = [r for r in rows if r["anomaly_type"] == "ordinary"]
    point = next(r for r in rows if r["anomaly_type"] == "point")
    axes[0].scatter([float(r["fill_weight_g"]) for r in ordinary], [float(r["viscosity_cp"]) for r in ordinary], s=15, color=BLUE, alpha=0.5)
    axes[0].scatter(float(point["fill_weight_g"]), float(point["viscosity_cp"]), s=65, marker="X", color=RED, zorder=4)
    axes[0].annotate("unusual alone", (float(point["fill_weight_g"]), float(point["viscosity_cp"])), xytext=(-58, 16), textcoords="offset points", arrowprops=dict(arrowstyle="->", color=RED), fontsize=7)
    axes[0].set(xlabel="Fill weight (g)", ylabel="Viscosity (cP)", title="Point anomaly")

    contextual = next(r for r in rows if r["anomaly_type"] == "contextual")
    for family, color, shift in (("sauce_a", BLUE, -0.004), ("sauce_b", TEAL, 0.004)):
        subset = [r for r in ordinary if r["product_family"] == family]
        axes[1].scatter([0 if family == "sauce_a" else 1 for _ in subset], [float(r["ph"]) for r in subset], s=15, color=color, alpha=0.48)
    axes[1].scatter(0, float(contextual["ph"]), s=65, marker="X", color=RED, zorder=4)
    axes[1].annotate("plausible globally,\nunusual for sauce A", (0, float(contextual["ph"])), xytext=(8, -8), textcoords="offset points", fontsize=6.8, color=NAVY)
    axes[1].set(xticks=(0, 1), xticklabels=("sauce A", "sauce B"), ylabel="pH", title="Contextual anomaly")

    sequence = [int(r["sequence_index"]) - 300 for r in rows]
    viscosity = [float(r["viscosity_cp"]) for r in rows]
    axes[2].plot(sequence, viscosity, color=BLUE, lw=1.0)
    collective = [r for r in rows if r["anomaly_type"] == "collective"]
    axes[2].scatter([int(r["sequence_index"]) - 300 for r in collective], [float(r["viscosity_cp"]) for r in collective], color=GOLD, s=42, zorder=4)
    axes[2].axvspan(51.5, 54.5, color=GOLD, alpha=0.13)
    axes[2].set(xlabel="Monitoring-batch order", ylabel="Viscosity (cP)", title="Collective anomaly")
    fig.suptitle("Anomaly meaning depends on observation and context", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    save_figure(fig, "fig-41-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
