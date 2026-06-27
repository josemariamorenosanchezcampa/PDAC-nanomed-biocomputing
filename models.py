# -*- coding: utf-8 -*-
"""
Computational Modeling for Bicompound Nanotherapeutic Architecture in PDAC.
Contains definitions for Stokes-Einstein diffusion, Debye-Huckel potentials,
Hill cooperativity kinetics, and the absolute cell death vector (Phi_Death).
"""

import numpy as np

def calculate_stokes_einstein_diffusion(sigma, r_H, xi, T=310.15, eta_0=1.2e-3, gamma=0.85, alpha=1.2):
    """
    Calculates the effective translational diffusion coefficient (D_eff) inside the stroma.
    """
    k_B = 1.3806e-23
    D_0 = (k_B * T) / (6 * np.pi * eta_0 * r_H)
    steric_hindrance = np.exp(-gamma * ((r_H / xi) ** alpha))
    D_eff = 0.5 * sigma * D_0 * steric_hindrance
    return D_eff

def calculate_debye_huckel_potential(r, a, psi_0, kappa):
    """
    Calculates the electrostatic potential psi(r) based on Debye-Huckel equation.
    """
    if r < a:
        return psi_0
    return psi_0 * (a / r) * np.exp(-kappa * (r - a))

def calculate_hill_occupancy(X, K_D, n):
    """
    Calculates fractional occupancy f(theta) using non-linear Hill cooperativity kinetics.
    """
    return (X ** n) / (K_D ** n + X ** n)

def evaluate_phi_death(A1, A2, B_miRNA, gpx4_conc, ros_lipid, fe2_free, w1=1.0, w2=1.0, w3=1.0):
    """
    Evaluates the deterministic state vector of absolute cell death (Phi_Death).
    """
    logic_prefix = int(A1 and A2 and not B_miRNA)
    if logic_prefix == 0:
        return 0.0
    
    # Avoid division by zero if GPX4 approaches 0
    gpx4_term = w1 * (1.0 / gpx4_conc) if gpx4_conc > 0 else float('inf')
    phi = logic_prefix * (gpx4_term + w2 * ros_lipid + w3 * fe2_free)
    return phi

if __name__ == "__main__":
    print("PDAC Nanomedicine Biocomputing Models Loaded Successfully.")
