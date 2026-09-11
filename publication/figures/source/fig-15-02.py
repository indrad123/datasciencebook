"""Figure 15.2: honest and truncated bar-chart baselines."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GREY, NAVY, RED, apply_style, save_figure


def main():
    apply_style(); labels = ["Region A", "Region B"]; values = [94, 100]
    fig, (a, b) = plt.subplots(1, 2, figsize=(5.2, 3.15))
    for ax, ylim, title, colour in [(a, (0, 110), "Clear: magnitude starts at zero", BLUE), (b, (90, 102), "Misleading: six-point gap enlarged", RED)]:
        bars = ax.bar(labels, values, color=colour, width=.58)
        ax.set_ylim(*ylim); ax.set_ylabel("On-time delivery rate (%)")
        ax.set_title(title, fontsize=8.5, color=NAVY, weight="bold")
        ax.grid(axis="y", color=GREY, alpha=.18)
        for bar, value in zip(bars, values): ax.text(bar.get_x()+bar.get_width()/2, value+.7 if ylim[0] == 0 else value+.15, f"{value}%", ha="center", fontsize=8, weight="bold", color=NAVY)
    fig.suptitle("Identical values can imply very different stories", color=NAVY, weight="bold", fontsize=11)
    fig.text(.5, .015, "Both panels show a 6 percentage-point difference; only the left preserves bar-length magnitude.", ha="center", fontsize=7, color=NAVY)
    fig.tight_layout(rect=(0,.05,1,.94)); save_figure(fig, "fig-15-02", ROOT); plt.close(fig)


if __name__ == "__main__": main()
