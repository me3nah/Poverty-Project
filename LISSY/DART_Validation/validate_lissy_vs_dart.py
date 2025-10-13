import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import os

metrics = [
    {
        'name': 'dhi_median',
        'dart_file': 'dart-table_dhi_median.csv',
        'lissy_file': 'lissy_pop_median_dhi_ppp_median_85-21.csv',
        'dart_type': 'median',
        'lissy_col': 'median',
        'ylabel': 'Median DHI',
    },
    {
        'name': 'dhi_pr',
        'dart_file': 'dart-table_dhi_pr.csv',
        'lissy_file': 'lissy_pop_median_dhi_ppp_median_85-21.csv',
        'dart_type': 'pr',
        'lissy_col': 'pr',
        'ylabel': 'Poverty Rate DHI (pp)',
    },
    {
        'name': 'mhi_median',
        'dart_file': 'dart-table_mhi_median.csv',
        'lissy_file': 'lissy_pop_median_mhi_ppp_median_85-21.csv',
        'dart_type': 'median',
        'lissy_col': 'median',
        'ylabel': 'Median MHI',
    },
    {
        'name': 'mhi_pr',
        'dart_file': 'dart-table_mhi_pr.csv',
        'lissy_file': 'lissy_pop_median_mhi_ppp_median_85-21.csv',
        'dart_type': 'pr',
        'lissy_col': 'pr',
        'ylabel': 'Poverty Rate MHI (pp)',
    },
]

years = [str(y) for y in range(1985, 2022)]

def load_dart_table(path):
    dart = pd.read_csv(path)
    dart.columns = [c.strip() for c in dart.columns]
    if 'countries' in dart.columns:
        dart = dart.rename(columns={'countries': 'country'})
    dart['country'] = dart['country'].str.strip()
    return dart

def load_lissy_file(path):
    lissy = pd.read_csv(path)
    lissy['country'] = lissy['country'].str.strip()
    return lissy

def plot_comparison_all_countries(years, dart_data, lissy_data, metric, ylabel):
    plt.figure(figsize=(14,7))
    for country in dart_data:
        # DART line: background, thick and faded
        plt.plot(years, dart_data[country], color="#0072B2", linewidth=8, alpha=0.15, label=f'DART {country}')
        # LISSY line: thin, solid
        plt.plot(years, lissy_data[country], linewidth=2, alpha=1, label=f'LISSY {country}')
    plt.title(f"{ylabel}: LISSY vs DART (All Countries)")
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    fname = f"all_countries_{metric}_comparison.png".replace(" ", "_")
    plt.savefig(fname)
    plt.close()
    return fname

for metric in metrics:
    print(f"\nProcessing {metric['name']}...")
    dart = load_dart_table(metric['dart_file'])
    lissy = load_lissy_file(metric['lissy_file'])

    dart_data = {}
    lissy_data = {}

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
                    if pd.notnull(dart_val) and pd.notnull(lissy_val):
                        dart_vals.append(float(dart_val))
                        # If metric is a poverty rate, convert LISSY to percentage points
                        if metric['dart_type'] == 'pr':
                            lissy_vals.append(float(lissy_val) * 100)
                        else:
                            lissy_vals.append(float(lissy_val))
                        valid_years.append(int(year))
        # Only add if all years are present
        if dart_vals and lissy_vals and len(dart_vals) == len(years):
            dart_data[country] = dart_vals
            lissy_data[country] = lissy_vals

    if dart_data and lissy_data:
        cmp_plot = plot_comparison_all_countries(years, dart_data, lissy_data, metric['name'], metric['ylabel'])
        print(f"Saved {cmp_plot}")

print("\nAll done!")
