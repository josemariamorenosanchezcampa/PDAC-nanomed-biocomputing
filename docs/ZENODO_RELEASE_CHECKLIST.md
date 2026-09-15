# Zenodo release checklist — v4.0.0

## Metadata
- [ ] Title matches README/CITATION.cff.
- [ ] Version is 4.0.0.
- [ ] Author is Moreno Sánchez-Campa, José María.
- [ ] ORCID is 0009-0000-0927-7397.
- [ ] DOI shown for this release is 10.5281/zenodo.22764930.
- [ ] Category/description states Project Proposal / Computational Proof of Concept.
- [ ] License is CC BY 4.0 everywhere.

## Scientific QA
- [ ] No synthetic benchmark is described as human validation.
- [ ] Sobol indices are computed, not manually entered.
- [ ] Optimized dosing is labeled in-silico/model units.
- [ ] Human repositories are described as sources unless a dataset is actually processed.
- [ ] GPX4 RNA is not described as GPX4 activity/concentration without a mapping model.

## Software QA
- [ ] `pytest -q` passes.
- [ ] `python main.py` runs from a clean environment.
- [ ] Output files regenerate.
- [ ] SHA256 checksums were recalculated after final edits.

## Archive QA
- [ ] No secrets, credentials, identifying patient data or controlled human data.
- [ ] README, LICENSE, CITATION.cff, metadata, manuscript, methods, validation and bibliography are included.
- [ ] Landscape and portrait infographics are supplementary, not substitutes for methods/results.
