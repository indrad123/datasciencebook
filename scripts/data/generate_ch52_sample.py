"""Generate deterministic gradient-check and optimization traces for Chapter 52."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.backpropagation import (  # noqa: E402
    finite_difference,
    forward,
    gradients,
    initialize,
    train,
)

OUT = ROOT / "data/generated/ch52_sample.csv"
SEED = 2
EPOCHS = 800
LEARNING_RATES = [("slow", 0.01), ("moderate", 0.10), ("fast", 0.50)]
XOR_X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
XOR_Y = np.array([0, 1, 1, 0], dtype=float)


def gradient_check():
    parameters = initialize(2, 4, seed=SEED)
    _, cache = forward(XOR_X, parameters)
    analytical = gradients(XOR_Y, parameters, cache)["W1"][0, 0]
    numerical = finite_difference(XOR_X, XOR_Y, parameters, "W1", (0, 0), epsilon=1e-5)
    return float(analytical), float(numerical)


def build_rows():
    analytical, numerical = gradient_check()
    rows = []
    for run_label, rate in LEARNING_RATES:
        parameters, history, norms = train(
            XOR_X, XOR_Y, hidden_size=4, learning_rate=rate, epochs=EPOCHS, seed=SEED
        )
        final_probability = forward(XOR_X, parameters)[0]
        final_pattern = "".join(str(v) for v in (final_probability >= 0.5).astype(int))
        for epoch, (epoch_loss, norm) in enumerate(zip(history, norms), start=1):
            rows.append(
                {
                    "run_id": f"xor-{run_label}",
                    "seed": str(SEED),
                    "learning_rate": f"{rate:.2f}",
                    "epoch": str(epoch),
                    "loss_before_update": f"{epoch_loss:.9f}",
                    "total_gradient_norm": f"{norm:.9f}",
                    "analytical_gradient_w1_00": f"{analytical:.12f}",
                    "numerical_gradient_w1_00": f"{numerical:.12f}",
                    "absolute_gradient_check_difference": f"{abs(analytical - numerical):.15f}",
                    "final_probability_x00": f"{final_probability[0]:.9f}",
                    "final_probability_x01": f"{final_probability[1]:.9f}",
                    "final_probability_x10": f"{final_probability[2]:.9f}",
                    "final_probability_x11": f"{final_probability[3]:.9f}",
                    "final_prediction_pattern": final_pattern,
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
