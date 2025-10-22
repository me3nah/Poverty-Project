# xlsxFiles

## Purpose

Source Excel files containing DART tables, LIS documentation, and variable definitions. These are the authoritative source files that feed into conversion pipelines.

## Quick Start

Convert all Excel files to multiple formats:
```bash
python convert_excel.py
```

View available files:
```bash
ls -lh xlsxFiles/
```

## Contents

- `dart-med-*.xlsx` — DART median income tables by demographic decomposition (DHI, MHI, MHIT)
  - Population, household type, homeownership, income decile, urban/rural breakdowns
- `our-lis-documentation*.xlsx` — LIS dataset documentation and availability matrices
- `variables-definition*.xlsx` — Variable definitions and ID mappings
- `codebook.xlsx` — LIS variable codebook (source for PDF version)

## Conventions

- Excel files are source data; do not edit manually without documenting changes
- Use `convert_excel.py` to generate CSV/JSON/MD outputs in `xlsxConverted/`
- Large Excel files are tracked in git; avoid adding very large binaries without need
- File naming follows pattern: `dart-med-{decomp}_{income-type}.xlsx`

## Maintainers

- @EEbrami
