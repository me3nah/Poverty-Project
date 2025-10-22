# Data Availability Submatrix Analysis

This module analyzes the OECD income dataset to find large all-ones submatrices within the country-by-year availability matrix (1 if income is present for a country in a year; 0 otherwise).

It implements several algorithms:
- Greedy longest-streak intersection (Phase 1 and Phase 2 as specified)
- Coverage-based pivot shrink (practical variant that records all countries covering the pivot)
- Best consecutive-year window
- Fixed 2- and 3-year window variants (including offset restrictions)
- Max biclique (arbitrary years, exact, with time limit + pruning)

## Input

- CSV: xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv
- Column "countries" for country names; remaining columns are expected to be 4-digit years.

## Output

Each algorithm writes a JSON file in analysis/data-availability/results/ with:
- num_countries: int
- length: int (number of years in the partition)
- partition: list of years
- period: [start_year, end_year] (when consecutive)
- countries: list of countries

For algorithms that may produce multiple rows (greedy variants), an extra CSV is written per algorithm to:
- analysis/data-availability/results/multiple-rows/
with columns:
- row_index, num_countries, length, period_start, period_end, partition_years (semicolon-delimited), countries (semicolon-delimited)

A consolidated summary is generated at:
- analysis/data-availability/summary.md

## Quick start

From repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r analysis/data-availability/requirements.txt
python analysis/data-availability/run.py
```

**Outputs** (gitignored - regenerate locally):
- `analysis/data-availability/results/*.json` - Algorithm results
- `analysis/data-availability/results/multiple-rows/*.csv` - Multi-row algorithm outputs
- `analysis/data-availability/summary.md` - Consolidated summary

**GitHub Actions:** Workflow available at `.github/workflows/data-availability-analysis.yml`

## Algorithms

- **Greedy longest-streak (Phase 1):** Sort countries by longest consecutive-ones streak. Start with largest and collect matching countries. On mismatch, record row and shrink. Phase 2 repeats with Phase 1 first-row countries removed.
- **Greedy pivot coverage:** Same mechanics, but records all countries covering the pivot interval (not just those with matching longest streak).
- **Best consecutive window:** Searches all year intervals `[l, r]` for maximum country coverage (ties broken by longer interval).
- **Fixed L-year windows:** Best L-year moving window; offset-restricted variants limit start positions.
- **Max biclique:** Exact backtracking search for arbitrary year sets maximizing `num_countries × length` (time-limited with pruning).

## Conventions

- Input CSV must have `countries` column + year columns (4-digit years)
- Outputs are JSON/CSV format
- Large result files are gitignored (see `.gitignore`)

## Privacy & Secrets

No sensitive data - analysis uses publicly available DART aggregated tables.

## Maintainers

Analytical module for finding optimal cross-country longitudinal panels.
