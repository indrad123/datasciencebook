"""Generate deterministic gradient-descent teaching data for Chapter 11."""

from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "generated" / "ch11_sample.csv"


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for learning_rate in (0.05, 0.10, 0.60, 1.10):
        w = 0.0
        for iteration in range(21):
            gradient = 2.0 * (w - 4.0)
            loss = (w - 4.0) ** 2 + 2.0
            rows.append({
                "scenario": "one_parameter",
                "iteration": iteration,
                "learning_rate": learning_rate,
                "parameter_x": w,
                "parameter_y": "",
                "loss": loss,
                "gradient_x": gradient,
                "gradient_y": "",
                "gradient_norm": abs(gradient),
                "distance_to_optimum": abs(w - 4.0),
            })
            w -= learning_rate * gradient

    x, y, learning_rate = -3.0, 4.0, 0.10
    for iteration in range(21):
        gx, gy = 2.0 * (x - 2.0), 2.0 * (y + 1.0)
        rows.append({
            "scenario": "two_parameter",
            "iteration": iteration,
            "learning_rate": learning_rate,
            "parameter_x": x,
            "parameter_y": y,
            "loss": (x - 2.0) ** 2 + (y + 1.0) ** 2,
            "gradient_x": gx,
            "gradient_y": gy,
            "gradient_norm": math.hypot(gx, gy),
            "distance_to_optimum": math.hypot(x - 2.0, y + 1.0),
        })
        x -= learning_rate * gx
        y -= learning_rate * gy
    return rows


def main() -> None:
    rows = build_rows()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
