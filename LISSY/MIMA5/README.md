# LISSY/MIMA5/

## Purpose

MIMA5 (5-year Moving Average of Median Income) poverty rate analysis and visualizations. Contains LISSY job outputs computing poverty rates anchored to the 5-year moving average of median income, comparing DHI and MHI across countries.

## Contents

- `plotting_mima5_pr.py` - Generates 4 plots comparing poverty rates and MIMA5 trends
- `lissy_mima5_*.csv` - LISSY outputs (MIMA5-based poverty rates for DHI/MHI)
- `lissy_CPI_mima5_*.csv` - CPI-adjusted MIMA5 poverty rates
- `*.png` - Visualizations (poverty rates and MIMA5 time series)
- **OLD/** - Archived outputs from previous runs

## Quick start

**Generate plots from existing CSV files:**
```bash
cd LISSY/MIMA5
python plotting_mima5_pr.py
```

**Outputs:**
- `mima5_dhi_50pp_pr.png` - DHI poverty rate (50% of MIMA5)
- `mima5_mhi_50pp_pr.png` - MHI poverty rate (50% of MIMA5)
- `mima5_dhi.png` - MIMA5 DHI time series
- `mima5_mhi.png` - MIMA5 MHI time series
- CPI-adjusted variants: `CPI_mima5_*.png`

## Inputs Required

**LISSY job outputs** (must be generated separately on LISSY):
- `lissy_mima5_dhi_50pr.csv` - DHI poverty rate @ 50% MIMA5
- `lissy_mima5_mhi_50pr.csv` - MHI poverty rate @ 50% MIMA5
- `lissy_CPI_mima5_dhi_50pr.csv` - CPI-adjusted DHI
- `lissy_CPI_mima5_mhi_50pr.csv` - CPI-adjusted MHI

Run R/Stata jobs on LISSY to compute these (see `LISSY/Tutorial/` for syntax).

## Conventions

- CSV files use long format: `country, year, pr, mima5`
- Plots fix country colors: Canada (green), Germany (red), UK (orange), US (blue)
- Outputs are PNG format (300 DPI recommended for publication)

## Privacy & Secrets

Only aggregated poverty rates and medians are stored. **Do NOT commit LIS microdata.**

LISSY jobs must be submitted via the [LISSY web interface](https://www.lisdatacenter.org/data-access/lissy/) or email. See `LISSY/README.md` for registration.

## Related Folders

- **DART/MIMA/** - MIMA computation workflow (using DART tables, not LISSY microdata)
- **METIS-LIS/mima_indicator.md** - MIMA methodology documentation
- **compute_mima.py** (root) - Python MIMA workflow for DART data

## Maintainers

MIMA5 analysis for poverty persistence research using LIS microdata.
