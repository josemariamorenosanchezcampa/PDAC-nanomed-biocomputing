# Model card — PDAC Nanotherapeutic Architecture v4.0.0

## Intended use
Research, education, hypothesis generation, sensitivity analysis, experiment prioritization and development of reproducible workflows for multiscale PDAC nanotherapy modeling.

## Not intended for
Clinical decision-making, patient stratification without validation, prescription or dosing, diagnosis, safety claims, efficacy claims, regulatory submission as a validated medical product, or replacement of experimental evidence.

## Inputs
Nanoparticle hydrodynamic radius, stromal correlation length, GPX4-related proxy/state, ROS-related proxy/state, labile iron-related proxy/state and optional kinetic/control parameters.

## Outputs
Effective diffusion, delivery factor, reduced ferroptosis score, bounded response, spatial concentration fields, ODE/SDE trajectories, PRCC/Sobol sensitivity indices, synthetic calibration metrics and mathematically optimized model-unit schedules.

## Key assumptions
- Stokes-Einstein diffusion is modified by a phenomenological steric term.
- Transport affects response through normalized delivery.
- The reduced intracellular score omits many ferroptosis regulators.
- Parameter distributions in sensitivity analysis are independent uniforms over declared ranges.
- Human molecular measurements require explicit proxy mappings.

## Validation status
Software sanity tests and synthetic benchmarks are included. No bundled result constitutes clinical, preclinical or external human validation.

## Principal risks of misuse
Treating RNA as protein activity; treating synthetic R² as human predictive performance; interpreting sensitivity rank as causal clinical importance; interpreting optimized model units as a patient regimen; redistributing controlled human data.
