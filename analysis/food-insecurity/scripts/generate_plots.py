import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- Path Setup ---
# This finds the script's own directory
SCRIPT_DIR = Path(__file__).parent
# This defines the base 'food-insecurity' directory (one level up)
BASE_DIR = SCRIPT_DIR.parent

# Define the data and visuals folders
DATA_DIR = BASE_DIR / 'data'
VISUALS_DIR = BASE_DIR / 'visuals'

# Create the visuals directory if it doesn't exist
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

# --- Load Data (using the robust path) ---
data_file = DATA_DIR / 'eu_silc_meal_data.csv'
df = pd.read_csv(data_file)

# --- Functions (no change) ---
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
    
    # Save the plot (using the robust path)
    plt.savefig(outfile, dpi=300)
    plt.close()
    print(f"Plot saved: {outfile.name}")

# --- Call the function (using the robust paths) ---
plot_country_smoothed('Germany', VISUALS_DIR / 'germany_meal_affordability_smoothed.png')
plot_country_smoothed('UK', VISUALS_DIR / 'uk_meal_affordability_smoothed.png')
