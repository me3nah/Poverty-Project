import pandas as pd
import matplotlib.pyplot as plt

# Load the data - FIXED PATH
df = pd.read_csv('../data/eu_silc_meal_data.csv')

# Define 3-year rolling average
def smooth_series(series):
    return series.rolling(window=3, min_periods=1, center=True).mean()

def plot_country_smoothed(country, outfile):
    country_df = df[['Year',
                     f'{country}_Total',
                     f'{country}_Female',
                     f'{country}_Male']].copy()
    country_df.set_index('Year', inplace=True)
    country_df = country_df.apply(smooth_series)

    plt.figure(figsize=(10, 6))
    plt.plot(country_df.index, country_df[f'{country}_Total'],
             label='Total', linewidth=2)
    plt.plot(country_df.index, country_df[f'{country}_Female'],
             label='Single Female', linestyle='--')
    plt.plot(country_df.index, country_df[f'{country}_Male'],
             label='Single Male', linestyle=':')
    plt.title(f'{country}: Inability to Afford a Meal Every Second Day (%)\n(3-Year Rolling Average)')
    plt.xlabel('Year')
    plt.ylabel('Percent')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()

# Call the function - FIXED PATHS
plot_country_smoothed('Germany', '../visuals/germany_meal_affordability_smoothed.png')
plot_country_smoothed('UK', '../visuals/uk_meal_affordability_smoothed.png')

print("Plots generated successfully in the 'visuals' folder.")
