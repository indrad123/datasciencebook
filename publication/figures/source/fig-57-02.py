"""Figure 57.2: held-out quality gains and computational cost."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch57_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    modalities = [r["modality"] for r in rows]
    baseline = np.array([float(r["baseline_quality"]) for r in rows])
    deep = np.array([float(r["deep_quality"]) for r in rows])
    gains = np.array([float(r["relative_improvement_pct"]) for r in rows])
    hours = np.array([float(r["deep_training_hours"]) for r in rows])
    latency = np.array([float(r["deep_inference_ms"]) for r in rows])
    score = np.array([float(r["deep_value_per_compute"]) for r in rows])

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 4.4))
    x = np.arange(len(rows))
    axes[0].bar(x - 0.18, baseline, 0.36, label="strong baseline", color=BLUE)
    axes[0].bar(x + 0.18, deep, 0.36, label="neural candidate", color=GOLD)
    axes[0].set(xticks=x, xticklabels=modalities, ylim=(0.70, 0.94), ylabel="Illustrative held-out quality",
                title="Deep learning does not win uniformly")
    axes[0].legend(frameon=False, fontsize=7)
    axes[0].grid(axis="y", alpha=0.15)
    for i, (b, d) in enumerate(zip(baseline, deep)):
        axes[0].text(i - 0.18, b + 0.006, f"{b:.2f}", ha="center", fontsize=6)
        axes[0].text(i + 0.18, d + 0.006, f"{d:.2f}", ha="center", fontsize=6)

    colors = [RED if g < 0 else TEAL for g in gains]
    axes[1].scatter(hours, gains, s=latency * 5.5, c=colors, edgecolor=NAVY, linewidth=0.5)
    axes[1].axhline(0, color=NAVY, linewidth=0.8)
    for m, h, g in zip(modalities, hours, gains):
        axes[1].annotate(m, (h, g), xytext=(4, 5), textcoords="offset points", fontsize=6.7)
    winner = int(np.argmax(score))
    axes[1].annotate("highest value-per-compute", (hours[winner], gains[winner]),
                     xytext=(-6, -30), textcoords="offset points", ha="center", color=TEAL, fontsize=6.5,
                     arrowprops={"arrowstyle": "->", "color": TEAL})
    axes[1].set(xlabel="Neural-candidate training hours", ylabel="Relative quality gain (%)",
                title="Quality gain must be read with cost and latency")
    axes[1].grid(alpha=0.15)
    fig.suptitle("A fair modality comparison retains strong baselines and operational costs",
                 color=NAVY, weight="bold", fontsize=11.5)
    fig.text(0.5, 0.018, "Bubble area represents neural inference latency; all values are synthetic teaching assumptions, not benchmarks.",
             ha="center", color=NAVY, fontsize=7.1)
    fig.tight_layout(rect=(0, 0.055, 1, 0.92), w_pad=1.6)
    save_figure(fig, "fig-57-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
