# LISSY/DART_Validation

## Purpose

Validation scripts that compare LISSY remote-execution results with DART reference tables. Ensures consistency between LIS microdata analyses and published aggregated indicators.

## Quick Start

Run validation:
```bash
# Review validation methodology
cat LISSY/DART_Validation/R_code_steps.md

# Run Python validation script
python LISSY/DART_Validation/validate_lissy_vs_dart.py
```

## Contents

- `R_code_steps.md` — Step-by-step guide for R-based validation workflow
- `validate_lissy_vs_dart.py` — Python script comparing LISSY outputs with DART tables

## Conventions

- Validation should be run when DART tables are updated
- Requires LISSY access credentials (do not commit secrets)
- Document discrepancies in validation reports
- Expected minor differences due to rounding or methodology updates

## Maintainers

- @EEbrami
