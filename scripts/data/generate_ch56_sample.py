"""Generate deterministic linear-autoencoder diagnostics for Chapter 56."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.generative import (  # noqa: E402
    decode,
    encode,
    fit_linear_autoencoder,
    reconstruction_error,
)

OUT = ROOT / "data/generated/ch56_sample.csv"
SEED = 56


def build_rows():
    rng = np.random.default_rng(SEED)
    base = rng.normal(size=(60, 2))
    routine = np.column_stack(
        [base[:, 0], base[:, 1], base[:, 0] + base[:, 1] + rng.normal(0, 0.08, 60)]
    )
    mean, components = fit_linear_autoencoder(routine, latent_dimension=2)
    routine_latent = encode(routine, mean, components)
    routine_reconstruction = decode(routine_latent, mean, components)
    routine_errors = reconstruction_error(routine, routine_reconstruction)
    threshold = float(np.quantile(routine_errors, 0.95))

    unusual = np.array([[4.0, -4.0, 4.0]])
    unusual_latent = encode(unusual, mean, components)
    unusual_reconstruction = decode(unusual_latent, mean, components)

    data = np.vstack([routine, unusual])
    latent = np.vstack([routine_latent, unusual_latent])
    reconstruction = np.vstack([routine_reconstruction, unusual_reconstruction])
    errors = reconstruction_error(data, reconstruction)
    descending_rank = np.empty(len(errors), dtype=int)
    descending_rank[np.argsort(-errors, kind="stable")] = np.arange(1, len(errors) + 1)

    rows = []
    for index in range(len(data)):
        residual = data[index] - reconstruction[index]
        package_type = "routine_fit" if index < 60 else "unusual_scored_after_fit"
        rows.append(
            {
                "package_id": f"PKG-{index + 1:03d}",
                "package_type": package_type,
                "fit_in_autoencoder": str(index < 60).lower(),
                "signal_1": f"{data[index, 0]:.12f}",
                "signal_2": f"{data[index, 1]:.12f}",
                "signal_3": f"{data[index, 2]:.12f}",
                "latent_1": f"{latent[index, 0]:.12f}",
                "latent_2": f"{latent[index, 1]:.12f}",
                "reconstructed_signal_1": f"{reconstruction[index, 0]:.12f}",
                "reconstructed_signal_2": f"{reconstruction[index, 1]:.12f}",
                "reconstructed_signal_3": f"{reconstruction[index, 2]:.12f}",
                "residual_signal_1": f"{residual[0]:.12f}",
                "residual_signal_2": f"{residual[1]:.12f}",
                "residual_signal_3": f"{residual[2]:.12f}",
                "reconstruction_mse": f"{errors[index]:.12f}",
                "routine_error_p95": f"{threshold:.12f}",
                "illustrative_review_flag": str(errors[index] > threshold).lower(),
                "descending_error_rank": str(descending_rank[index]),
                "data_seed": str(SEED),
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
