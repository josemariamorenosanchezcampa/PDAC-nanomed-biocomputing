# Human-data integration plan

No individual-level human data are bundled in v4.0.0. Repository names identify potential sources, not completed validation.

## TCGA-PAAD / NCI GDC
Potential role: PDAC tumor molecular context and calibration of transcriptomic/genomic proxies. Record exact project, data category, workflow, release and download date. Controlled-access files require authorization.

## GTEx pancreas
Potential role: non-diseased pancreatic expression reference. GTEx is not a patient-matched PDAC control and tissue composition differs from tumors. Respect open/controlled access boundaries.

## NCBI GEO
Potential role: independent bulk, single-cell, organoid or spatial cohorts. Each accession must be documented separately because platform, normalization, tissue composition and clinical metadata vary.

## CPTAC / NCI PDC
Potential role: proteomic/proteogenomic anchoring, especially when testing whether transcript-level proxies correspond to protein abundance. Assay-specific normalization and batch effects must be handled explicitly.

## Proxy policy
Do not equate GPX4 RNA with GPX4 catalytic activity. Do not infer ROS or labile Fe2 from expression without a justified and validated mapping. `xi` is a structural transport descriptor and generally requires imaging, histology or transport-based inference.

## Calibration/validation design
Use one cohort for preprocessing decisions and parameter fitting. Freeze the pipeline. Evaluate a separate cohort without refitting. Report uncertainty and negative results.

## Zenodo redistribution
Do not include controlled-access raw data, identifying data or data whose license prohibits redistribution. Archive accession manifests, code, derived non-identifying summaries when permitted, and provenance sufficient to reacquire the original data.
