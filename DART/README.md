# DART (Data Analysis & Reproducibility Toolkit)

## Purpose

Shared analysis utilities, validation/preprocessing scripts, and methodological notes for income and poverty analyses using LIS microdata. This folder contains validation outputs, comparison tables, and visualizations that ensure data quality and reproducibility.

## Quick Start

Validate DART tables against LIS data:
```bash
python DART/dart_validation.py
```

Generate plots from DART tables:
```bash
python DART/plot_dart_tables.py
```

## Contents

- `MIMA/` — Median Income Moving Average workflow (see [MIMA/README.md](MIMA/README.md))
- `Methodological_Notes.md` — Core methodological documentation
- `Methodological_Remarks.md` — Additional methodology details
- `dart_validation.py` — Validation script comparing DART outputs with source data
- `plot_dart_tables.py` — Visualization generation for DART tables
- `dart-table_*.csv` — Validation reference tables (median DHI, poverty rates)
- `dart_*_validation.csv` — Detailed validation results
- `*.png` — Generated visualizations (median income, poverty rates by country)

## Conventions

- Validation outputs are committed to track data quality over time
- Large PNG files (>100KB) are tracked but should be regenerated if source data changes
- All validation scripts expect input from `xlsxConverted/csvFiles/`
- Python dependencies: `pandas`, `numpy`, `matplotlib`

## Maintainers

- @EEbrami
