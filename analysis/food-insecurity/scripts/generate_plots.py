import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('analysis/food-insecurity/data/eu_silc_meal_data.csv')

def plot_country(country, outfile):
    country_df = df[['Year',
                     f'{country}_Total',
                     f'{country}_Female',
                     f'{country}_Male']]
    plt.figure()
    plt.plot(country_df['Year'], country_df[f'{country}_Total'],
             label='Total')
    plt.plot(country_df['Year'], country_df[f'{country}_Female'],
             label='Single Female')
    plt.plot(country_df['Year'], country_df[f'{country}_Male'],
             label='Single Male')
    plt.title(f'{country}: Inability to afford a meal every second day (%)')
    plt.xlabel('Year')
    plt.ylabel('Percent')
    plt.legend()
    plt.grid(True)
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    plt.close()

plot_country('Germany', 'analysis/food-insecurity/visuals/germany_meal_affordability.png')
plot_country('UK', 'analysis/food-insecurity/visuals/uk_meal_affordability.png')
