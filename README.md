# From Noodles to Neural Networks

Official reader companion for *From Noodles to Neural Networks: A Practical Data Science Handbook from Everyday Mathematics to Enterprise AI* by Indra Dewaji.

This repository provides the practical resources referenced in the book:

- Executable Jupyter notebooks
- Reusable Python modules
- Synthetic sample datasets and data dictionaries
- Reproducible dataset generators
- Exercises and supporting solutions
- Automated tests
- Selected instructional figures

The manuscript, publishing source files, KDP interiors, covers, proofs, and internal production records are not included.

## About the author

Indra Dewaji is an enterprise technology and transformation practitioner connecting architecture, delivery, governance, and business outcomes.

## Local setup

```bash
git clone https://github.com/indrad123/datasciencebook.git
cd datasciencebook
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
jupyter lab
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Repository layout

```text
data/
  generated/
  dictionaries/
  manifests/
notebooks/
src/datasciencebook/
tests/
exercises/
solutions/
publication/
  figure_manifest.csv
  figure_style.py
  figures/
    source/
    ebook/
```

## Data statement

Nusantara Rasa Global is fictional. Unless a resource explicitly identifies a public source, its data are synthetic and must not be interpreted as evidence about a real organisation, population, country, or market.

## Reproducibility

Synthetic-data generators use fixed instructional values or recorded random seeds. Notebooks identify their prerequisites and data sources. Reusable Python functions are supported by automated tests.

## Licences

Software source code is available under the Apache License 2.0. Educational content, explanatory prose, exercises, solutions, and original figures remain copyright © Indra Dewaji. See `CONTENT_LICENSE.md` for the precise boundary.

## Contributing and security

Read `CONTRIBUTING.md` before proposing a change. Report exposed credentials, personal data, or vulnerabilities privately as described in `SECURITY.md`.
