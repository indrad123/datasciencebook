"""Figure 52.2: learning-rate and gradient-norm diagnostics."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch52_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    groups = {}
    for row in rows:
        groups.setdefault(row["run_id"], []).append(row)
    colors = {"xor-slow": GOLD, "xor-moderate": BLUE, "xor-fast": TEAL}

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.3))
    for run_id, values in groups.items():
        epoch = [int(r["epoch"]) for r in values]
        loss = [float(r["loss_before_update"]) for r in values]
        norm = [float(r["total_gradient_norm"]) for r in values]
        rate = values[0]["learning_rate"]
        label = f"learning rate {rate}"
        axes[0].plot(epoch, loss, color=colors[run_id], linewidth=1.8, label=label)
        axes[1].plot(epoch, norm, color=colors[run_id], linewidth=1.8, label=label)
        axes[0].annotate(f"{loss[-1]:.4f}", (epoch[-1], loss[-1]), xytext=(-39, 5),
                         textcoords="offset points", fontsize=6.6, color=colors[run_id])
    axes[0].set_yscale("log")
    axes[1].set_yscale("log")
    axes[0].set(xlabel="Epoch", ylabel="Mean binary cross-entropy",
                title="Loss reveals optimization speed")
    axes[1].set(xlabel="Epoch", ylabel="Total gradient L2 norm",
                title="Gradient health changes during training")
    for ax in axes:
        ax.legend(frameon=False, fontsize=6.8)
        ax.grid(alpha=0.15)
    axes[0].text(0.98, 0.60, "0.01 has not learned\nXOR within this budget",
                 transform=axes[0].transAxes, ha="right", fontsize=7, color=NAVY)
    fig.suptitle("Learning rate changes the path even with identical data and initialization",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.025,
             "A useful run needs finite gradients and validation evidence—not merely a low training loss.",
             ha="center", color=NAVY, fontsize=7.4)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93))
    save_figure(fig, "fig-52-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
