# Data Availability Visualizations

This directory contains tools for generating data availability visualizations from country-by-year CSV data.

## Overview

The visualization tool creates two output files for each CSV:

1. **Plain text file (`.txt`)**: A grid visualization with headers and legend
2. **Markdown file (`.md`)**: Same grid in a code fence plus a summary section

Both files show data availability across years for each entity (country), with rows sorted by ascending longest streak length.

## Files

- `generate_visuals.py`: Python script that generates the visualizations
- `*.txt`: Generated plain text visualizations
- `*.md`: Generated Markdown visualizations

## How to Generate Visualizations


