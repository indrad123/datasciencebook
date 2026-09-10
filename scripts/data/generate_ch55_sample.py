"""Generate a deterministic self-attention trace for Chapter 55."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.attention import (  # noqa: E402
    causal_mask,
    scaled_dot_product_attention,
    sinusoidal_positions,
)

OUT = ROOT / "data/generated/ch55_sample.csv"
TOKENS = ["stok", "kopi", "belum", "tiba", "jakarta"]
QK = np.array([[1, 0], [0.8, 0.2], [0, 1], [0.2, 0.8], [0.5, 0.5]], dtype=float)
VALUES = np.arange(10, dtype=float).reshape(5, 2)


def build_rows():
    dimension = QK.shape[1]
    scale = np.sqrt(dimension)
    scores = QK @ QK.T / scale
    output, weights = scaled_dot_product_attention(QK, QK, VALUES)
    permitted = causal_mask(len(TOKENS))
    causal_output, causal_weights = scaled_dot_product_attention(
        QK, QK, VALUES, permitted
    )
    positions = sinusoidal_positions(len(TOKENS), 6)

    rows = []
    for query_position, query_token in enumerate(TOKENS):
        for source_position, source_token in enumerate(TOKENS):
            position = positions[source_position]
            rows.append(
                {
                    "query_position": str(query_position),
                    "query_token": query_token,
                    "source_position": str(source_position),
                    "source_token": source_token,
                    "query_component_1": f"{QK[query_position, 0]:.1f}",
                    "query_component_2": f"{QK[query_position, 1]:.1f}",
                    "key_component_1": f"{QK[source_position, 0]:.1f}",
                    "key_component_2": f"{QK[source_position, 1]:.1f}",
                    "value_component_1": f"{VALUES[source_position, 0]:.1f}",
                    "value_component_2": f"{VALUES[source_position, 1]:.1f}",
                    "scaled_compatibility_score": f"{scores[query_position, source_position]:.12f}",
                    "unmasked_attention_weight": f"{weights[query_position, source_position]:.12f}",
                    "causal_allowed": str(bool(permitted[query_position, source_position])).lower(),
                    "causal_attention_weight": f"{causal_weights[query_position, source_position]:.12f}",
                    "unmasked_output_component_1": f"{output[query_position, 0]:.12f}",
                    "unmasked_output_component_2": f"{output[query_position, 1]:.12f}",
                    "causal_output_component_1": f"{causal_output[query_position, 0]:.12f}",
                    "causal_output_component_2": f"{causal_output[query_position, 1]:.12f}",
                    "position_sin_1": f"{position[0]:.12f}",
                    "position_cos_1": f"{position[1]:.12f}",
                    "position_sin_2": f"{position[2]:.12f}",
                    "position_cos_2": f"{position[3]:.12f}",
                    "position_sin_3": f"{position[4]:.12f}",
                    "position_cos_3": f"{position[5]:.12f}",
                    "attention_dimension": str(dimension),
                    "score_divisor": f"{scale:.12f}",
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
