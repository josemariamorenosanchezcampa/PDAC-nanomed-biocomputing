# Validation plan — v4.0.0

## Level 1: mathematical verification
Check domains, units, limiting behavior, solver stability and benchmark problems.

## Level 2: software verification
Run unit tests, deterministic reruns, multiple seeds and regression tests against known synthetic problems.

## Level 3: computational validation
Study sensitivity to parameter ranges, priors, numerical resolution and alternative model structures. Report uncertainty intervals rather than a single deterministic result.

## Level 4: data calibration
Fit only parameters that are identifiable from a declared calibration dataset. Preserve raw-to-model transformations and avoid equating molecular proxies with biochemical activities.

## Level 5: external validation
Lock equations, transformations and fitted parameters before evaluating a genuinely independent cohort. Report R², RMSE, MAE, calibration where applicable and bootstrap uncertainty.

## Level 6: experimental validation
Measure nanoparticle transport/penetration, release, uptake, GPX4-related state, ROS, labile iron, lipid peroxidation and ferroptosis outcomes under controlled conditions.

## Level 7: preclinical translation
Only after earlier levels: evaluate biodistribution, PK/PD, toxicity, immunogenicity, therapeutic window and reproducibility in appropriate biological models.

No computational level alone establishes clinical efficacy or safety.
