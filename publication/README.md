# Instructional figures

This directory contains the reproducible figure resources for *From Noodles to Neural Networks*.

## Contents

- `figure_manifest.csv`: figure identifiers, chapter mappings, captions, accessibility text, and production metadata
- `figure_style.py`: shared colour and typography settings
- `figures/source/`: Python source for all 122 figures
- `figures/ebook/`: 300 dpi PNG renders for all 122 figures

Figures 1.1 through 58.2 contain two figures per chapter. Chapter 59 contains six capstone figures.

## Regenerating a figure

Run a figure script from the repository root. For example:

```bash
python publication/figures/source/fig-59-01.py
```

The script writes a high-resolution PNG to `publication/figures/ebook/` and a vector PDF to `publication/figures/print/`. Print PDFs are production outputs and are intentionally excluded from Git.

## Publication boundary

The included figures support readers and reproducibility. KDP interiors, covers, proofs, and other publishing deliverables are not stored in this repository. Figure reuse is governed by `CONTENT_LICENSE.md`.
