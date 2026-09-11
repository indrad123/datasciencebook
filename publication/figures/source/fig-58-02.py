"""Figure 58.2: errors, review queues, slices, and release readiness."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))
from datasciencebook.responsibility import slice_error_rates
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch58_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    actual = np.array([int(r["actual_defect"]) for r in rows])
    probability = np.array([float(r["risk_probability"]) for r in rows])
    labels = np.array([r["outcome_label"] for r in rows])
    factory = np.array([r["factory"] for r in rows])
    uncertainty = np.array([r["uncertainty_review_flag"] == "true" for r in rows])
    harm = np.array([r["harm_review_flag"] == "true" for r in rows])

    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(8.0, 5.8), gridspec_kw={"height_ratios": [1.15, 0.85]})
    order = ["TP", "TN", "FP", "FN"]
    colors = [TEAL, BLUE, GOLD, RED]
    counts = [int(np.sum(labels == k)) for k in order]
    axes[0, 0].bar(order, counts, color=colors)
    axes[0, 0].set(title="Outcome inventory", ylabel="Packages", ylim=(0, 4.8))
    for i, count in enumerate(counts): axes[0, 0].text(i, count + 0.12, str(count), ha="center", fontsize=7)
    axes[0, 0].grid(axis="y", alpha=0.15)

    x = np.arange(1, 13)
    point_colors = [RED if k in ("FP", "FN") else TEAL for k in labels]
    axes[0, 1].scatter(x, probability, c=point_colors, s=44, edgecolor="white", linewidth=0.5)
    axes[0, 1].scatter(x[uncertainty], probability[uncertainty], facecolors="none", edgecolors=GOLD,
                       s=125, linewidth=1.7, label="near-threshold queue")
    axes[0, 1].scatter(x[harm], probability[harm], marker="s", facecolors="none", edgecolors=NAVY,
                       s=90, linewidth=1.1, label="highest-harm queue")
    axes[0, 1].axhline(0.5, color=NAVY, linestyle="--", linewidth=1)
    axes[0, 1].set(title="Ambiguity and harm queues serve different goals", xlabel="Package", ylabel="Risk probability",
                   xticks=x, ylim=(0, 1))
    axes[0, 1].legend(frameon=False, fontsize=6.2, loc="lower right")
    axes[0, 1].grid(alpha=0.15)

    slices = slice_error_rates(actual, probability, factory)
    sx = np.arange(len(slices))
    width = 0.34
    axes[1, 0].bar(sx - width / 2, [100 * r["error_rate"] for r in slices], width, color=GOLD, label="error rate")
    axes[1, 0].bar(sx + width / 2, [100 * r["false_negative_rate"] for r in slices], width, color=RED, label="false-negative rate")
    axes[1, 0].set(xticks=sx, xticklabels=[f'Factory {r["group"]}\nn={r["count"]}' for r in slices],
                   ylabel="Rate (%)", title="Slices need denominators and mechanisms", ylim=(0, 40))
    axes[1, 0].legend(frameon=False, fontsize=6.5)
    axes[1, 0].grid(axis="y", alpha=0.15)

    axes[1, 1].axis("off")
    checks = [("Owner", True), ("Intended use", True), ("Test slices", True),
              ("Fallback", True), ("Monitoring", True), ("Rollback", False)]
    axes[1, 1].text(0.5, 0.94, "Deployment gate", ha="center", va="top", color=NAVY, fontsize=10, weight="bold")
    for i, (name, passed) in enumerate(checks):
        y = 0.78 - i * 0.115
        axes[1, 1].text(0.18, y, "✓" if passed else "✕", color=TEAL if passed else RED,
                        fontsize=12, weight="bold", va="center")
        axes[1, 1].text(0.28, y, name, color=NAVY, fontsize=7.3, va="center")
    axes[1, 1].text(0.5, 0.05, "BLOCKED: define and test rollback", ha="center", color=RED, fontsize=7.5, weight="bold")

    fig.suptitle("Average accuracy is only the start of responsible release evidence",
                 color=NAVY, weight="bold", fontsize=11.5)
    fig.tight_layout(rect=(0, 0.01, 1, 0.93), h_pad=1.4, w_pad=1.5)
    save_figure(fig, "fig-58-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
