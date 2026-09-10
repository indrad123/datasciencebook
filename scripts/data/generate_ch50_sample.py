"""Generate the deterministic single-neuron training sample for Chapter 50."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.neuron import (  # noqa: E402
    classify,
    neuron_probabilities,
    train_logistic_neuron,
)

OUT = ROOT / "data/generated/ch50_sample.csv"
SEED = 50
LEARNING_RATE = 0.15
EPOCHS = 900
THRESHOLD = 0.50


def build_rows():
    rng = np.random.default_rng(SEED)
    # Six decimals keeps the released inputs compact while making every fitted
    # value exactly reproducible from the CSV itself.
    features = np.round(rng.normal(size=(240, 2)), 6)
    noise = np.round(rng.normal(0, 0.55, 240), 6)
    latent = 1.6 * features[:, 0] + features[:, 1] - 0.35 + noise
    labels = (latent > 0).astype(int)

    fit = train_logistic_neuron(
        features, labels, learning_rate=LEARNING_RATE, epochs=EPOCHS
    )
    logits = features @ fit["weights"] + fit["bias"]
    probabilities = neuron_probabilities(features, fit["weights"], fit["bias"])
    predictions = classify(probabilities, THRESHOLD)
    loss = -(labels * np.log(probabilities) + (1 - labels) * np.log(1 - probabilities))
    signed_distance = logits / np.linalg.norm(fit["weights"])

    rows = []
    for i in range(len(features)):
        rows.append(
            {
                "package_id": f"PKG50-{i + 1:03d}",
                "impact_score_standardized": f"{features[i, 0]:.6f}",
                "moisture_score_standardized": f"{features[i, 1]:.6f}",
                "latent_damage_score": f"{latent[i]:.6f}",
                "damage_label": str(labels[i]),
                "initial_probability": "0.500000",
                "trained_logit": f"{logits[i]:.6f}",
                "trained_probability": f"{probabilities[i]:.6f}",
                "predicted_damage_at_0_5": str(predictions[i]),
                "binary_cross_entropy_contribution": f"{loss[i]:.6f}",
                "probability_minus_label": f"{probabilities[i] - labels[i]:.6f}",
                "signed_boundary_distance": f"{signed_distance[i]:.6f}",
                "classification_correct": str(int(predictions[i] == labels[i])),
            }
        )
    return rows


def main():
    rows = build_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
