# xlsxConverted/

## Purpose

Auto-generated output directory containing converted formats (CSV, JSON, Markdown) from Excel files in `xlsxFiles/`.

## Contents

- **csvFiles/** - CSV format (for R/Python/Stata analysis)
- **jsonFiles/** - JSON format (for web/API consumption)
- **mdFiles/** - Markdown tables (for documentation)

## Quick start

**Regenerate all conversions:**
```bash
python convert_excel.py --input-dir xlsxFiles --output-dir xlsxConverted
```

Or trigger via GitHub Actions workflow: `.github/workflows/convert-excel.yml`

## Conventions

- **Do not edit files manually** - they are auto-generated
- Files mirror the structure and naming of source Excel files
- Outputs are committed to the repository for reproducibility

## Privacy & Secrets

No sensitive data - all files are derived from public LIS/DART tables.

## Regenerating Outputs

If source Excel files are updated:
1. Run `python convert_excel.py` locally, or
2. Trigger the GitHub Actions workflow manually via Actions tab

## Related Folders

- **xlsxFiles/** - Source Excel files
- **analysis/data-availability/** - Consumes CSV files from this folder
