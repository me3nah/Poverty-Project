# METIS-LIS/

## Purpose

Documentation and metadata for LIS (Luxembourg Income Study) datasets, including codebooks, MIMA indicator definitions, and wave/date mappings.

## Contents

- `codebook.pdf` - LIS variable codebook (names, definitions, codes)
- `mima_indicator.md` - MIMA (Median Income Moving Average) indicator methodology
- `waves-and-dates.md` - LIS data collection waves and reference dates

## Quick start

**View codebook:**
```bash
open METIS-LIS/codebook.pdf  # macOS
xdg-open METIS-LIS/codebook.pdf  # Linux
```

**Review MIMA methodology:**
```bash
cat METIS-LIS/mima_indicator.md
```

## Conventions

- Files are reference documentation (read-only)
- PDF codebook is the authoritative source for LIS variable definitions
- Markdown files provide concise summaries for quick reference

## Related Resources

- [LIS METIS Portal](https://www.lisdatacenter.org/frontend) - Full online documentation
- [LIS Database](https://www.lisdatacenter.org/) - Official LIS homepage
- **DART/MIMA/** - Implementation of MIMA methodology
- **LISSY/** - Remote execution system for LIS microdata

## Maintainers

Documentation sourced from [LIS Cross-National Data Center](https://www.lisdatacenter.org/).
