# DART/

## Purpose

DART (Data Access in Real Time) validation, analysis, and visualization outputs from LIS Key Figures. Contains scripts for comparing LISSY microdata results with official DART tables and producing median income plots.

## Contents

- `dart_validation.py` - Validates LISSY results against DART median income tables
- `plot_dart_tables.py` - Generates visualizations from DART CSV tables
- `Methodological_Notes.md` - LIS Key Figures methodology (population coverage, income concepts, equivalence scales)
- `Methodological_Remarks.md` - Extended methodological documentation
- `dart-table_*.csv` - DART reference tables (DHI median, poverty rates)
- `dart_*_plot.png` - Generated visualizations
- **MIMA/** - Moving Average workflow (detailed README inside)

## Quick start

**Validate LISSY vs DART:**
```bash
python DART/dart_validation.py
# Outputs: dart_dhi_median_validation.csv, dart_dhi_median_error_facts.txt
```

**Plot DART tables:**
```bash
python DART/plot_dart_tables.py
# Outputs: PNG plots in DART/
```

**Run MIMA workflow:**
```bash
python compute_mima.py \
  --ma-number 5 \
  --countries "Canada,Germany,Luxembourg,United Kingdom,United States" \
  --start-year 1985 --end-year 2021 \
  --input-path "xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv" \
  --output-path "DART"
# Outputs: DART/MIMA/csv/ and DART/MIMA/visualizations/
```

See `DART/MIMA/README.md` for full MIMA documentation.

## Conventions

- CSV tables use countries as rows, years as columns
- Scripts run from repository root (not from DART/ directory)
- Validation scripts compare LISSY outputs to DART tables and report error statistics

## Privacy & Secrets

No microdata is stored here - only aggregated tables and validation outputs. LISSY jobs must be run separately on the LIS remote server.

## Related Folders

- **LISSY/DART_Validation/** - Alternative DART validation using R
- **xlsxConverted/csvFiles/** - Source DART tables in CSV format
- **compute_mima.py** (root) - MIMA computation script

## Maintainers

DART tables sourced from [LIS DART Portal](https://www.lisdatacenter.org/data-access/dart/).
