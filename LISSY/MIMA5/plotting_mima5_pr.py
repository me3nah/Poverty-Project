#!/usr/bin/env python3
"""
plot_lissy_mima5.py

Reads the two CSV files in the current working directory:
 - lissy_mima5_dhi_50pr.csv
 - lissy_mima5_mhi_50pr.csv

Creates 4 plots (each plot contains the 4 countries in the same axis):
  1) Poverty rate (pr) for dhi  (saved as pr_mima5_dhi_50pp.png)
  2) Poverty rate (pr) for mhi  (saved as pr_mima5_mhi_50pp.png)
  3) mima5_dhi over time       (saved as mima5_dhi.png)
  4) mima5_mhi over time       (saved as mima5_mhi.png)

Assumes you run the script in the folder that contains the two CSV files
(i.e., the script uses the current working directory).

Country colors (fixed):
 - Canada: green
 - Germany: red
 - United Kingdom: orange
 - United States: blue

Usage:
  python plot_lissy_mima5.py
"""
from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Filenames expected in the current working directory
FILE_DHI = Path("lissy_mima5_dhi_50pr.csv")
FILE_MHI = Path("lissy_mima5_mhi_50pr.csv")

# Output filenames (as requested)
OUT_PR_DHI = "pr_mima5_dhi_50pp.png"
OUT_PR_MHI = "pr_mima5_mhi_50pp.png"
OUT_MIMA5_DHI = "mima5_dhi.png"
OUT_MIMA5_MHI = "mima5_mhi.png"

# Countries and explicit colors
COUNTRIES = ["Canada", "Germany", "United Kingdom", "United States"]
COLORS = {
    "Canada": "green",
    "Germany": "red",
    "United Kingdom": "orange",
    "United States": "blue",
}

def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    # Read robustly: the CSVs use commas and quotes
    df = pd.read_csv(path, quotechar='"', skipinitialspace=True)
    # Ensure year numeric
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    return df

def find_mima5_col(df: pd.DataFrame) -> str:
    # Find a column that starts with "mima5_"
    for c in df.columns:
        if isinstance(c, str) and c.startswith("mima5_"):
            return c
    raise KeyError("No column starting with 'mima5_' found in dataframe")

def plot_pr(df: pd.DataFrame, outfile: str, label: str):
    if "pr" not in df.columns:
        raise KeyError(f"'pr' column not found in {label}")
    plt.figure(figsize=(10, 6))
    for country in COUNTRIES:
        sub = df[df["country"] == country].sort_values("year")
        if sub.empty:
            print(f"Warning: no data for {country} in {label}")
            continue
        # Convert decimal share to percentage points
        plt.plot(sub["year"], sub["pr"] * 100, marker="o", color=COLORS.get(country), label=country)
    plt.xlabel("Year")
    plt.ylabel("Poverty rate (percentage points)")
    plt.title(f"Poverty rate (pr) — {label}")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=100.0))
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile, dpi=150)
    plt.close()
    print(f"Saved {outfile}")

def plot_mima5(df: pd.DataFrame, col: str, outfile: str, label: str):
    if col not in df.columns:
        raise KeyError(f"Column {col} not found in {label}")
    plt.figure(figsize=(10, 6))
    for country in COUNTRIES:
        sub = df[df["country"] == country].sort_values("year")
        if sub.empty:
            print(f"Warning: no data for {country} in {label}")
            continue
        plt.plot(sub["year"], sub[col], marker="o", color=COLORS.get(country), label=country)
    plt.xlabel("Year")
    plt.ylabel(f"{col}")
    plt.title(f"{col} over time — {label}")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile, dpi=150)
    plt.close()
    print(f"Saved {outfile}")

def main():
    print("Working directory:", Path.cwd())
    try:
        df_dhi = read_csv(FILE_DHI)
    except Exception as e:
        print("Error reading dhi CSV:", e)
        sys.exit(1)

    try:
        df_mhi = read_csv(FILE_MHI)
    except Exception as e:
        print("Error reading mhi CSV:", e)
        sys.exit(1)

    # Basic sanity check
    for name, df in [("dhi", df_dhi), ("mhi", df_mhi)]:
        if "country" not in df.columns or "year" not in df.columns:
            print(f"Error: {name} file missing 'country' or 'year' columns.")
            sys.exit(1)

    # Plot poverty rates (pr) -> saved as percentage points files requested
    try:
        plot_pr(df_dhi, OUT_PR_DHI, "dhi")
    except Exception as e:
        print("Failed to plot pr for dhi:", e)

    try:
        plot_pr(df_mhi, OUT_PR_MHI, "mhi")
    except Exception as e:
        print("Failed to plot pr for mhi:", e)

    # Plot mima5_* columns
    try:
        mima5_col_dhi = find_mima5_col(df_dhi)
        plot_mima5(df_dhi, mima5_col_dhi, OUT_MIMA5_DHI, "dhi")
    except Exception as e:
        print("Failed to plot mima5 for dhi:", e)

    try:
        mima5_col_mhi = find_mima5_col(df_mhi)
        plot_mima5(df_mhi, mima5_col_mhi, OUT_MIMA5_MHI, "mhi")
    except Exception as e:
        print("Failed to plot mima5 for mhi:", e)

if __name__ == "__main__":
    main()
