"""Generate a deterministic production-monitoring ledger for Chapter 48."""

import csv
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch48_sample.csv"

REQUESTS = [9820, 10040, 10180, 10320, 10560, 10740, 10920, 11160, 10880, 10420, 10680, 11020]
ERRORS = [18, 21, 24, 29, 34, 43, 62, 118, 381, 146, 47, 31]
P95_LATENCY = [78, 81, 84, 88, 91, 104, 119, 142, 196, 151, 96, 87]
MISSING_RATE = [0.010, 0.011, 0.012, 0.014, 0.016, 0.021, 0.028, 0.039, 0.061, 0.043, 0.019, 0.014]
PSI = [0.030, 0.040, 0.050, 0.070, 0.080, 0.110, 0.160, 0.240, 0.310, 0.180, 0.090, 0.060]
SCORE_MEAN = [0.289, 0.291, 0.294, 0.298, 0.302, 0.311, 0.327, 0.346, 0.382, 0.335, 0.304, 0.296]
ACTION_RATE = [0.000, 0.000, 0.081, 0.086, 0.092, 0.096, 0.104, 0.117, 0.141, 0.101, 0.094, 0.091]
LABEL_COVERAGE = [1.00, 1.00, 1.00, 0.99, 0.98, 0.92, 0.81, 0.65, 0.43, 0.24, 0.10, 0.00]
BRIER = [0.218, 0.214, 0.211, 0.209, 0.207, 0.212, 0.221, None, None, None, None, None]
VERSIONS = ["v1.1-shadow", "v1.1-shadow", "v1.1-canary", "v1.1-canary", "v1.1", "v1.1", "v1.1", "v1.1", "v1.1", "v1.0", "v1.0", "v1.0"]
STAGES = ["shadow", "shadow", "canary", "canary", "full", "full", "full", "full", "full", "rollback", "recovered", "recovered"]
DECISION_TRAFFIC = [0.00, 0.00, 0.10, 0.25, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]
RESPONSES = [
    "observe shadow logs", "approve limited canary", "continue canary", "approve full release",
    "routine monitoring", "open drift investigation", "compare seasonal reference", "prepare rollback",
    "stop v1.1 and roll back", "verify containment", "close incident after review", "routine monitoring",
]


def alert_state(error_rate, latency, missing, psi):
    if error_rate >= 0.03 or latency >= 180 or missing >= 0.05 or psi >= 0.25:
        return "critical"
    if error_rate >= 0.01 or latency >= 120 or missing >= 0.03 or psi >= 0.10:
        return "warning"
    return "ok"


def build_rows():
    rows = []
    start = date(2026, 1, 5)
    for i in range(12):
        error_rate = ERRORS[i] / REQUESTS[i]
        state = alert_state(error_rate, P95_LATENCY[i], MISSING_RATE[i], PSI[i])
        incident = "INC-48-001" if 8 <= i <= 10 else ""
        rows.append(
            {
                "cohort_week": (start + timedelta(weeks=i)).isoformat(),
                "model_version": VERSIONS[i],
                "release_stage": STAGES[i],
                "decision_traffic_share": f"{DECISION_TRAFFIC[i]:.2f}",
                "requests": str(REQUESTS[i]),
                "error_count": str(ERRORS[i]),
                "error_rate": f"{error_rate:.6f}",
                "p95_latency_ms": str(P95_LATENCY[i]),
                "route_distance_missing_rate": f"{MISSING_RATE[i]:.3f}",
                "route_distance_psi": f"{PSI[i]:.3f}",
                "mean_late_risk_score": f"{SCORE_MEAN[i]:.3f}",
                "intervention_action_rate": f"{ACTION_RATE[i]:.3f}",
                "mature_label_join_coverage": f"{LABEL_COVERAGE[i]:.2f}",
                "mature_cohort_brier_score": "" if BRIER[i] is None else f"{BRIER[i]:.3f}",
                "alert_state": state,
                "incident_id": incident,
                "response_action": RESPONSES[i],
                "accountable_owner": "ML operations lead",
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
