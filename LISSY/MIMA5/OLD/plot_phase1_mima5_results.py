import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('phase1_mima5_results.csv')

# List of countries in the data
countries = df['country'].unique()

# Plot mima5 over time
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['country'] == country]
    plt.plot(country_data['year'], country_data['mima5'], label=country)
plt.xlabel('Year')
plt.ylabel('mima5 (5-year MA of household income)')
plt.title('mima5 over Time by Country')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)  # Faded grid
plt.tight_layout()
plt.savefig('mima5_by_country.png')
plt.show()

# Plot pl (poverty line) over time
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['country'] == country]
    plt.plot(country_data['year'], country_data['pl'], label=country)
plt.xlabel('Year')
plt.ylabel('pl (Poverty Line, half of mima5)')
plt.title('Poverty Line (pl) over Time by Country')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)  # Faded grid
plt.tight_layout()
plt.savefig('pl_by_country.png')
plt.show()

# Plot H (poverty rate) over time
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['country'] == country]
    plt.plot(country_data['year'], country_data['H'], label=country)
plt.xlabel('Year')
plt.ylabel('H (Poverty Rate)')
plt.title('Poverty Rate (H) over Time by Country')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)  # Faded grid
plt.tight_layout()
plt.savefig('poverty_rate_by_country.png')
plt.show()
