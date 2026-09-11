"""Figure 53.2: training controls and their inference rules."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch53_sample.csv").open(encoding="utf-8") as handle:
        benchmark = next(csv.DictReader(handle))

    rows = [
        ["Initialization", "unstable / weak signal", "sets starting scale", "fixed learned weights", "activation variance"],
        ["Input standardization", "scale imbalance", "centres and rescales inputs", "reuse training state", "means and scales"],
        ["Batch normalization", "shifting activations", "normalizes mini-batches", "use running statistics", "train/eval parity"],
        ["L2 / weight decay", "overly large weights", "penalizes magnitude", "no added inference step", "validation loss"],
        ["Dropout", "co-adaptation", "masks and rescales units", "turn masking off", "mode-switch test"],
        ["Early stopping", "validation deterioration", "keeps best checkpoint", "load selected checkpoint", "held-out curve"],
    ]
    columns = ["Control", "Primary warning", "During training", "Evaluation / inference", "Verify"]

    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    ax.axis("off")
    table = ax.table(cellText=rows, colLabels=columns, cellLoc="left", colLoc="left",
                     colWidths=[0.17, 0.20, 0.22, 0.24, 0.17], bbox=[0.01, 0.22, 0.98, 0.66])
    table.auto_set_font_size(False)
    table.set_fontsize(6.4)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("white")
        if row == 0:
            cell.set_facecolor(NAVY)
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        else:
            cell.set_facecolor(LIGHT_BLUE if row % 2 else "#F4F6F7")
            cell.get_text().set_color(NAVY)

    scale_1 = float(benchmark["training_sensor_1_scale"])
    scale_2 = float(benchmark["training_sensor_2_scale"])
    zero = 100 * float(benchmark["dropout_observed_zero_fraction"])
    output_mean = float(benchmark["dropout_output_mean"])
    penalty = float(benchmark["l2_penalty"])
    ax.text(0.02, 0.15, "REPRODUCIBLE BOOK CHECKS", transform=ax.transAxes,
            color=NAVY, fontsize=7.2, weight="bold")
    ax.text(0.02, 0.085,
            f"Training-fitted standardizer: means [4, 24], scales [{scale_1:.3f}, {scale_2:.3f}] → standardized means 0 and SDs 1",
            transform=ax.transAxes, color=NAVY, fontsize=6.8,
            bbox={"boxstyle": "round,pad=0.35", "facecolor": LIGHT_GOLD, "edgecolor": "white"})
    ax.text(0.02, 0.025,
            f"Inverted dropout at 25%: {zero:.2f}% zeros and output mean {output_mean:.3f}  |  L2 benchmark penalty: {penalty:.4f}",
            transform=ax.transAxes, color=NAVY, fontsize=6.8)
    fig.suptitle("Every training control needs an explicit evaluation and inference rule",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.915,
             "Fit preprocessing on training data only; store its state; test mode switches before deployment.",
             ha="center", color=NAVY, fontsize=7.5)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    save_figure(fig, "fig-53-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
