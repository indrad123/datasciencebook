"""Figure 44.2: class-associated terms from a training-only text model."""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure

COLORS = {"service": BLUE, "quality": RED, "finance": GOLD, "sales": TEAL}


def main():
    with (ROOT / "data/generated/ch44_sample.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    train = [r for r in rows if r["split"] == "train"]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)
    x = vectorizer.fit_transform([r["message_text"] for r in train])
    model = LogisticRegression(max_iter=1000, random_state=44).fit(x, [r["route_label"] for r in train])
    terms = np.asarray(vectorizer.get_feature_names_out())

    apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(7.4, 5.4))
    for ax, route, coefficients in zip(axes.flat, model.classes_, model.coef_):
        order = np.argsort(coefficients)[-5:]
        labels = terms[order]
        values = coefficients[order]
        y = np.arange(len(labels))
        ax.barh(y, values, color=COLORS[route])
        ax.set(yticks=y, yticklabels=labels, xlabel="one-vs-rest coefficient", title=route.capitalize())
        ax.axvline(0, color=NAVY, linewidth=0.8)
        ax.set_xlim(0, max(1.8, float(values.max()) * 1.12))
    fig.text(0.5, 0.03, "Associations describe this fitted model; they are not causal explanations.", ha="center", color=RED, fontsize=8, weight="bold")
    fig.suptitle("Terms associated with each message route", color=NAVY, weight="bold", fontsize=12)
    fig.tight_layout(rect=(0, 0.06, 1, 0.94))
    save_figure(fig, "fig-44-02", ROOT)
    plt.close(fig)


if __name__ == "__main__":
    main()
