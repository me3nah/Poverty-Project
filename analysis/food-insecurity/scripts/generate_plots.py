import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- Setup Robust Paths ---
# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).resolve().parent

# Go up from 'scripts' to 'analysis/food-insecurity'
BASE_DIR = SCRIPT_DIR.parent

# Define the data and output paths based on this location
DATA_PATH = BASE_DIR / 'data' / 'eu_silc_meal_data.csv'
VISUALS_DIR = BASE_DIR / 'visuals'

# Create the visuals directory if it doesn't exist
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

# --- Load and Inspect the Data ---
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"Error: Data file not found at {DATA_PATH}")
    exit()

# --- DEBUGGING: Uncomment these lines to check your columns and data types ---
# print("--- DataFrame Info ---")
# df.info()
# print("\n--- DataFrame Columns ---")
# print(df.columns.to_list())
# print("\n--- Data Head ---")
# print(df.head())
# --------------------------------------------------------------------------

# Define 3-year rolling average
def smooth_series(series):
    # Ensure data is numeric, coercing errors to NaN (which rolling handles)
    numeric_series = pd.to_numeric(series, errors='coerce')
    return numeric_series.rolling(window=3, min_periods=1, center=True).mean()

def plot_country_smoothed(country_name, outfile):
    # Define the exact columns you expect
    expected_cols = [
        'Year',
        f'{country_name}_Total',
        f'{country_name}_Female',
        f'{country_name}_Male'
    ]
    
    # Check if all expected columns are in the dataframe
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        print(f"Error: Missing columns for '{country_name}': {missing_cols}")
        print(f"Available columns are: {df.columns.to_list()}")
        return

    # Select and copy data
    country_df = df[expected_cols].copy()
    
    # Set index and apply smoothing
    country_df.set_index('Year', inplace=True)
    country_df = country_df.apply(smooth_series)

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(country_df.index, country_df[f'{country_name}_Total'],
             label='Total', linewidth=2, marker='o', markersize=4)
    plt.plot(country_df.index, country_df[f'{country_name}_Female'],
             label='Single Female', linestyle='--', marker='x', markersize=4)
    plt.plot(country_df.index, country_df[f'{country_name}_Male'],
             label='Single Male', linestyle=':', marker='s', markersize=4)
    
    plt.title(f'{country_name}: Inability to Afford a Meal Every Second Day (%)\n(3-Year Rolling Average)')
    plt.xlabel('Year')
    plt.ylabel('Percent')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()
    print(f"Plot saved to {outfile}")

# --- Call the functions ---
plot_country_smoothed('Germany', VISUALS_DIR / 'germany_meal_affordability_smoothed.png')
plot_country_smoothed('UK', VISUALS_DIR / 'uk_meal_affordability_smoothed.png')
