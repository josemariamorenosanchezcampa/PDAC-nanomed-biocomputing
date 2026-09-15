# -*- coding: utf-8 -*-
"""PDAC nanotherapeutic model v3.0.

Research prototype. The transport-to-ferroptosis coupling is a phenomenological
hypothesis and must be calibrated/validated before biological or clinical use.
"""
from __future__ import annotations
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rankdata, t as student_t

K_B = 1.380649e-23


def calculate_stokes_einstein_diffusion(sigma, r_H, xi, T=310.15,
                                         eta_0=1.2e-3, gamma=0.85, alpha=1.2):
    """Effective diffusion with stromal steric hindrance (SI units)."""
    if not (0 < sigma <= 1):
        raise ValueError("sigma must be in (0, 1].")
    if r_H <= 0 or xi <= 0 or eta_0 <= 0 or T <= 0:
        raise ValueError("r_H, xi, eta_0 and T must be > 0.")
    d0 = K_B * T / (6 * np.pi * eta_0 * r_H)
    hindrance = np.exp(-gamma * (r_H / xi) ** alpha)
    return 0.5 * sigma * d0 * hindrance


def logic_gate(A1, A2, B_miRNA):
    """Tumour-selective Boolean gate used by the conceptual model."""
    return int(bool(A1) and bool(A2) and not bool(B_miRNA))


def intracellular_ferroptosis_score(gpx4_conc, ros_lipid, fe2_free,
                                     w1=1.0, w2=1.0, w3=1.0):
    """Algebraic intracellular ferroptosis score; not a probability."""
    if gpx4_conc <= 0:
        raise ValueError("GPX4 concentration must be > 0.")
    if ros_lipid < 0 or fe2_free < 0:
        raise ValueError("ROS lipid and Fe2+ must be >= 0.")
    return w1 / gpx4_conc + w2 * ros_lipid + w3 * fe2_free


def transport_delivery_factor(r_H, xi, sigma=1.0,
                              reference_r_H=20e-9, reference_xi=45e-9):
    """Dimensionless transport factor D_eff/D_ref.

    This is an explicit phenomenological bridge between transport and the
    intracellular score. It is a modelling assumption, not an experimentally
    calibrated pharmacokinetic relationship.
    """
    d_eff = calculate_stokes_einstein_diffusion(sigma, r_H, xi)
    d_ref = calculate_stokes_einstein_diffusion(sigma, reference_r_H, reference_xi)
    return d_eff / d_ref


def evaluate_phi_death(A1, A2, B_miRNA, gpx4_conc, ros_lipid, fe2_free,
                       r_H=None, xi=None, sigma=1.0,
                       w1=1.0, w2=1.0, w3=1.0):
    """Integrated conceptual death score Phi_Death.

    If r_H and xi are supplied, transport modulates intracellular exposure.
    Omitting both preserves the legacy algebraic model for compatibility.
    """
    gate = logic_gate(A1, A2, B_miRNA)
    if gate == 0:
        return 0.0
    score = intracellular_ferroptosis_score(gpx4_conc, ros_lipid, fe2_free, w1, w2, w3)
    if (r_H is None) != (xi is None):
        raise ValueError("r_H and xi must be supplied together.")
    delivery = 1.0 if r_H is None else transport_delivery_factor(r_H, xi, sigma)
    return gate * delivery * score


def latin_hypercube_sampling(bounds, n_samples, rng=None):
    """Latin Hypercube Sampling with an explicit random generator."""
    if n_samples < 2 or not bounds:
        raise ValueError("n_samples >= 2 and at least one bound are required.")
    rng = np.random.default_rng() if rng is None else rng
    k = len(bounds)
    u = rng.random((n_samples, k))
    out = np.empty_like(u)
    for j, (low, high) in enumerate(bounds):
        if high <= low:
            raise ValueError("Each upper bound must exceed its lower bound.")
        perm = rng.permutation(n_samples)
        out[:, j] = (perm + u[:, j]) / n_samples * (high - low) + low
    return out


def calculate_prcc(X, Y, return_p=False):
    """PRCC using ranked residuals and regressions with intercepts."""
    X = np.asarray(X, float); Y = np.asarray(Y, float)
    if X.ndim != 2 or Y.ndim != 1 or len(Y) != len(X):
        raise ValueError("X must be 2-D and Y a matching 1-D vector.")
    n, k = X.shape
    if n <= k + 2:
        raise ValueError("Too few observations for PRCC.")
    xr = np.apply_along_axis(rankdata, 0, X)
    yr = rankdata(Y)
    vals = np.zeros(k)
    for j in range(k):
        idx = [i for i in range(k) if i != j]
        design = np.column_stack([np.ones(n), xr[:, idx]])
        bx = np.linalg.lstsq(design, xr[:, j], rcond=None)[0]
        by = np.linalg.lstsq(design, yr, rcond=None)[0]
        rx = xr[:, j] - design @ bx
        ry = yr - design @ by
        vals[j] = np.corrcoef(rx, ry)[0, 1]
    if not return_p:
        return vals
    df = n - k - 1
    denom = np.maximum(1.0 - vals**2, np.finfo(float).eps)
    stat = vals * np.sqrt(df / denom)
    p = 2 * student_t.sf(np.abs(stat), df)
    return vals, p


