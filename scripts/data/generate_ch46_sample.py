"""Generate deterministic propensity-weighting data for Chapter 46."""

import csv
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch46_sample.csv"
N = 600
TRUE_EFFECT = 8.0


def build_rows():
    rng = np.random.default_rng(46)
    prior = np.round(rng.normal(100, 22, N), 3)
    tenure = np.round(rng.uniform(1, 8, N), 3)
    logit = -4.2 + 0.035 * prior + 0.18 * tenure
    true_propensity = 1 / (1 + np.exp(-logit))
    treatment = rng.binomial(1, true_propensity)
    common_noise = rng.normal(0, 12, N)
    potential_y0 = np.round(35 + 0.72 * prior + 1.5 * tenure + common_noise, 3)
    potential_y1 = np.round(potential_y0 + TRUE_EFFECT, 3)
    observed = np.where(treatment == 1, potential_y1, potential_y0)

    x = np.column_stack([prior, tenure])
    model = LogisticRegression(max_iter=1000, random_state=46).fit(x, treatment)
    estimated = model.predict_proba(x)[:, 1]
    weights = treatment / estimated + (1 - treatment) / (1 - estimated)

    rows = []
    for i in range(N):
        rows.append(
            {
                "distributor_id": f"D46-{i + 1:03d}",
                "territory": ("West Indonesia", "Central Indonesia", "East Indonesia")[i % 3],
                "prior_90d_sales_kidr": f"{prior[i]:.3f}",
                "tenure_years": f"{tenure[i]:.3f}",
                "coached": str(treatment[i]),
                "assignment_propensity": f"{true_propensity[i]:.6f}",
                "estimated_propensity": f"{estimated[i]:.6f}",
                "ipw_ate": f"{weights[i]:.6f}",
                "potential_sales_no_coaching_kidr": f"{potential_y0[i]:.3f}",
                "potential_sales_coaching_kidr": f"{potential_y1[i]:.3f}",
                "observed_next_90d_sales_kidr": f"{observed[i]:.3f}",
                "simulated_individual_effect_kidr": f"{TRUE_EFFECT:.3f}",
                "overlap_supported": "1" if 0.05 <= estimated[i] <= 0.95 else "0",
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
