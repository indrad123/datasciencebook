"""Figure 50.2: full-batch gradient descent and its learned linear boundary."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))
from datasciencebook.neuron import classify, neuron_probabilities, train_logistic_neuron
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch50_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    features = np.array([[float(r["impact_score_standardized"]),
                          float(r["moisture_score_standardized"])] for r in rows])
    labels = np.array([int(r["damage_label"]) for r in rows])
    fit = train_logistic_neuron(features, labels, learning_rate=0.15, epochs=900)
    probabilities = neuron_probabilities(features, fit["weights"], fit["bias"])
    predictions = classify(probabilities, 0.5)
    accuracy = np.mean(predictions == labels)

    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.3))
    epochs = np.arange(1, 901)
    axes[0].plot(epochs, fit["loss_history"], color=BLUE, linewidth=2)
    axes[0].scatter([1, 900], [fit["loss_history"][0], fit["loss_history"][-1]],
                    color=[GOLD, TEAL], s=45, zorder=3)
    axes[0].annotate(f"initial {fit['loss_history'][0]:.3f}", (1, fit["loss_history"][0]),
                     xytext=(23, -2), textcoords="offset points", fontsize=7, color=NAVY)
    axes[0].annotate(f"final {fit['loss_history'][-1]:.3f}", (900, fit["loss_history"][-1]),
                     xytext=(-74, 10), textcoords="offset points", fontsize=7, color=NAVY)
    axes[0].set(xlabel="Epoch", ylabel="Mean binary cross-entropy",
                title="Full-batch gradient descent")
    axes[0].text(0.43, 0.73, "$p-y$ supplies the batch gradient signal",
                 transform=axes[0].transAxes, fontsize=7, color=NAVY)

    correct = predictions == labels
    for label, color, marker, name in [(0, BLUE, "o", "no damage"), (1, RED, "^", "damage")]:
        mask = labels == label
        axes[1].scatter(features[mask, 0], features[mask, 1], color=color, marker=marker,
                        s=23, alpha=0.70, label=name, edgecolors="none")
    wrong = ~correct
    axes[1].scatter(features[wrong, 0], features[wrong, 1], facecolors="none", edgecolors=GOLD,
                    linewidths=1.2, s=58, label="training error")
    xline = np.linspace(features[:, 0].min() - 0.2, features[:, 0].max() + 0.2, 150)
    yline = -(fit["bias"] + fit["weights"][0] * xline) / fit["weights"][1]
    axes[1].plot(xline, yline, color=NAVY, linewidth=1.8, label="$p=0.50$ boundary")
    axes[1].set(xlabel="Standardized impact score", ylabel="Standardized moisture score",
                title=f"One neuron: linear boundary, {accuracy:.1%} accuracy")
    axes[1].legend(frameon=False, fontsize=6.7, loc="lower left")
    axes[1].text(0.98, 0.98, "More epochs cannot make\none line represent XOR",
                 transform=axes[1].transAxes, ha="right", va="top", fontsize=7,
                 color=NAVY, bbox={"facecolor": "white", "edgecolor": NAVY, "pad": 3})

    fig.suptitle("Optimization lowers training loss; representation still limits the model",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    save_figure(fig, "fig-50-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
