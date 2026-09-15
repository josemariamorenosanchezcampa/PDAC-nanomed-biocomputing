## 4.0.0 — scientific audit corrections
- Corrected the heterogeneous spatial operator to a conservative discretization of div(D grad C), using harmonic face diffusivities.
- Clarified dimensional interpretation of the reduced ferroptosis score and its weights.
- Added `normalized_response()` while retaining `death_probability()` as a backward-compatible alias with an explicit calibration caveat.
- Renamed the optimization penalty concept from toxicity to exposure/control penalty (legacy keyword accepted for compatibility).
- Strengthened spatial and analytical Sobol tests.
- Replaced/normalized bibliographic entries identified by the scientific audit and embedded the audit report in `docs/`.
- Corrected manuscript references and interpretation language.

# Changelog

## v4.0.0 — 2026

### Added
- Integrated causal chain from nanoparticle transport to effective delivery and ferroptosis-related response.
- Computed Sobol first-order and total-order sensitivity indices.
- Corrected rank-based PRCC workflow with intercepts and bootstrap confidence intervals.
- Heterogeneous two-dimensional stromal diffusion field and diffusion-reaction concentration prototype.
- Deterministic ODE and Euler-Maruyama SDE ferroptosis-related dynamics.
- Constrained numerical optimization of a seven-control in-silico dosing schedule.
- Synthetic calibration benchmark with hold-out R², RMSE and MAE.
- Human-data ingestion contract, proxy policy and external-validation plan.
- Expanded tests, model card, data dictionary, reproducibility protocol, annotated bibliography, manuscript and infographics.
- Zenodo metadata, CC BY 4.0 licensing, citation file and release checksums.

### Scientific interpretation changes
- Removed any interpretation of manually entered sensitivity bars as Sobol results; v4 computes indices from model evaluations.
- A dosing curve is called optimal only when produced by the declared numerical objective and constraints.
- Synthetic calibration is explicitly labeled software verification and not experimental/human validation.
- Repository data sources are distinguished from datasets actually processed by the pipeline.

## v3.0.0
- Coupled r_H and xi to the ferroptosis score through normalized transport.
- Corrected PRCC residual regressions and added uncertainty/convergence analysis.
