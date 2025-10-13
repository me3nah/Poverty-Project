import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# --- CONFIGURATION ---
DATA_DIR = '.'  # Use current folder
LISSY_PATTERN = "lissy_*.csv"
DART_PATTERN = "dart_*.csv"

# These are the expected metric pairs
metrics = [
    ("dhi_median", "dart_dhi_median"),
    ("dhi_pr", "dart_dhi_pr"),
    ("mhi_median", "dart_mhi_median"),
    ("mhi_pr", "dart_mhi_pr"),
]

def plot_series_comparison(time, target, interest, title, ylabel, out_file):
    plt.figure(figsize=(9, 5))
    plt.plot(time, target, color="#0072B2", linewidth=4, alpha=0.25, label='DART (Benchmark)')
    plt.plot(time, interest, color="#0072B2", linewidth=1.5, alpha=1, label='LISSY (Extracted)')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel("Time/Observation Index")
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_file)
    plt.close()

def plot_error_distribution(errors, title, out_file):
    plt.figure(figsize=(7, 4))
    sns.histplot(errors, bins=30, color="#0072B2", kde=True)
    plt.title(title, fontsize=12, fontweight='bold')
    plt.xlabel("Absolute Relative Error")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(out_file)
    plt.close()

def absolute_relative_error(target, interest):
    return (target - interest).abs() / target.abs()

def save_moments(errors, out_file):
    moments = {
        "mean": errors.mean(),
        "variance": errors.var(),
        "skewness": skew(errors),
        "kurtosis": kurtosis(errors),
        "min": errors.min(),
        "max": errors.max(),
        "count": errors.count()
    }
    with open(out_file, "w") as f:
        for k, v in moments.items():
            f.write(f"{k}: {v}\n")

if __name__ == "__main__":
    for lissy_name, dart_name in metrics:
        lissy_file = glob.glob(os.path.join(DATA_DIR, f"{lissy_name}.csv"))
        dart_file = glob.glob(os.path.join(DATA_DIR, f"{dart_name}.csv"))
        if not (lissy_file and dart_file):
            print(f"Skipping {lissy_name}/{dart_name}: files not found.")
            continue

        lissy_df = pd.read_csv(lissy_file[0])
        dart_df = pd.read_csv(dart_file[0])

        time = lissy_df['Time']
        lissy_values = lissy_df['Value']
        dart_values = dart_df['Value']

        graph_title = f"{lissy_name.replace('_', ' ').upper()} vs DART"
        ylabel = lissy_name.split('_')[1].capitalize()
        out_graph = f"comparison_{lissy_name}_vs_{dart_name}.png"
        plot_series_comparison(time, dart_values, lissy_values, graph_title, ylabel, out_graph)

        errors = absolute_relative_error(dart_values, lissy_values)
        error_title = f"Distribution of Absolute Relative Errors: {lissy_name.replace('_', ' ').upper()}"
        out_error = f"error_distribution_{lissy_name}_vs_{dart_name}.png"
        plot_error_distribution(errors, error_title, out_error)

        # Save moments to txt
        moments_txt = f"moments_{lissy_name}_vs_{dart_name}.txt"
        save_moments(errors, moments_txt)

        print(f"Saved: {out_graph}, {out_error}, {moments_txt}")

    print("All graphs, distributions, and summary txt files saved.")
