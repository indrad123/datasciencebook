"""Figure 15.1: match analytical questions to suitable displays."""
from pathlib import Path
import csv, sys
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, GREY, NAVY, RED, TEAL, apply_style, save_figure


def main():
    apply_style()
    rows = list(csv.DictReader((ROOT / "data/generated/ch15_sample.csv").open(encoding="utf-8")))
    counts = Counter(r["product_category"] for r in rows)
    ordered = sorted(counts, key=counts.get)
    days = np.array([int(r["delivery_days"]) for r in rows])
    daily = Counter(r["order_date"] for r in rows)
    dates = sorted(daily)
    fig, axes = plt.subplots(2, 2, figsize=(5.2, 4.0))
    a, b, c, d = axes.flat
    a.barh(ordered, [counts[x] for x in ordered], color=BLUE)
    a.set_title("Compare categories: bar chart", fontsize=8.5, color=NAVY, weight="bold")
    a.set_xlabel("Orders")
    bins = np.arange(.5, 10.5, 1)
    b.hist(days, bins=bins, color=TEAL, edgecolor="white")
    b.set_title("See numeric shape: histogram", fontsize=8.5, color=NAVY, weight="bold")
    b.set_xlabel("Delivery time (days)")
    x = np.sort(days); y = np.arange(1, len(x) + 1) / len(x)
    c.step(x, y, where="post", color=GOLD, lw=2)
    c.axvline(4, color=RED, ls="--", lw=1)
    c.set_ylim(0, 1.03); c.set_xlabel("Delivery time (days)"); c.set_ylabel("Cumulative share")
    c.set_title("Check a threshold: ECDF", fontsize=8.5, color=NAVY, weight="bold")
    day_numbers = [int(x[-2:]) for x in dates]
    d.plot(day_numbers, [daily[x] for x in dates], marker="o", ms=3, color=BLUE)
    d.set_xlim(1, 30); d.set_xlabel("Day in April 2026"); d.set_ylabel("Orders")
    d.set_title("Follow ordered change: line chart", fontsize=8.5, color=NAVY, weight="bold")
    for ax in axes.flat: ax.grid(color=GREY, alpha=.16)
    fig.suptitle("The question and variable type determine the display", color=NAVY, weight="bold", fontsize=11)
    fig.tight_layout(); save_figure(fig, "fig-15-01", ROOT); plt.close(fig)


if __name__ == "__main__": main()
