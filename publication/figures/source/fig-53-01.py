"""Figure 53.1: activation signal through eight hidden layers."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch53_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    layers = [int(row["layer_number"]) for row in rows]
    series = [
        ("Small + tanh", [float(r["small_tanh_activation_variance"]) for r in rows], GOLD, "o"),
        ("Xavier + tanh", [float(r["xavier_tanh_activation_variance"]) for r in rows], BLUE, "s"),
        ("He + ReLU", [float(r["he_relu_activation_variance"]) for r in rows], TEAL, "^"),
    ]

    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    for label, values, color, marker in series:
        ax.plot(layers, values, label=label, color=color, marker=marker,
                linewidth=2, markersize=4.5)
    ax.set_yscale("log")
    ax.set(xlabel="Hidden layer", ylabel="Activation variance (log scale)",
           xticks=layers, title="Initialization must match the activation and network width")
    ax.grid(alpha=0.18, which="both")
    ax.legend(frameon=False, loc="lower left")
    ax.annotate("Signal collapses by about 15 orders of magnitude",
                xy=(8, series[0][1][-1]), xytext=(4.25, 2e-11), color=GOLD,
                arrowprops={"arrowstyle": "->", "color": GOLD}, fontsize=7.4)
    fig.suptitle("Tiny weights can erase the learning signal across deep layers",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.025,
             "Xavier is paired with tanh; He is paired with ReLU. This is a signal diagnostic, not a performance ranking.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93))
    save_figure(fig, "fig-53-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
