# scripts/

## Purpose

Utility scripts for repository automation and maintenance.

## Contents

- `convert-html-to-md.sh` - Automated HTML-to-Markdown converter using pandoc

## Quick start

The HTML converter runs automatically via GitHub Actions when HTML files are added to the repository.

**Manual execution:**
```bash
# Ensure pandoc is installed
sudo apt-get install pandoc  # Linux
# brew install pandoc         # macOS

# Run converter
./scripts/convert-html-to-md.sh
```

## Conventions

- Scripts are executable (`chmod +x`)
- Include usage comments at the top of each script
- Set environment variables via GitHub Actions workflows (see `.github/workflows/html-to-md.yml`)

## GitHub Actions Integration

- **Workflow**: `.github/workflows/html-to-md.yml`
- **Trigger**: Push events with HTML files
- **Output**: Markdown files committed automatically with `[skip html-to-md]` marker
