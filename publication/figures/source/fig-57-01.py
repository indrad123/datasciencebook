"""Figure 57.1: modality-specific architecture and validation matrix."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import LIGHT_BLUE, LIGHT_GOLD, NAVY, TEAL, apply_style, save_figure


def wrap(text, width):
    words = text.split()
    lines, current = [], []
    for word in words:
        if len(" ".join(current + [word])) > width and current:
            lines.append(" ".join(current)); current = [word]
        else:
            current.append(word)
    lines.append(" ".join(current))
    return "\n".join(lines)


def main():
    with (ROOT / "data/generated/ch57_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    apply_style()
    fig, ax = plt.subplots(figsize=(8.1, 5.0))
    ax.axis("off")
    headers = ["Modality and unit", "Strong baseline", "Neural candidate", "Leakage boundary", "Monitor and fallback"]
    x = [0.08, 1.65, 3.20, 4.78, 6.45]
    widths = [1.42, 1.38, 1.38, 1.48, 1.45]
    for xpos, width, header in zip(x, widths, headers):
        ax.add_patch(FancyBboxPatch((xpos, 4.25), width, 0.46, boxstyle="round,pad=0.02",
                                    facecolor=NAVY, edgecolor=NAVY))
        ax.text(xpos + width / 2, 4.48, header, ha="center", va="center",
                color="white", fontsize=6.7, weight="bold")
    for i, row in enumerate(rows):
        y = 3.25 - i * 1.02
        face = LIGHT_BLUE if i % 2 == 0 else LIGHT_GOLD
        values = [
            f'{row["modality"]}\n{wrap(row["data_unit"], 22)}',
            wrap(row["baseline_model"], 21),
            wrap(row["deep_model"], 21),
            wrap(row["leakage_control"], 25),
            wrap(row["monitoring_focus"] + "; fallback: " + row["missing_input_fallback"], 25),
        ]
        for xpos, width, value in zip(x, widths, values):
            ax.add_patch(FancyBboxPatch((xpos, y), width, 0.86, boxstyle="round,pad=0.02",
                                        facecolor=face, edgecolor=TEAL, linewidth=0.8))
            ax.text(xpos + width / 2, y + 0.43, value, ha="center", va="center",
                    color=NAVY, fontsize=5.75, weight="bold" if xpos == x[0] else "normal")
    ax.set(xlim=(0, 8), ylim=(0, 4.9))
    fig.suptitle("Architecture, splitting, monitoring, and fallback must follow the data modality",
                 color=NAVY, weight="bold", fontsize=11.5)
    fig.text(0.5, 0.025, "One uniform neural stack would erase important differences in structure and operational failure modes.",
             ha="center", color=NAVY, fontsize=7.2)
    fig.tight_layout(rect=(0, 0.05, 1, 0.92))
    save_figure(fig, "fig-57-01", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
