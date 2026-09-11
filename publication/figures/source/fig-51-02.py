"""Figure 51.2: identity, sigmoid, tanh, and ReLU activations."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))
from datasciencebook.forward_network import activation
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    z = np.linspace(-5, 5, 500)
    specs = [
        ("identity", BLUE, "unrestricted output", "$g(z)=z$"),
        ("sigmoid", TEAL, "range (0, 1)", r"$g(z)=1/(1+e^{-z})$"),
        ("tanh", GOLD, "range (−1, 1)", r"$g(z)=\tanh(z)$"),
        ("relu", RED, "zero below 0; linear above", "$g(z)=\\max(0,z)$"),
    ]
    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(7.6, 5.3), sharex=True)
    for ax, (kind, color, subtitle, formula) in zip(axes.flat, specs):
        ax.axhline(0, color=NAVY, linewidth=0.7, alpha=0.55)
        ax.axvline(0, color=NAVY, linewidth=0.7, alpha=0.55)
        ax.plot(z, activation(z, kind), color=color, linewidth=2.1)
        ax.set(title=f"{kind.capitalize()} — {subtitle}", xlim=(-5, 5))
        ax.text(0.04, 0.88, formula, transform=ax.transAxes, fontsize=8, color=NAVY)
        ax.grid(alpha=0.15)
    axes[0, 0].set_ylim(-5.2, 5.2)
    axes[0, 1].set_ylim(-0.08, 1.08)
    axes[1, 0].set_ylim(-1.15, 1.15)
    axes[1, 1].set_ylim(-0.25, 5.2)
    axes[0, 0].set_ylabel("Activation output")
    axes[1, 0].set_ylabel("Activation output")
    axes[1, 0].set_xlabel("Preactivation $z$")
    axes[1, 1].set_xlabel("Preactivation $z$")
    fig.suptitle("Activation choice sets the shape and range passed to the next layer",
                 color=NAVY, weight="bold", fontsize=12)
    fig.text(0.5, 0.025,
             "Nonlinearity prevents stacked dense layers from collapsing into one linear transformation.",
             ha="center", color=NAVY, fontsize=7.5)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93))
    save_figure(fig, "fig-51-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
