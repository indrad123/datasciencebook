"""Generate deterministic weekly demand and forecast vintages for Chapter 42."""

import csv
from datetime import date, timedelta
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch42_sample.csv"
SEASON = 52
TRAIN_WEEKS = 130


def seasonal_naive(history, horizon):
    return np.resize(history[-SEASON:], horizon)


def build_rows():
    rng = np.random.default_rng(42)
    weeks = np.arange(156)
    trend = np.round(520 + 1.15 * weeks, 2)
    seasonal = np.round(75 * np.sin(2 * np.pi * weeks / SEASON), 2)
    event = np.zeros(156)
    event[[35, 36, 88, 89, 140, 141]] = [42, 55, 48, 60, 52, 64]
    event[112] = -78
    irregular = np.round(rng.normal(0, 18, len(weeks)), 2)
    demand = np.round(trend + seasonal + event + irregular, 2)

    train = demand[:TRAIN_WEEKS]
    horizon = len(demand) - TRAIN_WEEKS
    naive = np.repeat(train[-1], horizon)
    seasonal_fc = seasonal_naive(train, horizon)
    slope = (train[-1] - train[0]) / (len(train) - 1)
    drift = train[-1] + slope * np.arange(1, horizon + 1)
    seasonal_errors = train[SEASON:] - train[:-SEASON]
    sigma = np.std(seasonal_errors, ddof=1)
    h = np.arange(1, horizon + 1)
    half_width = 1.282 * sigma * np.sqrt(1 + h / SEASON)

    start = date(2023, 1, 2)
    rows = []
    for i in weeks:
        test = i >= TRAIN_WEEKS
        j = i - TRAIN_WEEKS
        rows.append(
            {
                "week_start": (start + timedelta(weeks=int(i))).isoformat(),
                "week_index": str(i + 1),
                "trend_level_cases": f"{trend[i]:.2f}",
                "seasonal_component_cases": f"{seasonal[i]:.2f}",
                "event_adjustment_cases": f"{event[i]:.2f}",
                "irregular_component_cases": f"{irregular[i]:.2f}",
                "cases_shipped": f"{demand[i]:.2f}",
                "evaluation_split": "holdout" if test else "training",
                "forecast_origin_week": str(TRAIN_WEEKS) if test else "",
                "horizon_weeks": str(j + 1) if test else "",
                "naive_forecast_cases": f"{naive[j]:.2f}" if test else "",
                "seasonal_naive_forecast_cases": f"{seasonal_fc[j]:.2f}" if test else "",
                "drift_forecast_cases": f"{drift[j]:.2f}" if test else "",
                "seasonal_naive_lower_80": f"{seasonal_fc[j] - half_width[j]:.2f}" if test else "",
                "seasonal_naive_upper_80": f"{seasonal_fc[j] + half_width[j]:.2f}" if test else "",
                "seasonal_naive_error_cases": f"{demand[i] - seasonal_fc[j]:.2f}" if test else "",
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
