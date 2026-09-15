# Reproducibility protocol

1. Create a clean Python environment.
2. Install `requirements.txt`.
3. Run `pytest -q`; all bundled tests should pass.
4. Run `python main.py` from the repository root.
5. Compare regenerated output structure with `outputs/`; stochastic routines use fixed seeds in the reference workflow.
6. Record Python and dependency versions for any publication-quality rerun.
7. For human data, freeze accession IDs, download date, preprocessing version, inclusion/exclusion criteria and checksums before calibration.
8. Never tune transformations or parameters on the external validation cohort.
9. Report parameter ranges and random seeds with every sensitivity analysis.
10. Recalculate `SHA256SUMS.txt` after any release change.

## Expected tests
The suite checks diffusion monotonicity, gating/response behavior, bounded normalized-response behavior, deterministic/stochastic numerical finiteness, stochastic reproducibility, spatial non-negativity and a Sobol additive benchmark against its analytical variance fractions.
