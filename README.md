# Source Code and Kinetic Calibration Matrices for the PDAC Nanotherapeutic Architecture

This repository contains the foundational biophysical calibration matrices, multi-phase transport parameters, and biochemical specifications for the dual-nanoplataform system (NPA and NPB) designed for Pancreatic Ductal Adenocarcinoma (PDAC).

## 🔬 Project Overview
The dataset and underlying scripts model a fourth-generation nanomedicine platform featuring:
1. **Multi-Phase Kinetic Transport:** Sequential stroma fluidization and targeted synthetic lethality triggered by boolean `[AND]` enzymatic gates (MMP-9 / Cathepsin B).
2. **Active Hepatoprotective Shielding:** Selective sinusoidal clearance mediated by GalNAc/ASGPR interactions combined with an irreversible covalent Michael addition at the Cys524 residue of the SMAD4 protein.
3. **Genetic Circuit Controls:** Safety regulation utilizing an Incoherent Feed-Forward Loop (IFFL) driven by the hepatocyte-specific miR-122 sentinel microRNA.

## 📊 Repository Structure
* `/data`: Contains raw calibration matrices and kinetic datasets (`Libro1z.xlsx` / CSV unifications).
  * `Hoja1_Especificaciones.csv`: Multi-phase specification matrix.
  * `Hoja2_Blindaje_Hepatico.csv`: Active biochemical hepatoprotective shield parameters.
  * `Hoja3_Parametros_Control.csv`: Biophysical constants and bio-calibration constraints.
* `/src`: Contains the source code used for the *in silico* molecular biocomputing simulations and stoichiometric decay tracking.

## 🧑‍🔬 Author & Metadata
* **Lead Researcher:** JM Moreno Sánchez-Campa
* **ORCID:** [0009-0008-5421-4601](https://orcid.org/0009-0008-5421-4601)
* **Associated Concept DOI (Report):** [10.5281/zenodo.20821491](https://doi.org/10.5281/zenodo.20821491)

## 📄 License
