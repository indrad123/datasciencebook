"""Generate deterministic product-portfolio PCA data for Chapter 40."""

import csv
from pathlib import Path

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch40_sample.csv"
FEATURES = (
    "weekly_unit_volume",
    "weekly_order_count",
    "stockout_rate",
    "contribution_margin_pct",
    "promotion_share",
    "supplier_lead_days",
)


def build_rows():
    index = np.arange(240)
    activity = 0.95 * np.sin(index * 0.173) + 0.55 * np.cos(index * 0.071)
    positioning = 0.80 * np.cos(index * 0.137) + 0.35 * np.sin(index * 0.047)
    supply = 0.65 * np.sin(index * 0.097 + 0.8)
    noise = lambda frequency, phase=0: 0.12 * np.sin(index * frequency + phase)

    values = np.column_stack(
        (
            980 + 250 * activity + 35 * positioning + 22 * noise(0.41),
            36 + 8.5 * activity + 1.5 * positioning + noise(0.37, 0.4),
            0.075 - 0.020 * activity + 0.012 * supply + 0.004 * noise(0.53),
            24 + 2.8 * positioning - 0.8 * supply + 0.4 * noise(0.31, 0.7),
            0.28 + 0.075 * positioning + 0.025 * activity + 0.01 * noise(0.29),
            8.2 + 1.7 * supply - 0.55 * positioning + 0.25 * noise(0.43, 0.2),
        )
    )
    # Quantise the released measurements before fitting so every published PCA
    # output can be reproduced exactly from the CSV inputs.
    values = np.column_stack(
        (
            np.round(values[:, 0], 2),
            np.round(values[:, 1], 2),
            np.round(values[:, 2], 5),
            np.round(values[:, 3], 3),
            np.round(values[:, 4], 5),
            np.round(values[:, 5], 3),
        )
    )
    is_test = index % 4 == 3
    scaler = StandardScaler().fit(values[~is_test])
    scaled = scaler.transform(values)
    pca = PCA(n_components=2, svd_solver="full").fit(scaled[~is_test])
    scores = pca.transform(scaled)
    reconstructed = pca.inverse_transform(scores)
    rmse = np.sqrt(np.mean((scaled - reconstructed) ** 2, axis=1))

    rows = []
    families = ("staples", "beverages", "snacks", "premium")
    for i in range(240):
        row = {
            "product_id": f"P40-{i + 1:03d}",
            "product_family": families[i % len(families)],
            "evaluation_split": "test" if is_test[i] else "training",
            "weekly_unit_volume": f"{values[i, 0]:.2f}",
            "weekly_order_count": f"{values[i, 1]:.2f}",
            "stockout_rate": f"{values[i, 2]:.5f}",
            "contribution_margin_pct": f"{values[i, 3]:.3f}",
            "promotion_share": f"{values[i, 4]:.5f}",
            "supplier_lead_days": f"{values[i, 5]:.3f}",
            "pc1_score": f"{scores[i, 0]:.6f}",
            "pc2_score": f"{scores[i, 1]:.6f}",
            "two_component_reconstruction_rmse": f"{rmse[i]:.6f}",
        }
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
