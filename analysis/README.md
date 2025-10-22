# analysis/

## Purpose

Parent folder for analytical pipelines and research modules. Each subfolder contains a self-contained analysis with its own README, requirements, and outputs.

## Contents

- **data-availability/** - Submatrix analysis finding optimal country-year panels in OECD income data

## Quick start

Navigate to specific analysis folders for detailed instructions:

```bash
# Run data availability analysis
cd analysis/data-availability
python run.py
```

See individual folder READMEs for requirements, inputs, and outputs.

## Conventions

- Each analysis subfolder is **self-contained** with its own `requirements.txt`
- Analysis scripts run from the **repository root** (not from analysis/)
- Use Python virtual environments to isolate dependencies
- Large outputs (plots, JSON results) may be gitignored - check folder READMEs for regeneration steps

## Adding New Analyses

1. Create subfolder: `analysis/my-analysis/`
2. Add `README.md` documenting purpose, inputs, outputs, and commands
3. Add `requirements.txt` if Python dependencies are needed
4. Include example run command in README
5. Update this parent README to list the new analysis

## Related Folders

- **xlsxConverted/csvFiles/** - Common input source for many analyses
- **DART/** - DART-specific analysis and validation
