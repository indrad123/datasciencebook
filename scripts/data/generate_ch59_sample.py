"""Generate the deterministic Chapter 59 forecasting and replenishment sample."""

import csv
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from datasciencebook.inventory_planning import (  # noqa: E402
    inventory_position,
    lead_time_target,
    order_up_to_quantity,
)

OUT = ROOT / "data/generated/ch59_sample.csv"
SEED = 20260828
HOLDOUT = 13
LEAD_TIME = 2
SERVICE_LEVEL = 0.90

PRODUCTS = [
    ("SAMBAL_250", 82, 11, 120, 24, 8, 12),
    ("KOPI_200", 61, 8, 90, 12, 4, 10),
    ("TEH_20", 48, 6, 70, 12, 2, 12),
]


def historical_two_week_errors(train):
    return np.array([
        np.sum(train[end:end + LEAD_TIME] - np.resize(train[end - 13:end], LEAD_TIME))
        for end in range(39, len(train) - LEAD_TIME, 2)
    ])


def build_rows():
    rng = np.random.default_rng(SEED)
    start = np.datetime64("2024-01-01")
    rows = []
    for product, base, amplitude, on_hand, on_order, backorders, case_pack in PRODUCTS:
        raw = []
        for week in range(104):
            promotion = int(week % 13 == 10)
            demand = max(0, round(base + 0.18 * week + amplitude * np.sin(2 * np.pi * week / 13)
                                  + 15 * promotion + rng.normal(0, 5)))
            stockout = int(demand > base + 24 and rng.random() < 0.18)
            sales = demand if not stockout else max(0, demand - int(rng.integers(4, 13)))
            raw.append((promotion, stockout, sales, demand))

        demand = np.array([x[3] for x in raw], dtype=float)
        train, test = demand[:-HOLDOUT], demand[-HOLDOUT:]
        seasonal = np.resize(train[-13:], HOLDOUT)
        last = np.repeat(train[-1], HOLDOUT)
        drift = train[-1] + (train[-1] - train[0]) / (len(train) - 1) * np.arange(1, HOLDOUT + 1)
        errors = historical_two_week_errors(train)
        plan = lead_time_target(seasonal[:LEAD_TIME], errors, SERVICE_LEVEL)
        position = inventory_position(on_hand, on_order, backorders)
        raw_order = max(0.0, plan["target"] - position)
        recommendation = order_up_to_quantity(plan["target"], position, case_pack)
        origin = str(start + np.timedelta64(7 * (len(train) - 1), "D"))

        for week, (promotion, stockout, sales, actual) in enumerate(raw):
            in_holdout = week >= len(train)
            h = week - len(train) + 1
            row = {
                "week_start": str(start + np.timedelta64(7 * week, "D")),
                "dc_id": "JKT_DC",
                "product_id": product,
                "promotion": str(promotion),
                "stockout": str(stockout),
                "observed_sales_cases": str(sales),
                "latent_demand_cases": str(actual),
                "data_split": "holdout" if in_holdout else "training",
                "forecast_origin_week": origin if in_holdout else "",
                "forecast_horizon_weeks": str(h) if in_holdout else "",
                "last_observation_forecast_cases": f"{last[h - 1]:.3f}" if in_holdout else "",
                "seasonal_naive_forecast_cases": f"{seasonal[h - 1]:.3f}" if in_holdout else "",
                "drift_forecast_cases": f"{drift[h - 1]:.3f}" if in_holdout else "",
                "selected_model": "seasonal_naive" if in_holdout else "",
                "selected_forecast_cases": f"{seasonal[h - 1]:.3f}" if in_holdout else "",
                "selected_error_cases": f"{test[h - 1] - seasonal[h - 1]:.3f}" if in_holdout else "",
                "selected_absolute_error_cases": f"{abs(test[h - 1] - seasonal[h - 1]):.3f}" if in_holdout else "",
                "lead_time_weeks": str(LEAD_TIME) if in_holdout else "",
                "service_level": f"{SERVICE_LEVEL:.2f}" if in_holdout else "",
                "lead_time_point_demand_cases": f"{plan['point_demand']:.3f}" if in_holdout else "",
                "error_quantile_cases": f"{plan['safety_stock']:.3f}" if in_holdout else "",
                "safety_stock_cases": f"{plan['safety_stock']:.3f}" if in_holdout else "",
                "order_up_to_target_cases": f"{plan['target']:.3f}" if in_holdout else "",
                "on_hand_cases": str(on_hand) if in_holdout else "",
                "on_order_cases": str(on_order) if in_holdout else "",
                "backorders_cases": str(backorders) if in_holdout else "",
                "inventory_position_cases": f"{position:.3f}" if in_holdout else "",
                "case_pack_cases": str(case_pack) if in_holdout else "",
                "unconstrained_order_cases": f"{raw_order:.3f}" if in_holdout else "",
                "recommended_order_cases": f"{recommendation:.3f}" if in_holdout else "",
                "accountable_owner": "Demand Planning Manager" if in_holdout else "",
                "approval_state": "planner_review_required" if in_holdout else "",
                "data_seed": str(SEED),
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
