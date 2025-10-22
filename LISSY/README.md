# LISSY/

## Purpose

LISSY (LIS remote-execution system) documentation, tutorials, and outputs. This folder contains onboarding materials, validation scripts, and analysis results from LIS microdata jobs.

## Contents

- **Tutorial/** - LISSY onboarding, syntax examples, and exercises (comprehensive README inside)
- **DART_Validation/** - Validates LISSY job outputs against DART aggregated tables
- **MIMA5/** - MIMA5 poverty rate analysis and visualizations

## Quick start

**New to LISSY?** Start with the Tutorial:
```bash
# Read the tutorial README
cat LISSY/Tutorial/README.md

# Browse R and Stata syntax examples
ls LISSY/Tutorial/Exercises_syntax_files-R-Part_II/
```

**Validate your LISSY results:**
```bash
cd LISSY/DART_Validation
python validate_lissy_vs_dart.py
```

**Plot MIMA5 poverty rates:**
```bash
cd LISSY/MIMA5
python plotting_mima5_pr.py
```

## What is LISSY?

LISSY is a remote-execution system that allows researchers to access [LIS](https://www.lisdatacenter.org/) and [LWS](https://www.lisdatacenter.org/data-access/lws/) microdata while adhering to privacy restrictions. Researchers submit statistical programs (R, SAS, SPSS, Stata) through a web-based interface, and LISSY returns aggregated results.

## How to Register

[Register for LISSY access](https://www.lisdatacenter.org/data-access/lissy/) (1-year access, renewable annually).

## Privacy & Secrets

**Critical:** LIS microdata is confidential. NEVER commit microdata to this repository.

- Submit jobs via the [LISSY web interface](https://www.lisdatacenter.org/data-access/lissy/)
- Only commit **aggregated outputs** (tables, plots, summary statistics)
- Individual-level data violates LIS terms of use
- See [LIS Privacy Policy](https://www.lisdatacenter.org/about-lis/terms-of-use/)

## Onboarding Resources

- **Tutorial/** folder in this repo (syntax examples, exercises)
- [LIS Self-Teaching Materials](https://www.lisdatacenter.org/resources/self-teaching/)
- [METIS Documentation Portal](https://www.lisdatacenter.org/frontend)
- [LIS FAQ](https://www.lisdatacenter.org/resources/faq/)
- Contact: [usersupport@lisdatacenter.org](mailto:usersupport@lisdatacenter.org)

## Citation

All papers using LIS microdata must be submitted to the LIS Working Paper series before publication. See [General Policies](https://www.lisdatacenter.org/working-papers/#general).

## Related Folders

- **METIS-LIS/** - LIS codebooks and variable documentation
- **DART/** - DART validation using aggregated tables (no microdata)
- **compute_mima.py** (root) - MIMA workflow using DART tables

## Maintainers

Documentation and examples sourced from [LIS Cross-National Data Center](https://www.lisdatacenter.org/).
