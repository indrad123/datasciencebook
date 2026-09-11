"""Figure 28.1: distinguish explanation, inference, prediction, and decisions."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    apply_style()
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    ax.axis("off")
    panels = [
        (0.06, 0.55, "EXPLANATION", "Why does delay occur?", "Causal effect\n+ assumptions", BLUE),
        (0.53, 0.55, "INFERENCE", "What is the population rate?", "Estimate\n+ uncertainty", TEAL),
        (0.06, 0.10, "PREDICTION", "Which shipment will be late?", "Future-case score\n+ test performance", GOLD),
        (0.53, 0.10, "DECISION", "Which shipment should we expedite?", "Action\n+ costs + constraints", RED),
    ]
    for x, y, heading, question, evidence, colour in panels:
        ax.add_patch(plt.Rectangle((x, y), .40, .32, facecolor="white", edgecolor=colour, linewidth=2))
        ax.text(x+.02, y+.25, heading, color=colour, weight="bold", fontsize=9)
        ax.text(x+.02, y+.16, question, color=NAVY, fontsize=8)
        ax.text(x+.02, y+.04, evidence, color=NAVY, fontsize=7)
    ax.text(.5, .96, "One situation, four different analytical purposes", ha="center", color=NAVY, weight="bold", fontsize=12)
    ax.text(.5, .02, "Shared data do not make the targets or evidence interchangeable", ha="center", color=NAVY, fontsize=8)
    fig.tight_layout()
    save_figure(fig, "fig-28-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
