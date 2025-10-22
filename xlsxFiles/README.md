# xlsxFiles/

## Purpose

Source data files in Excel format (`.xlsx`) used as input for analysis workflows and conversion pipelines.

## Contents

- `dart-*.xlsx` - DART median income tables by decomposition type (DHI, MHI, MHIT) and category (population, household type, urban/rural, etc.)
- `codebook.xlsx` - Variable definitions and metadata
- `our-lis-documentation*.xlsx` - LIS dataset documentation and availability matrices
- `variables-definition*.xlsx` - Variable mappings and definitions

## Quick start

These files are **read-only inputs**. Do not modify directly.

**Convert to CSV/JSON/MD:**
```bash
python convert_excel.py --input xlsxFiles/<filename>.xlsx --output xlsxConverted
```

Or use the automated workflow (`.github/workflows/convert-excel.yml`).

## Conventions

- Files are version-controlled (committed to repo)
- Use descriptive naming: `<source>-<category>_<type>-<income-concept>.xlsx`
- Large Excel files (>100MB) should be excluded via `.gitignore`

## Related Folders

- **xlsxConverted/** - Generated outputs (CSV, JSON, Markdown)
- **DART/** - Analysis using these data files
