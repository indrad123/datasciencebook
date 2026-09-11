"""Figure 28.2: prediction accuracy and cost-aware decision value."""
from pathlib import Path
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, apply_style, save_figure


def main():
    apply_style()
    rows = list(csv.DictReader((ROOT / "data/generated/ch28_sample.csv").open()))
    p = np.linspace(0, 1, 201)
    fig, ax = plt.subplots(figsize=(5.8, 3.6))
    ax.plot(p, 80*p, color=BLUE, lw=2.5, label="Standard: 80p")
    ax.axhline(12, color=GOLD, lw=2.5, label="Expedite: 12")
    ax.axvline(.15, color=RED, ls="--", lw=1.5)
    xs = [float(r["predicted_late_probability"]) for r in rows]
    ys = [min(float(r["expected_loss_standard"]), 12) for r in rows]
    colours = [RED if r["recommended_action"] == "expedite" else NAVY for r in rows]
    ax.scatter(xs, ys, c=colours, s=20, zorder=3, edgecolor="white", linewidth=.4)
    ax.annotate("Decision threshold\np = 12/80 = 0.15", xy=(.15, 12), xytext=(.28, 31),
                arrowprops=dict(arrowstyle="->", color=RED), color=RED, fontsize=8)
    ax.set(xlim=(0, 1), ylim=(0, 82), xlabel="Predicted probability of late arrival", ylabel="Expected loss (illustrative units)")
    ax.set_title("Choose the action with lower expected loss", color=NAVY, weight="bold")
    ax.legend(frameon=False, loc="upper left")
    ax.grid(alpha=.17)
    fig.tight_layout()
    save_figure(fig, "fig-28-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
