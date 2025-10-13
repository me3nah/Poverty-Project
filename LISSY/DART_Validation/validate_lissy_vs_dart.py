import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import os

# ---- CONFIG ----
metrics = [
    {
        'name': 'dhi_median',
        'dart_file': 'dart_table_dhi_median.csv',
        'lissy_file': 'lissy_pop_median_dhi_ppp_median_85-21.csv',
        'dart_type': 'median',
        'lissy_col': 'median',
        'ylabel': 'Median DHI',
    },
    {
        'name': 'dhi_pr',
        'dart_file': 'dart_table_dhi_pr.csv',
        'lissy_file': 'lissy_pop_median_dhi_ppp_median_85-21.csv',
        'dart_type': 'pr',
        'lissy_col': 'pr',
        'ylabel': 'Poverty Rate DHI',
    },
    {
        'name': 'mhi_median',
        'dart_file': 'dart_table_mhi_median.csv',
        'lissy_file': 'lissy_pop_median_mhi_ppp_median_85-21.csv',
        'dart_type': 'median',
        'lissy_col': 'median',
        'ylabel': 'Median MHI',
    },
    {
        'name': 'mhi_pr',
        'dart_file': 'dart_table_mhi_pr.csv',
        'lissy_file': 'lissy_pop_median_mhi_ppp_median_85-21.csv',
        'dart_type': 'pr',
        'lissy_col': 'pr',
        'ylabel': 'Poverty Rate MHI',
    },
]

years = [str(y) for y in range(1985, 2022)]

def load_dart_table(path):
    """Load a DART table (wide format) and clean country names."""
    dart = pd.read_csv(path)
    dart.columns = [c.strip() for c in dart.columns]
    if 'countries' in dart.columns:
        dart = dart.rename(columns={'countries': 'country'})
    dart['country'] = dart['country'].str.strip()
    return dart

def load_lissy_file(path):
    """Load a LISSY file (long format) and clean country names."""
    lissy = pd.read_csv(path)
    lissy['country'] = lissy['country'].str.strip()
    return lissy

def plot_comparison(years, dart_vals, lissy_vals, country, metric, ylabel):
    plt.figure(figsize=(10,5))
    plt.plot(years, dart_vals, color="#0072B2", linewidth=4, alpha=0.25, label='DART (Benchmark)')
    plt.plot(years, lissy_vals, color="#0072B2", linewidth=1.5, alpha=1, label='LISSY (Extracted)')
    plt.title(f"{ylabel} for {country}: LISSY vs DART")
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    fname = f"{country}_{metric}_comparison.png".replace(" ", "_")
    plt.savefig(fname)
    plt.close()
    return fname

def plot_error_distribution(errors, country, metric, ylabel):
    plt.figure(figsize=(7,4))
    sns.histplot(errors, bins=15, color="#0072B2", kde=True)
    plt.title(f"Absolute Relative Error Distribution: {ylabel} for {country}")
    plt.xlabel("Absolute Relative Error")
    plt.ylabel("Frequency")
    plt.tight_layout()
    err_fname = f"{country}_{metric}_error_dist.png".replace(" ", "_")
    plt.savefig(err_fname)
    plt.close()
    return err_fname

def save_moments(errors, country, metric):
    moments = {
        "mean": errors.mean(),
        "variance": errors.var(),
        "skewness": skew(errors),
        "kurtosis": kurtosis(errors),
        "min": errors.min(),
        "max": errors.max(),
        "count": errors.count()
    }
    txt_fname = f"{country}_{metric}_error_moments.txt".replace(" ", "_")
    with open(txt_fname, "w") as f:
        for k, v in moments.items():
            f.write(f"{k}: {v}\n")
    return txt_fname

for metric in metrics:
    print(f"\nProcessing {metric['name']}...")
    dart = load_dart_table(metric['dart_file'])
    lissy = load_lissy_file(metric['lissy_file'])

    for country in dart['country'].unique():
        dart_row = dart[dart['country'] == country]
        lissy_rows = lissy[lissy['country'] == country]
        dart_vals = []
        lissy_vals = []
        valid_years = []
        for year in years:
            if year in dart_row.columns:
                dart_val = dart_row[year].values[0]
                lissy_row = lissy_rows[lissy_rows['year'] == int(year)]
                if not lissy_row.empty:
                    lissy_val = lissy_row[metric['lissy_col']].values[0]
                    # Only add if both values are numbers
                    if pd.notnull(dart_val) and pd.notnull(lissy_val):
                        dart_vals.append(float(dart_val))
                        lissy_vals.append(float(lissy_val))
                        valid_years.append(int(year))
        if not dart_vals or not lissy_vals:
            print(f"Skipping {country} for {metric['name']} (no overlap)")
            continue

        # Plot comparison
        cmp_plot = plot_comparison(valid_years, dart_vals, lissy_vals, country, metric['name'], metric['ylabel'])

        # Error distribution
        dart_series = pd.Series(dart_vals, dtype=float)
        lissy_series = pd.Series(lissy_vals, dtype=float)
        abs_rel_error = (dart_series - lissy_series).abs() / dart_series.abs()
        err_plot = plot_error_distribution(abs_rel_error, country, metric['name'], metric['ylabel'])

        # Save moments
        moments_txt = save_moments(abs_rel_error, country, metric['name'])

        print(f"Saved {cmp_plot}, {err_plot}, {moments_txt}")

print("\nAll done!")
