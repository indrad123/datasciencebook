"""Figure 11.2: learning-rate effects on convergence."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main() -> None:
    apply_style()
    with (ROOT / "data/generated/ch11_sample.csv").open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["scenario"] == "one_parameter"]
    colours = {0.05: BLUE, 0.10: TEAL, 0.60: GOLD, 1.10: RED}
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.2, 3.15))
    for lr, colour in colours.items():
        subset = [r for r in rows if abs(float(r["learning_rate"]) - lr) < 1e-9]
        iterations = [int(r["iteration"]) for r in subset]
        parameters = [float(r["parameter_x"]) for r in subset]
        losses = [float(r["loss"]) for r in subset]
        label = f"learning rate {lr:.2f}"
        ax1.plot(iterations, parameters, color=colour, linewidth=1.7, label=label)
        ax2.semilogy(iterations, losses, color=colour, linewidth=1.7, label=label)
    ax1.axhline(4, color=NAVY, linestyle=":", linewidth=1, label="optimum w = 4")
    ax1.set_title("Parameter path", color=NAVY, weight="bold", fontsize=9)
    ax1.set_xlabel("Iteration"); ax1.set_ylabel("Parameter w"); ax1.set_ylim(-20, 12)
    ax2.axhline(2, color=NAVY, linestyle=":", linewidth=1, label="minimum loss = 2")
    ax2.set_title("Objective history", color=NAVY, weight="bold", fontsize=9)
    ax2.set_xlabel("Iteration"); ax2.set_ylabel("Loss (log scale)")
    for ax in (ax1, ax2): ax.grid(alpha=0.18); ax.legend(frameon=False, fontsize=5.8)
    fig.suptitle("Learning rate controls speed, oscillation, and divergence", color=NAVY, weight="bold", fontsize=11)
    fig.tight_layout(); save_figure(fig, "fig-11-02", ROOT); plt.close(fig)


if __name__ == "__main__": main()
