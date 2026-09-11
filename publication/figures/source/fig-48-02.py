"""Figure 48.2: layered monitoring with delayed labels and response."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, GREY, LIGHT_BLUE, NAVY, RED, TEAL, apply_style, save_figure


def main():
    with (ROOT / "data/generated/ch48_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    weeks = np.arange(1, len(rows) + 1)
    psi = np.array([float(r["route_distance_psi"]) for r in rows])
    missing = np.array([float(r["route_distance_missing_rate"]) for r in rows])
    latency = np.array([float(r["p95_latency_ms"]) for r in rows])
    coverage = np.array([float(r["mature_label_join_coverage"]) for r in rows])
    brier = np.array([np.nan if not r["mature_cohort_brier_score"] else float(r["mature_cohort_brier_score"]) for r in rows])
    states = [r["alert_state"] for r in rows]

    apply_style()
    fig, axes = plt.subplots(4, 1, figsize=(7.6, 6.5), sharex=True,
                             gridspec_kw={"height_ratios": [1.2, 1.2, 1.2, 0.72]})

    axes[0].plot(weeks, psi, marker="o", color=BLUE, linewidth=1.8)
    axes[0].axhline(0.10, color=GOLD, linestyle=":", label="warning 0.10")
    axes[0].axhline(0.25, color=RED, linestyle=":", label="critical 0.25")
    axes[0].set(ylabel="PSI", title="Covariate drift")
    axes[0].legend(frameon=False, ncol=2, loc="upper left")

    axes[1].plot(weeks, missing / 0.05 * 100, marker="s", color=TEAL, label="distance missingness")
    axes[1].plot(weeks, latency / 180 * 100, marker="o", color=BLUE, label="P95 latency")
    axes[1].axhline(100, color=RED, linestyle=":", label="critical threshold")
    axes[1].set(ylabel="% of critical", title="Data quality and service health")
    axes[1].legend(frameon=False, ncol=3, loc="upper left")

    axes[2].bar(weeks, coverage * 100, color=LIGHT_BLUE, edgecolor=BLUE, label="label-join coverage")
    axes[2].set(ylabel="Coverage (%)", ylim=(0, 110), title="Outcome labels mature later")
    ax_brier = axes[2].twinx()
    ax_brier.plot(weeks, brier, marker="o", color=GOLD, linewidth=1.8, label="Brier score")
    ax_brier.set(ylabel="Brier", ylim=(0.18, 0.24))
    handles = [axes[2].patches[0], ax_brier.lines[0]]
    axes[2].legend(handles, ["label-join coverage", "Brier when coverage ≥ 80%"], frameon=False, ncol=2, loc="upper right")

    colors = {"ok": TEAL, "warning": GOLD, "critical": RED}
    for week, state in zip(weeks, states):
        axes[3].barh(0, 0.88, left=week - 0.44, color=colors[state], height=0.48)
    axes[3].text(8.55, 0.34, "INC-48-001 detected", color=RED, fontsize=7, weight="bold")
    axes[3].annotate("rollback", xy=(10, 0), xytext=(10, -0.34), ha="center", color=NAVY, fontsize=7,
                     arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1))
    axes[3].set(yticks=[], ylabel="State", ylim=(-0.48, 0.55), title="Actionable alert and incident response")
    axes[3].set(xlabel="Production cohort week", xticks=weeks, xlim=(0.45, 12.55))

    fig.suptitle("Monitoring connects changing signals to delayed evidence and owned action",
                 color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    save_figure(fig, "fig-48-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
