"""Generate the deterministic convolution and pooling trace for Chapter 54."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.convolution import (  # noqa: E402
    conv_parameter_count,
    convolve2d,
    max_pool2d,
    output_size,
    receptive_field,
)

OUT = ROOT / "data/generated/ch54_sample.csv"
KERNEL = np.array([[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]])


def build_arrays():
    image = np.zeros((12, 12), dtype=float)
    image[3:9, 3:9] = 1.0
    image[5:7, 6:10] = 0.2
    feature = convolve2d(image, KERNEL, stride=1, padding=1)
    pooled = max_pool2d(np.abs(feature), pool=2, stride=2)
    return image, feature, pooled


def build_rows():
    image, feature, pooled = build_arrays()
    dense_parameters = 224 * 224 * 3 * 16 + 16
    convolution_parameters = conv_parameter_count(3, 3, 3, 16)
    rows = []
    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            pool_row, pool_column = row // 2, column // 2
            rows.append(
                {
                    "pixel_row": str(row),
                    "pixel_column": str(column),
                    "input_intensity": f"{image[row, column]:.1f}",
                    "vertical_edge_response": f"{feature[row, column]:.10f}",
                    "absolute_edge_response": f"{abs(feature[row, column]):.10f}",
                    "pool_row": str(pool_row),
                    "pool_column": str(pool_column),
                    "pooled_max_absolute_response": f"{pooled[pool_row, pool_column]:.10f}",
                    "kernel_values_row_major": "-1;0;1;-1;0;1;-1;0;1",
                    "convolution_stride": "1",
                    "convolution_padding": "1",
                    "convolution_output_height": str(output_size(12, 3, 1, 1)),
                    "convolution_output_width": str(output_size(12, 3, 1, 1)),
                    "pool_size": "2",
                    "pool_stride": "2",
                    "pooled_output_height": str(output_size(12, 2, 2, 0)),
                    "pooled_output_width": str(output_size(12, 2, 2, 0)),
                    "three_layer_receptive_field": str(
                        receptive_field([(3, 1), (2, 2), (3, 1)])
                    ),
                    "dense_parameter_example": str(dense_parameters),
                    "convolution_parameter_example": str(convolution_parameters),
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
