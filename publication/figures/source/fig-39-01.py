"""Figure 39.1: distributor segments and centroids."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure

COLORS = {"steady_bulk": BLUE, "frequent_broad_mix": TEAL, "campaign_specialist": RED}
LABELS = {"steady_bulk": "steady bulk", "frequent_broad_mix": "frequent broad mix", "campaign_specialist": "campaign specialist"}


def main():
    with (ROOT / "data/generated/ch39_sample.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    for group, color in COLORS.items():
        subset = [r for r in rows if r["assigned_cluster"] == group]
        x = [float(r["orders_scaled"]) for r in subset]
        y = [float(r["mix_scaled"]) for r in subset]
        ax.scatter(x, y, s=34, color=color, alpha=0.88, label=LABELS[group])
        cx = float(subset[0]["centroid_orders_scaled"])
        cy = float(subset[0]["centroid_mix_scaled"])
        ax.scatter(cx, cy, marker="X", s=180, color=GOLD, edgecolor=NAVY, linewidth=1.2, zorder=5)
        ax.add_patch(Circle((cx, cy), 0.38, fill=False, color=color, ls="--", lw=1.1))
    label_positions = {
        "steady_bulk": (-1.53, 1.17),
        "frequent_broad_mix": (0.69, 1.27),
        "campaign_specialist": (-0.35, -0.76),
    }
    for group, (lx, ly) in label_positions.items():
        ax.text(lx, ly, LABELS[group], fontsize=8, weight="bold", color=NAVY,
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.82, pad=1.5))
    ax.set(xlabel="Ordering frequency (scaled)", ylabel="Broad product mix (scaled)", xlim=(-1.65, 1.55), ylim=(-1.55, 1.35))
    ax.set_title("A three-cluster partition reflects the chosen representation", color=NAVY, weight="bold")
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    fig.text(0.5, 0.02, "Gold X = centroid  ·  dashed circles aid comparison; they are not decision boundaries", ha="center", fontsize=7, color=NAVY)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    save_figure(fig, "fig-39-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
