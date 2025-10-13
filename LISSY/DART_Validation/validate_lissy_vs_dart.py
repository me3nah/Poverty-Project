import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import os

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
        'ylabel': 'Poverty Rate DHI (pp)',
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
        plt.plot(years, dart_data[country], color="#0072B2", linewidth=8, alpha=0.12)
        # LISSY line: thin, solid
        plt.plot(years, lissy_data[country], linewidth=2, alpha=1, label=f"LISSY {country}")
    plt.title(f"{ylabel}: LISSY vs DART (All Countries)")
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend(loc="best", fontsize="small")
    plt.tight_layout()
    fname = f"all_countries_{metric}_comparison.png".replace(" ", "_")
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

def get_error_moments(errors):
    return {
        "mean": errors.mean(),
        "variance": errors.var(),
        "skewness": skew(errors),
        "kurtosis": kurtosis(errors),
        "min": errors.min(),
        "max": errors.max(),
        "count": errors.count()
    }

for metric in metrics:
    print(f"\nProcessing {metric['name']}...")
    dart = load_dart_table(metric['dart_file'])
    lissy = load_lissy_file(metric['lissy_file'])

    # Get the intersection of countries in both datasets
    dart_countries = set(dart['country'].unique())
    lissy_countries = set(lissy['country'].unique())
    countries = sorted(list(dart_countries & lissy_countries))

    dart_data = {}
    lissy_data = {}
    error_moments_dict = {}

    for country in countries:
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
        if dart_vals and lissy_vals and len(dart_vals) == len(valid_years):
            dart_data[country] = dart_vals
            lissy_data[country] = lissy_vals
            # Calculate error distribution and moments
            dart_series = pd.Series(dart_vals, dtype=float)
            lissy_series = pd.Series(lissy_vals, dtype=float)
            abs_rel_error = (dart_series - lissy_series).abs() / dart_series.abs()
            error_moments = get_error_moments(abs_rel_error)
            error_moments_dict[country] = error_moments
            # Save error distribution plot
            plot_error_distribution(abs_rel_error, country, metric['name'], metric['ylabel'])
            # Save txt file for this country
            txt_fname = f"{country}_{metric['name']}_error_moments.txt".replace(" ", "_")
            with open(txt_fname, "w") as f:
                for k, v in error_moments.items():
                    f.write(f"{k}: {v}\n")

    # Plot all countries on one compare graph
    if dart_data and lissy_data:
        cmp_plot = plot_comparison_all_countries(years, dart_data, lissy_data, metric['name'], metric['ylabel'])
        print(f"Saved {cmp_plot}")

    # Save CSV of error moments (moments x countries)
    error_moments_df = pd.DataFrame(error_moments_dict).T.transpose()
    error_moments_csv = f"{metric['name']}_error_moments_by_country.csv"
    error_moments_df.to_csv(error_moments_csv)
    print(f"Saved {error_moments_csv}")

print("\nAll done!")
