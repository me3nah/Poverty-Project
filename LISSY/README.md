# LISSY (Remote-Execution System for LIS/LWS Microdata)

## Purpose

Documentation, tutorials, and job templates for submitting reproducible statistical programs to the LISSY remote-execution system. LISSY provides secure access to LIS and LWS microdata while adhering to privacy restrictions.

## Quick Start

**Register for access**: [LIS LISSY Registration](https://www.lisdatacenter.org/data-access/lissy/)

**Get started with tutorials**:
```bash
# Explore R tutorials
ls LISSY/Tutorial/

# Review job submission basics
cat LISSY/Tutorial/README.md
```

**Submit a job** via [LISSY Web Interface](https://www.lisdatacenter.org/data-access/lissy/):
- Write jobs in R, SAS, SPSS, or Stata
- Jobs return aggregated results within minutes
- See [Tutorial/](Tutorial/) for language-specific examples

## Contents

- `Tutorial/` — Self-teaching materials and examples (R, Stata) (see [Tutorial/README.md](Tutorial/README.md))
- `DART_Validation/` — Validation scripts comparing LISSY with DART tables (see [DART_Validation/README.md](DART_Validation/README.md))
- `MIMA5/` — MIMA5 analysis scripts and plotting utilities (see [MIMA5/README.md](MIMA5/README.md))

## Key Resources

- **LISSY Interface**: https://www.lisdatacenter.org/data-access/lissy/
- **METIS (Documentation)**: https://www.lisdatacenter.org/frontend
- **Self-Teaching Materials**: https://www.lisdatacenter.org/resources/self-teaching/
- **FAQ**: https://www.lisdatacenter.org/resources/faq/
- **User Support**: usersupport@lisdatacenter.org

## Dataset Aliases and Syntax

Datasets use 2-letter country code + 2-digit year + file type letter:
- Example: `lu04h` = Luxembourg 2004 household file

**Calling datasets by statistical package**:
- **R**: `ds <- read.LIS("lu10h")` or use `lissyrtools` package
- **SAS**: `PROC MEANS DATA=&lu10h;`
- **SPSS**: `get file = lu10h`
- **Stata**: `use $lu10h` or `lissyuse` command

## Conventions

- **Do not commit secrets** — LISSY credentials must be stored externally
- **Test jobs locally** using [LIS sample files](https://www.lisdatacenter.org/data-access/lissy/) before submitting
- **Debug syntax** on your computer to avoid system congestion
- **Do not print individual records** — violates privacy and may terminate access
- **Avoid disallowed commands**: `print`, `list`, `pwd`, `rm`, etc.
- Submit jobs one at a time and wait for results before submitting next

## Citation Requirements

All papers using LIS microdata must be submitted to the [LIS Working Paper series](https://www.lisdatacenter.org/working-papers/#general) before publication. Follow [LIS citation guidelines](https://www.lisdatacenter.org/about-lis/terms-of-use/).

## Maintainers

- @EEbrami
