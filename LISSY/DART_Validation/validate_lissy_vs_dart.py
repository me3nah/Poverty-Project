import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import os
import matplotlib.cm as cm

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
years_short = [y[-2:] for y in years]  # ['85', '86', ..., '21']

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

def get_country_colors(countries):
    """
    Assigns colors to countries with custom logic:
    - US is blue
    - CA is green
    - UK is orange
    - Germany is red
    - All other countries get colors from tab20 colormap, skipping first 4 indices.
    """
    color_map = {}
    # Explicit colors (matplotlib RGBA)
    us_blue    = (0.121, 0.466, 0.705, 1.0)   # US (blue, tab10[0])
    ca_green   = (0.172, 0.627, 0.172, 1.0)   # CA (green, tab10[2])
    uk_orange  = (1.0,   0.498, 0.054, 1.0)   # UK (orange, tab10[1])
    de_red     = (0.839, 0.153, 0.157, 1.0)   # Germany (red, tab10[3])

    for country in countries:
        cu = country.upper()
        if cu in ['US', 'USA', 'UNITED STATES']:
            color_map[country] = us_blue
        elif cu in ['CA', 'CANADA']:
            color_map[country] = ca_green
        elif cu in ['UK', 'GB', 'UNITED KINGDOM']:
            color_map[country] = uk_orange
        elif cu in ['DE', 'GERMANY']:
            color_map[country] = de_red

    # Assign remaining colors from tab20 colormap, skipping 0-3 (already used)
    cmap = cm.get_cmap('tab20', len(countries) + 4)
    idx = 0
    for country in countries:
        if country not in color_map:
            color_map[country] = cmap(idx + 4)
            idx += 1
    return color_map

def plot_comparison_all_countries(years, dart_data, lissy_data, metric, ylabel):
    plt.figure(figsize=(14,7))
    countries = list(dart_data.keys())
    color_map = get_country_colors(countries)
    for country in countries:
        color = color_map[country]
        # DART line: background, thick and faded
        plt.plot(years_short, dart_data[country], color=color, linewidth=8, alpha=0.12)
        # LISSY line: thin, solid, same color
        plt.plot(years_short, lissy_data[country], color=color, linewidth=2, alpha=1, label=f"LISSY {country}")
    plt.title(f"{ylabel}: LISSY vs DART (All Countries)")
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend(loc="best", fontsize="small")
    plt.tight_layout()
    fname = f"all_countries_{metric}_comparison.png".replace(" ", "_")
    plt.savefig(fname)
    plt.close()
    return fname

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
            error_moments_dict[country] = get_error_moments(abs_rel_error)

    # Plot all countries on one compare graph
    if dart_data and lissy_data:
        cmp_plot = plot_comparison_all_countries(years, dart_data, lissy_data, metric['name'], metric['ylabel'])
        print(f"Saved {cmp_plot}")

    # Save CSV of error moments (moments x countries)
    error_moments_df = pd.DataFrame(error_moments_dict)
    error_moments_csv = f"{metric['name']}_error_moments_by_country.csv"
    error_moments_df.to_csv(error_moments_csv)
    print(f"Saved {error_moments_csv}")

print("\nAll done!")
