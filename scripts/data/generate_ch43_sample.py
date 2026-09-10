"""Generate deterministic recommendation-ranking data for Chapter 43."""

import csv
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch43_sample.csv"
USERS = 80
ITEMS = 12
FAMILIES = ("noodles", "spices", "coffee", "tea")
MARKETS = ("SEA", "MEA", "EU", "AMER")


def stable_ranks(scores, eligible):
    order = [i for i in np.argsort(-scores, kind="stable") if eligible[i]]
    ranks = {item: rank for rank, item in enumerate(order, 1)}
    return ranks


def build_rows():
    rng = np.random.default_rng(43)
    user_factors = rng.normal(size=(USERS, 3))
    item_factors = rng.normal(size=(ITEMS, 3))
    affinity = user_factors @ item_factors.T
    interactions = np.where(
        affinity + rng.normal(0, 0.8, (USERS, ITEMS)) > 1.0,
        rng.integers(1, 6, (USERS, ITEMS)),
        0,
    ).astype(float)
    train = interactions.copy()
    held_out = {}
    for user in range(USERS):
        positives = np.flatnonzero(train[user] > 0)
        if len(positives) > 1:
            held_out[user] = int(positives[-1])
            train[user, positives[-1]] = 0

    popularity = train.sum(axis=0)
    u, singular, vt = np.linalg.svd(train, full_matrices=False)
    latent = (u[:, :3] * singular[:3]) @ vt[:3]
    stock = np.array([1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], dtype=bool)

    rows = []
    for user in range(USERS):
        seen = train[user] > 0
        unseen = ~seen
        market = MARKETS[user % len(MARKETS)]
        market_ok = np.ones(ITEMS, dtype=bool)
        if market == "EU":
            market_ok[11] = False
        if market == "MEA":
            market_ok[9] = False
        eligible = unseen & stock & market_ok
        pop_ranks = stable_ranks(popularity, unseen)
        latent_ranks = stable_ranks(latent[user], unseen)
        bought_families = {FAMILIES[item % 4] for item in np.flatnonzero(seen)}
        diversity_bonus = np.array([0.18 if FAMILIES[item % 4] not in bought_families else 0 for item in range(ITEMS)])
        business_score = latent[user] - 0.002 * popularity + diversity_bonus
        final_ranks = stable_ranks(business_score, eligible)
        for item in range(ITEMS):
            rows.append(
                {
                    "distributor_id": f"D43-{user + 1:03d}",
                    "market": market,
                    "product_id": f"SKU-{item + 1:02d}",
                    "product_family": FAMILIES[item % 4],
                    "training_interaction_count": str(int(train[user, item])),
                    "held_out_relevant": "1" if held_out.get(user) == item else "0",
                    "seen_in_training": "1" if seen[item] else "0",
                    "stock_available": "1" if stock[item] else "0",
                    "market_eligible": "1" if market_ok[item] else "0",
                    "popularity_score": f"{popularity[item]:.2f}",
                    "latent_score": f"{latent[user, item]:.6f}",
                    "popularity_unseen_rank": str(pop_ranks[item]) if item in pop_ranks else "",
                    "latent_unseen_rank": str(latent_ranks[item]) if item in latent_ranks else "",
                    "final_business_score": f"{business_score[item]:.6f}",
                    "final_eligible_rank": str(final_ranks[item]) if item in final_ranks else "",
                    "recommended_top_5": "1" if final_ranks.get(item, 999) <= 5 else "0",
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
