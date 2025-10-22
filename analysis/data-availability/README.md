# Data Availability Analysis

## Purpose

Analyzes country-by-year availability matrices to identify optimal subsets of countries and years with complete data coverage. Implements multiple algorithms for finding large complete submatrices, supporting cross-national research design decisions.

## Quick Start

Run all analysis algorithms:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Review consolidated results:
```bash
cat summary.md
```

## Input

- **CSV**: `xlsxConverted/csvFiles/dart-med-pop_decomp-dhi.csv`
- **Format**: Column `countries` for country names; remaining columns are 4-digit years
- **Values**: Numeric data indicates availability; NaN/missing indicates unavailability

## Output

Results written to `results/`:
- Individual JSON files per algorithm with best submatrix found
- CSV files in `results/multiple-rows/` for algorithms yielding multiple solutions
- `summary.md` — Consolidated summary comparing all algorithms

Each JSON result contains:
- `num_countries`, `length`, `partition`, `period`, `countries`

## Algorithms

Six complementary algorithms find different optimal submatrices:

1. **Greedy Longest-Streak (Phase 1 & 2)** — Iteratively finds countries sharing longest consecutive availability
2. **Greedy Pivot Coverage** — Identifies all countries fully covering each pivot interval
3. **Best Consecutive Window** — Exhaustive search over all year ranges for maximum country count
4. **Fixed L-Year Windows** — Moving window optimization for L=2 or L=3 years
5. **Offset-Restricted Windows** — Constrained window positions (e.g., every 5 years)
6. **Max Biclique** — Exact backtracking for maximum area submatrix (countries × years)

## Conventions

- Generated JSON/CSV files in `results/` are gitignored (see root `.gitignore`)
- Summary file `summary.md` is gitignored
- Regenerate results after input data updates
- Algorithms use heuristics and pruning for computational tractability

## Maintainers

- @EEbrami
