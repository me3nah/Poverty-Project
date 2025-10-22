# LISSY/MIMA5

## Purpose

LISSY-specific implementation and visualization scripts for MIMA (Median Income Moving Average) analysis with window size 5. Contains job submission templates and plotting utilities for remote-execution results.

## Quick Start

Generate MIMA5 plots from LISSY outputs:
```bash
python LISSY/MIMA5/plotting_mima5_pr.py
```

## Contents

- `plotting_mima5_pr.py` — Generate poverty rate plots from MIMA5 results
- `OLD/` — Archived scripts from earlier analysis phases

## Conventions

- LISSY jobs must be submitted via LISSY interface (see [LISSY/README.md](../README.md))
- Plotting scripts expect specific output format from LISSY jobs
- Do not commit LISSY credentials or raw microdata outputs
- Generated plots should be reviewed before committing

## Maintainers

- @EEbrami
