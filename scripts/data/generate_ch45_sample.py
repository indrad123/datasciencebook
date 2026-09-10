"""Generate deterministic distributor time-to-event data for Chapter 45."""

import csv
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch45_sample.csv"
N = 240
GROUPS = ("standard", "enhanced")


def build_rows():
    rng = np.random.default_rng(45)
    groups = np.repeat(GROUPS, N // 2)
    scale = np.where(groups == "standard", 25.0, 38.0)
    true_event_time = rng.exponential(scale)
    administrative_limit = rng.uniform(18, 36, N)
    followup = np.round(np.minimum(true_event_time, administrative_limit), 3)
    event = (true_event_time <= administrative_limit).astype(int)

    # Entry is measured from a common programme-cohort origin. Later entrants
    # must not contribute to a risk set before they become observable.
    entry_month = np.zeros(N, dtype=int)
    entry_month[np.arange(N) % 12 == 5] = 3
    entry_month[np.arange(N) % 12 == 11] = 6
    exit_month = np.round(entry_month + followup, 3)

    rows = []
    for i in range(N):
        rows.append(
            {
                "distributor_id": f"D45-{i + 1:03d}",
                "retention_program": str(groups[i]),
                "region": ("Indonesia", "Southeast Asia", "Middle East", "Europe")[i % 4],
                "cohort_origin_month": "0",
                "entry_month": str(entry_month[i]),
                "observed_followup_months": f"{followup[i]:.3f}",
                "exit_month": f"{exit_month[i]:.3f}",
                "event_observed": str(event[i]),
                "end_state": "churn" if event[i] else "right_censored",
                "censor_reason": "" if event[i] else "administrative_study_end",
                "at_risk_month_12": "1" if followup[i] >= 12 else "0",
                "at_risk_month_24": "1" if followup[i] >= 24 else "0",
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
