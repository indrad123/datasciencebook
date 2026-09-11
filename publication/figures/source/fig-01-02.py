"""Figure 1.2: measurement variation and reporting precision."""

from pathlib import Path
import csv
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from publication.figure_style import BLUE, GOLD, GREY, NAVY, apply_style, save_figure


def main() -> None:
    apply_style()
    data_path = ROOT / "data" / "generated" / "ch01_sample.csv"
    with data_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["pack_id"].replace("NRG-", "") for row in rows]
    values = [float(row["measured_mass_g"]) for row in rows]
    label = float(rows[0]["label_mass_g"])
    mean = sum(values) / len(values)

    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ax.axhline(label, color=GOLD, linewidth=1.5, linestyle="--", label=f"Label mass: {label:.1f} g")
    ax.plot(ids, values, color=BLUE, marker="o", linewidth=1.3, label="Measured mass")
    ax.axhline(mean, color=NAVY, linewidth=1.2, linestyle=":", label=f"Mean: {mean:.1f} g")
    for x, value in zip(ids, values):
        ax.annotate(f"{value:.1f}", (x, value), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=8)
    ax.set_ylim(84.55, 85.45)
    ax.set_xlabel("Pack identifier")
    ax.set_ylabel("Mass (g)")
    ax.set_title("Individual measurements vary around the labelled mass", color=NAVY, weight="bold")
    ax.grid(axis="y", color=GREY, alpha=0.18, linewidth=0.7)
    ax.legend(frameon=False, ncol=1, loc="lower right")
    fig.tight_layout()
    save_figure(fig, "fig-01-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
