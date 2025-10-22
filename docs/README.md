# docs/

## Purpose

Documentation and reference materials for the Poverty Project repository.

## Contents

Currently minimal; intended for project-wide documentation such as:
- Contributor guides
- Data access instructions
- Analysis methodology overviews
- Onboarding materials

## Quick start

Place HTML documentation files here for automatic conversion to Markdown via the `scripts/convert-html-to-md.sh` workflow.

**Add new documentation:**
```bash
# Place HTML file in docs/
cp mydoc.html docs/

# Commit and push - automatic conversion to Markdown will run
git add docs/mydoc.html
git commit -m "docs: add new documentation"
git push
```

## Conventions

- Use descriptive filenames
- Prefer Markdown (`.md`) over HTML when possible
- Link to external LIS documentation rather than duplicating content

## Related Folders

- **METIS-LIS/** - LIS-specific codebooks and metadata
- **LISSY/Tutorial/** - LISSY onboarding and usage examples
- **scripts/** - HTML-to-Markdown converter