def bootstrap_prcc(X, Y, n_boot=500, seed=1234):
    """Non-parametric 95% bootstrap confidence intervals for PRCC."""
    rng = np.random.default_rng(seed)
    n = len(Y); draws = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        try:
            v = calculate_prcc(X[idx], Y[idx])
            if np.all(np.isfinite(v)):
                draws.append(v)
        except (ValueError, np.linalg.LinAlgError):
            pass
    if len(draws) < max(30, n_boot // 2):
        raise RuntimeError("Insufficient valid bootstrap replicates.")
    draws = np.asarray(draws)
    return np.percentile(draws, 2.5, axis=0), np.percentile(draws, 97.5, axis=0)


def simulate_samples(samples):
    """Evaluate integrated tumour model for [r_H, xi, GPX4, ROS, Fe2+]."""
    y = np.empty(len(samples))
    for i, (r_h, xi, gpx4, ros, fe2) in enumerate(samples):
        y[i] = evaluate_phi_death(True, True, False, gpx4, ros, fe2, r_h, xi)
    return y


def run_sensitivity_and_plotting(output_dir="outputs_v3", n_samples=1000,
                                 n_boot=300, seed=42):
    """Run integrated LHS-PRCC, uncertainty estimation and convergence analysis."""
    os.makedirs(output_dir, exist_ok=True)
    bounds = [(5e-9, 40e-9), (10e-9, 80e-9), (0.01, 0.8), (10., 90.), (5., 50.)]
    names = [r"$r_H$", r"$\xi$", "GPX4", "ROS lipid", r"Fe$^{2+}$"]
    rng = np.random.default_rng(seed)
    samples = latin_hypercube_sampling(bounds, n_samples, rng)
    outputs = simulate_samples(samples)
    prcc, pvals = calculate_prcc(samples, outputs, return_p=True)
    ci_low, ci_high = bootstrap_prcc(samples, outputs, n_boot=n_boot, seed=seed + 1)

    fig, axes = plt.subplots(1, 3, figsize=(17, 5.5))
    g = np.linspace(0.01, 1.0, 150)
    phi = [evaluate_phi_death(True, True, False, x, 50, 20, 20e-9, 45e-9) for x in g]
    axes[0].plot(g, phi, linewidth=2.2)
    axes[0].set(title=r"A. Integrated ferroptosis dynamics ($\Phi_{Death}$)",
                xlabel="GPX4 concentration", ylabel=r"Conceptual death score ($\Phi_{Death}$)")
    axes[0].grid(True, linestyle="--", alpha=.45)

    ypos = np.arange(len(names))
    err = np.vstack([prcc-ci_low, ci_high-prcc])
    axes[1].barh(ypos, prcc, xerr=err, alpha=.8, edgecolor="black", capsize=3)
    axes[1].set_yticks(ypos, names); axes[1].axvline(0, linewidth=1, linestyle="--")
    axes[1].set_xlim(-1.05, 1.05)
    axes[1].set(title="B. LHS-PRCC with bootstrap 95% CI", xlabel="PRCC")
    axes[1].grid(True, axis="x", linestyle="--", alpha=.45)

    ns = [100, 250, 500, n_samples] if n_samples >= 500 else [100, n_samples]
    ns = sorted(set(n for n in ns if n <= n_samples))
    conv = np.vstack([calculate_prcc(samples[:n], outputs[:n]) for n in ns])
    for j, name in enumerate(names):
        axes[2].plot(ns, conv[:, j], marker="o", label=name)
    axes[2].axhline(0, linewidth=1, linestyle="--")
    axes[2].set(title="C. PRCC convergence", xlabel="Sample size", ylabel="PRCC", ylim=(-1.05, 1.05))
    axes[2].legend(fontsize=8); axes[2].grid(True, linestyle="--", alpha=.45)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "pdac_integrated_sensitivity_v3.png"), dpi=300)
    plt.close(fig)

    table = np.column_stack([prcc, ci_low, ci_high, pvals])
    np.savetxt(os.path.join(output_dir, "prcc_results.csv"), table, delimiter=",",
               header="prcc,ci95_low,ci95_high,p_value", comments="")
    return dict(names=names, prcc=prcc, ci_low=ci_low, ci_high=ci_high, pvals=pvals)


if __name__ == "__main__":
    result = run_sensitivity_and_plotting()
    for name, r, lo, hi, p in zip(result["names"], result["prcc"], result["ci_low"], result["ci_high"], result["pvals"]):
        print(f"{name:10s} PRCC={r:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}]  p={p:.3g}")
