"""Shared publication styling for print and eBook figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl


NAVY = "#17324D"
BLUE = "#2E6F9E"
TEAL = "#2A7F7F"
GOLD = "#C58B2A"
RED = "#A64B3C"
LIGHT_BLUE = "#DCEAF3"
LIGHT_GOLD = "#F3E8D0"
GREY = "#5C6770"
LIGHT_GREY = "#E8ECEF"


def apply_style() -> None:
    """Apply a restrained style that remains legible in grayscale."""
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 9,
            "axes.edgecolor": GREY,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "savefig.bbox": "tight",
        }
    )


def save_figure(fig, figure_id: str, root: Path) -> tuple[Path, Path]:
    """Save vector print and high-resolution eBook versions."""
    print_path = root / "publication" / "figures" / "print" / f"{figure_id}.pdf"
    ebook_path = root / "publication" / "figures" / "ebook" / f"{figure_id}.png"
    print_path.parent.mkdir(parents=True, exist_ok=True)
    ebook_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(print_path)
    fig.savefig(ebook_path, dpi=300)
    return print_path, ebook_path

