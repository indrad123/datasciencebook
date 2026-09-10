"""Generate deterministic training-control diagnostics for Chapter 53."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.training_controls import (  # noqa: E402
    activation_variances,
    apply_standardizer,
    dropout,
    fit_standardizer,
    initialize_weights,
    l2_penalty,
)

OUT = ROOT / "data/generated/ch53_sample.csv"
DATA_SEED = 53
WEIGHT_SEED = 1
LAYERS = 8


def he_relu_variances(x):
    """Propagate through He-initialized ReLU layers with fixed per-layer seeds."""
    activation = x.copy()
    values = []
    for layer in range(LAYERS):
        weights = initialize_weights(
            activation.shape[1], 64, scheme="he", seed=WEIGHT_SEED + layer
        )
        activation = np.maximum(0.0, activation @ weights)
        values.append(float(np.var(activation)))
    return values


def build_rows():
    rng = np.random.default_rng(DATA_SEED)
    x = rng.normal(size=(1000, 32))
    small = activation_variances(x, [64] * LAYERS, "small", WEIGHT_SEED)
    xavier = activation_variances(x, [64] * LAYERS, "xavier", WEIGHT_SEED)
    he_relu = he_relu_variances(x)

    sensor = np.array([[2.0, 20.0], [4.0, 24.0], [6.0, 28.0]])
    state = fit_standardizer(sensor)
    standardized = apply_standardizer(sensor, state)
    dropped = dropout(np.ones(20_000), rate=0.25, training=True, seed=7)
    penalty = l2_penalty([np.array([[1.0, -2.0], [0.5, 0.0]])], 0.1)

    rows = []
    for layer in range(LAYERS):
        fan_in = 32 if layer == 0 else 64
        rows.append(
            {
                "layer_number": str(layer + 1),
                "fan_in": str(fan_in),
                "fan_out": "64",
                "data_seed": str(DATA_SEED),
                "weight_seed": str(WEIGHT_SEED + layer),
                "small_tanh_weight_scale": "0.010000000",
                "small_tanh_activation_variance": f"{small[layer]:.12e}",
                "xavier_tanh_weight_scale": f"{np.sqrt(2 / (fan_in + 64)):.9f}",
                "xavier_tanh_activation_variance": f"{xavier[layer]:.12f}",
                "he_relu_weight_scale": f"{np.sqrt(2 / fan_in):.9f}",
                "he_relu_activation_variance": f"{he_relu[layer]:.12f}",
                "training_sensor_1_mean": f"{state['mean'][0]:.6f}",
                "training_sensor_1_scale": f"{state['scale'][0]:.9f}",
                "training_sensor_2_mean": f"{state['mean'][1]:.6f}",
                "training_sensor_2_scale": f"{state['scale'][1]:.9f}",
                "standardized_sensor_1_mean": f"{standardized[:, 0].mean():.9f}",
                "standardized_sensor_1_std": f"{standardized[:, 0].std():.9f}",
                "standardized_sensor_2_mean": f"{standardized[:, 1].mean():.9f}",
                "standardized_sensor_2_std": f"{standardized[:, 1].std():.9f}",
                "dropout_rate": "0.25",
                "dropout_observed_zero_fraction": f"{np.mean(dropped == 0):.6f}",
                "dropout_output_mean": f"{dropped.mean():.9f}",
                "l2_strength": "0.10",
                "l2_penalty": f"{penalty:.6f}",
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
