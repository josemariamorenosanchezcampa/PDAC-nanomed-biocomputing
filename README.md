# PDAC Nanotherapeutic Architecture — v4.0.0

**A multiscale computational proof of concept for nanoparticle transport, ferroptosis dynamics, uncertainty analysis, calibration and in-silico dosing optimization in pancreatic ductal adenocarcinoma (PDAC).**

**Author:** Moreno Sánchez-Campa, José María  
**Year:** 2026  
**Category:** Project Proposal / Computational Proof of Concept  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**DOI:** 10.5281/zenodo.22764930  
**ORCID:** 0009-0000-0927-7397  
**Version:** 4.0.0

> Scientific status: research software and hypothesis-generating in-silico model. It is not a medical device, clinical decision system, validated therapy, dosing recommendation, or demonstration of clinical efficacy or safety.

## Abstract

PDAC Nanotherapeutic Architecture v4.0.0 integrates biophysical nanoparticle transport, heterogeneous stromal diffusion, phenomenological transport-to-delivery coupling, ferroptosis-related intracellular states, deterministic and stochastic dynamics, global sensitivity analysis, calibration utilities and constrained dosing optimization. The model links hydrodynamic radius and an effective stromal correlation length to diffusion, propagates spatial concentration with a two-dimensional diffusion-reaction prototype, and represents a reduced ferroptosis state using GPX4-related antioxidant capacity, reactive oxygen species (ROS), labile iron and lipid peroxidation. Uncertainty is evaluated with Latin hypercube sampling, PRCC with bootstrap confidence intervals, and computed Sobol first- and total-order indices. Calibration and validation are deliberately separated: the bundled calibration example is synthetic and serves only as software verification. TCGA/GDC, GTEx, NCBI GEO and CPTAC/PDC are documented as candidate public sources for future human-data calibration and independent validation; repository availability is not presented as evidence that those data have already validated the v4 results. The project is intended to generate testable hypotheses and prioritize experiments while keeping mathematical outputs clearly separated from biological and clinical evidence.

## Scientific workflow

`nanoparticle design → stromal transport → delivery/release → intracellular exposure → ferroptosis-related dynamics → predicted in-silico response`

Analytical layers surround the mechanistic chain: `LHS/PRCC + Sobol → calibration → external validation → constrained dosing optimization`.

## Core equations

Stokes–Einstein reference diffusion:

`D0 = k_B T / (6 π η r_H)`

Effective diffusion with steric hindrance:

`D_eff = 0.5 σ D0 exp[-γ (r_H/ξ)^α]`

Phenomenological delivery coupling:

`F_delivery = (D_eff / D_ref) f_release(t)`

Spatial diffusion–reaction prototype:

`∂C/∂t = ∇·(D(x,y)∇C) − k_u C − k_deg C`

The v4.0.0 release solver discretizes the heterogeneous diffusion term in conservative face-flux form with harmonic face diffusivities.

Reduced ferroptosis score:

`S = w1/GPX4 + w2·ROS + w3·Fe2`

This is a phenomenological score in model units. GPX4, ROS and Fe2 must be normalized to declared reference scales, or the fitted weights must carry reciprocal units that make the terms commensurate; default weights are illustrative, not universal biochemical constants.

Bounded response mapping:

`Phi_death = 1 / (1 + exp[-(S − S0)/k])`

The model also contains deterministic ODE and stochastic SDE representations for GPX4-like, ROS-like and lipid-peroxidation states.

## Installation and reproduction

Python 3.10+ is recommended.

```bash
python -m pip install -r requirements.txt
python main.py
pytest -q
```

`main.py` regenerates machine-readable sensitivity and synthetic benchmark outputs plus the principal scientific figures in `outputs/`.

## Human-data policy

No individual-level human data are bundled. TCGA-PAAD/GDC is proposed for tumor molecular context; GTEx pancreas for non-diseased expression reference; GEO for independent bulk, single-cell or spatial cohorts; and CPTAC/PDC for proteomic/proteogenomic anchoring. RNA expression is not equated with protein abundance or biochemical activity. GPX4, ROS, Fe2 and stromal variables require explicit measurement-to-model mappings. Controlled-access or identifying data must never be redistributed in this archive.

## Repository map

- `pdac_model/` — executable model modules.
- `tests/` — unit and sanity tests.
- `main.py` — reproducible end-to-end example.
- `outputs/` — generated figures and machine-readable results.
- `docs/METHODS.md` — equations, assumptions and algorithms.
- `docs/MODEL_EQUATIONS.md` — compact mathematical specification.
- `docs/MODEL_CARD.md` — intended use, non-use, limitations and validation status.
- `docs/HUMAN_DATA.md` — human-data integration and proxy policy.
- `docs/VALIDATION.md` — validation roadmap and reporting rules.
- `docs/REPRODUCIBILITY.md` — reproducibility protocol.
- `docs/DATA_DICTIONARY.md` — model/data variable definitions.
- `docs/REFERENCIAS_BIBLIOGRAFICAS_60.md` — 60 annotated references and their role in the project.
- `manuscript/` — extended v4.0.0 project manuscript.
- `infographics/` — landscape and portrait graphical summaries.

## Citation

Please cite the exact Zenodo version used. Citation metadata are supplied in `CITATION.cff`. Suggested human-readable citation:

Moreno Sánchez-Campa, José María (2026). *PDAC Nanotherapeutic Architecture v4.0.0: Multiscale Computational Proof of Concept for Nanoparticle Transport and Ferroptosis-Based Therapy in PDAC*. Zenodo. DOI: 10.5281/zenodo.22764930.

## License

This release is distributed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Attribution must identify the author and source. See `LICENSE` and `NOTICE.md`.

## Interpretation rule

A model result is evidence about the behavior of the model under declared assumptions. It is not automatically evidence of patient benefit, therapeutic safety, clinical selectivity, or readiness for translation. Any future human-data release must freeze accession IDs, preprocessing and calibration choices before external validation.
