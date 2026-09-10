"""Generate a deterministic dense-network forward trace for Chapter 51."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.forward_network import forward_network  # noqa: E402

OUT = ROOT / "data/generated/ch51_sample.csv"
SEED = 51
CLASS_NAMES = np.array(["normal", "inspect", "reject"])


def network_layers():
    """Return the fixed 4-6-3 network used throughout the reader sample."""
    hidden_weights = np.array(
        [
            [1.0, 0.0, 0.0, 0.0, -0.8, 1.0],
            [0.0, 1.0, 0.0, 0.0, -0.7, 1.0],
            [0.0, 0.0, -1.0, 0.0, 0.6, -1.0],
            [0.0, 0.0, 0.0, 1.0, -0.3, 1.0],
        ]
    )
    hidden_bias = np.array([0.0, 0.0, 0.0, 0.0, 0.2, -1.0])
    output_weights = np.array(
        [
            [-0.6, 0.6, 0.9],
            [-0.5, 0.5, 0.8],
            [-0.5, 0.4, 0.7],
            [-0.4, 0.3, 0.6],
            [1.2, -0.5, -0.7],
            [-1.0, 0.2, 1.5],
        ]
    )
    output_bias = np.array([1.2, -0.2, -1.3])
    return [
        {"weights": hidden_weights, "bias": hidden_bias, "activation": "relu"},
        {"weights": output_weights, "bias": output_bias, "activation": "softmax"},
    ]


def build_rows():
    rng = np.random.default_rng(SEED)
    features = np.round(rng.normal(size=(32, 4)), 6)
    severity = (
        1.3 * features[:, 0]
        + 0.8 * features[:, 1]
        - 0.7 * features[:, 2]
        + 0.5 * features[:, 3]
    )
    true_index = np.where(severity < 0, 0, np.where(severity < 1.3, 1, 2))
    probabilities, trace = forward_network(features, network_layers(), return_trace=True)
    hidden_z = trace[0]["preactivation"]
    hidden_a = trace[0]["activation"]
    logits = trace[1]["preactivation"]
    predicted_index = np.argmax(probabilities, axis=1)
    loss = -np.log(probabilities[np.arange(len(features)), true_index])

    rows = []
    for i in range(len(features)):
        row = {
            "package_id": f"PKG51-{i + 1:02d}",
            "impact_score_standardized": f"{features[i, 0]:.6f}",
            "moisture_score_standardized": f"{features[i, 1]:.6f}",
            "seal_temperature_standardized": f"{features[i, 2]:.6f}",
            "line_speed_standardized": f"{features[i, 3]:.6f}",
            "synthetic_severity_score": f"{severity[i]:.6f}",
            "true_class": CLASS_NAMES[true_index[i]],
        }
        row.update({f"hidden_{j + 1}_preactivation": f"{hidden_z[i, j]:.6f}" for j in range(6)})
        row.update({f"hidden_{j + 1}_relu": f"{hidden_a[i, j]:.6f}" for j in range(6)})
        row.update({f"{CLASS_NAMES[j]}_logit": f"{logits[i, j]:.6f}" for j in range(3)})
        row.update({f"{CLASS_NAMES[j]}_probability": f"{probabilities[i, j]:.6f}" for j in range(3)})
        row["predicted_class"] = CLASS_NAMES[predicted_index[i]]
        row["cross_entropy_contribution"] = f"{loss[i]:.6f}"
        row["softmax_probability_sum"] = f"{probabilities[i].sum():.6f}"
        rows.append(row)
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
