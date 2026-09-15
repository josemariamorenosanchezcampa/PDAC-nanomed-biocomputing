"""Biophysical core for the PDAC nanotherapy research model v4.

All outputs are in-silico research quantities, not clinical predictions.
"""
from __future__ import annotations
import numpy as np
K_B = 1.380649e-23

def diffusion(sigma: float, r_h_m: float, xi_m: float, T=310.15, eta=1.2e-3, gamma=.85, alpha=1.2):
    if not 0 < sigma <= 1 or min(r_h_m, xi_m, T, eta) <= 0: raise ValueError("invalid physical parameter")
    d0 = K_B*T/(6*np.pi*eta*r_h_m)
    return .5*sigma*d0*np.exp(-gamma*(r_h_m/xi_m)**alpha)

def delivery_factor(r_h_m, xi_m, sigma=1., ref_r=20e-9, ref_xi=45e-9):
    return diffusion(sigma,r_h_m,xi_m)/diffusion(sigma,ref_r,ref_xi)

def ferroptosis_score(gpx4, ros, fe2, weights=(1.,1.,1.)):
    """Reduced phenomenological score in model units, not a biochemical law.

    Inputs must either be normalized to declared reference scales or the fitted
    weights must carry the reciprocal units required to make the three terms
    commensurate. The default numerical example uses model units only.
    """
    if gpx4 <= 0 or ros < 0 or fe2 < 0: raise ValueError("invalid biomarker value")
    w1,w2,w3=weights
    return w1/gpx4+w2*ros+w3*fe2

def gate(a1=True,a2=True,b_mirna=False): return int(bool(a1) and bool(a2) and not bool(b_mirna))

def phi_death(gpx4,ros,fe2,r_h_m=20e-9,xi_m=45e-9,sigma=1.,weights=(1.,1.,1.),a1=True,a2=True,b_mirna=False):
    return gate(a1,a2,b_mirna)*delivery_factor(r_h_m,xi_m,sigma)*ferroptosis_score(gpx4,ros,fe2,weights)

def normalized_response(phi, midpoint=75., scale=15.):
    """Bounded logistic model response; not a calibrated probability by default."""
    if scale <= 0: raise ValueError("scale must be > 0")
    z=np.clip((np.asarray(phi)-midpoint)/scale,-60,60)
    return 1/(1+np.exp(-z))

def death_probability(phi, midpoint=75., scale=15.):
    """Backward-compatible alias. Interpret as probability only after calibration."""
    return normalized_response(phi, midpoint, scale)
