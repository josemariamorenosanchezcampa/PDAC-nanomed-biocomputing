# Data dictionary

| Variable | Meaning in model | Typical unit/status | Human-data interpretation |
|---|---|---|---|
| `r_H` | nanoparticle hydrodynamic radius | m in code | physical design variable |
| `xi` | effective stromal correlation length | m in code | inferred structural proxy unless measured |
| `sigma` | dimensionless transport prefactor | 0–1 | model parameter |
| `GPX4` | reduced antioxidant state/input | positive model quantity | RNA/protein/activity must be distinguished |
| `ROS` | reactive-oxygen state/input | non-negative model quantity | direct assay or validated proxy preferred |
| `Fe2` | labile iron-related state/input | non-negative model quantity | direct labile-iron assay or justified proxy |
| `Phi_Death` | transport-weighted ferroptosis score | model units | not a clinical probability |
| `death_probability` | logistic bounded response | 0–1 | requires outcome calibration before probability interpretation |
| `C(x,y,t)` | normalized spatial concentration | normalized | requires imaging/transport calibration for physical concentration |
| `G,R,L` | GPX4-like, ROS-like, lipid-peroxidation states | model units | reduced dynamical states |
| `u(t)` | dosing/control input | model units | not a patient dose |

Human validation schema: `GPX4_proxy, ROS_proxy, Fe2_proxy, death_fraction`, with optional provenance fields `cohort, sample_id_hash, tissue, platform, outcome_time, source_accession`.
