# xlsxConverted

## Purpose

Machine-readable outputs generated from Excel source files in `xlsxFiles/`. Contains CSV for data analysis, JSON for programmatic access, and Markdown for documentation.

## Quick Start

Regenerate all converted files:
```bash
python convert_excel.py
```

Access converted data:
```bash
# CSV files for analysis
ls xlsxConverted/csvFiles/

# JSON files for API/programmatic use
ls xlsxConverted/jsonFiles/

# Markdown files for documentation
ls xlsxConverted/mdFiles/
```

## Contents

- `csvFiles/` — CSV format, suitable for pandas, R, statistical analysis
- `jsonFiles/` — JSON format, suitable for web applications and APIs
- `mdFiles/` — Markdown tables for documentation and review

## Conventions

- **Do not edit manually** — files are auto-generated from `xlsxFiles/`
- Regenerate after any changes to source Excel files
- Some outputs may be gitignored if very large (see `.gitignore`)
- CSV files follow naming: `{source-stem}.csv`

## Maintainers

- @EEbrami
