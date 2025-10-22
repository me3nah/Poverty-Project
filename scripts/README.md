# scripts

## Purpose

Repository-wide utility scripts for data conversion and document processing. These scripts automate the conversion of Excel files to various formats and HTML documentation to Markdown.

## Quick Start

Convert all Excel files to CSV/JSON/MD:
```bash
python convert_excel.py
```

Convert HTML documentation to Markdown:
```bash
./scripts/convert-html-to-md.sh
```

## Contents

- `convert-html-to-md.sh` — Converts HTML files to Markdown format
  - Executable script using Pandoc or similar tools
  - Processes documentation from external sources

## Conventions

- Scripts run from repository root
- Conversion outputs go to `xlsxConverted/` directory
- Large generated files should be gitignored if not needed for review
- Ensure scripts are executable: `chmod +x scripts/*.sh`

## Maintainers

- @EEbrami
