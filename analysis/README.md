# analysis

## Purpose

Cross-national poverty and data availability analyses using harmonized LIS microdata. Contains algorithms, visualizations, and reports for understanding country-year coverage patterns.

## Quick Start

Run data availability analysis:
```bash
cd analysis/data-availability
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Generate visualizations:
```bash
# Via GitHub Actions workflow or directly
python analysis/data-availability/visuals/generate_visuals.py \
  --csv-path xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv
```

## Contents

- `data-availability/` — Submatrix analysis and visualization tools (see [data-availability/README.md](data-availability/README.md))
  - Algorithms for finding optimal country-year coverage windows
  - Heatmap generation showing data availability patterns

## Conventions

- Each analysis subfolder should have its own README
- Install dependencies in virtual environments to avoid conflicts
- Generated outputs (JSON, CSV, figures) documented in subfolder READMEs
- Results that are too large should be gitignored with regeneration instructions

## Maintainers

- @EEbrami
