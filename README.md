# From Noodles to Neural Networks

Official reader companion for *From Noodles to Neural Networks: A Practical Data Science Handbook from Everyday Mathematics to Enterprise AI* by Indra Dewaji.

This repository contains the practical resources referenced in the book:

- 59 executable chapter notebooks and 7 executable appendix notebooks
- reusable Python modules with automated tests
- synthetic sample datasets, data dictionaries, and deterministic generators
- chapter and appendix exercises with supporting solutions
- 122 reproducible instructional figures rendered for eBook use

The manuscript, KDP interiors, covers, proofs, and internal production records are not included.

## Start here

```bash
git clone https://github.com/indrad123/datasciencebook.git
cd datasciencebook
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
pytest
jupyter lab
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Open the notebook that matches the chapter you are reading. Paths use the book's part and chapter numbering. Some book parts contain no executable companion item, so directory numbers intentionally follow the book rather than forming an uninterrupted sequence.

## Repository guide

| Path | Purpose |
|---|---|
| `notebooks/` | Executable chapter and appendix walkthroughs |
| `data/generated/` | Reader-ready synthetic CSV files |
| `data/dictionaries/` | Field definitions and data contracts |
| `data/manifests/` | Dataset provenance, integrity, and chapter mappings |
| `scripts/data/` | Deterministic dataset generators |
| `src/datasciencebook/` | Reusable instructional Python functions |
| `tests/` | Automated checks for reusable functions |
| `exercises/` | Chapter and appendix questions |
| `solutions/` | Supporting solutions |
| `publication/` | Figure manifest, source scripts, style, and eBook renders |

For figure-specific instructions, see `publication/README.md`. For dataset rules and limitations, see `data/README.md`.

## Data statement

Nusantara Rasa Global is fictional. Unless a resource explicitly identifies a public source, its data are synthetic and must not be interpreted as evidence about a real organisation, population, country, or market.

Monetary examples for the Jakarta-based company use IDR or kIDR unless a chapter explicitly explains another unit.

## Reproducibility

Synthetic-data generators use fixed instructional values or recorded random seeds. Notebooks identify their prerequisites and data sources. Reusable Python functions are supported by automated tests.

Before reporting an issue, run `pytest` from the repository root and record the notebook or script path involved.

## Licences

Software source code is available under the Apache License 2.0. Educational content, explanatory prose, exercises, solutions, and original figures remain copyright © Indra Dewaji. See `CONTENT_LICENSE.md` for the precise boundary.

## Contributing and security

Read `CONTRIBUTING.md` before proposing a change. Report exposed credentials, personal data, or vulnerabilities privately as described in `SECURITY.md`.
