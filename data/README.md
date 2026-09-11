# Book datasets

This directory contains the datasets and data contracts used in *From Noodles to Neural Networks*.

## Availability rule

Every dataset used by a chapter, notebook, exercise, solution, table, or figure must be available in this repository, unless the item is generated entirely inside the relevant notebook from a clearly documented formula. In that case, the reusable generator must also be stored in the repository.

## Directory structure

```text
data/
  generated/          # Reader-ready synthetic chapter datasets
  dictionaries/       # Field definitions and NRG schemas
  manifests/          # Chapter mappings, provenance, licences, and checksums
```

The matching deterministic generators are stored in `scripts/data/`.

## Required documentation

Each released dataset must record:

- dataset identifier and version;
- chapters, notebooks, exercises, tables, and figures that use it;
- file format, row count, column count, and unit of observation;
- field-level definitions and units;
- missing-value and category conventions;
- synthetic, derived, or external status;
- generator script and random seed for synthetic data;
- source, licence, and permitted redistribution for external data;
- integrity checksum; and
- known limitations and appropriate uses.

## NRG data statement

Nusantara Rasa Global is fictional. NRG datasets are synthetic and do not describe a real company, person, country, customer, supplier, or market. They are created only for education and reproducible examples.

Monetary fields for NRG use IDR or kIDR as declared in the relevant data dictionary. A field must not be interpreted without checking its recorded unit.

## Reader workflow

Readers should be able to clone the repository, install the documented environment, and run each notebook without manually downloading an undocumented file or changing an absolute file path.
