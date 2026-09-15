# Model equations — v4.0.0

## 1. Transport

`D0 = k_B T / (6 π η r_H)`

`D_eff = 0.5 σ D0 exp[-γ (r_H/ξ)^α]`

The steric term is phenomenological. `r_H` is hydrodynamic radius and `ξ` an effective stromal correlation length.

## 2. Delivery

`F_delivery = D_eff / D_ref`

A release extension can be written `f_release(t)=1-exp(-k_rel t)` and multiplied by the delivery factor.

## 3. Reduced intracellular score

`S = w1/GPX4 + w2 ROS + w3 Fe2`

This is a phenomenological model-unit score. Inputs must be normalized to declared reference scales, or the weights must carry reciprocal units so the terms are commensurate. The bundled defaults are illustrative and are not universal biochemical constants.

`Phi = gate × F_delivery × S`

`P = 1/[1+exp(-(Phi-midpoint)/scale)]`

The logistic output is a normalized model response unless probability calibration is demonstrated.

## 4. Spatial transport

`∂C/∂t = ∇·(D(x,y)∇C) - k_u C - k_deg C`

The bundled solver implements this heterogeneous operator in conservative face-flux form with harmonic face diffusivities. It is a qualitative prototype and not patient-specific transport.

## 5. Temporal dynamics

The deterministic model tracks GPX4-like `G`, ROS-like `R` and lipid-peroxidation `L` states. The stochastic version adds Wiener increments and is integrated with Euler-Maruyama. Noise amplitudes are model parameters until estimated from repeated measurements.

## 6. Sensitivity

`PRCC_i = corr(resid(rank(X_i)), resid(rank(Y)))`

`S_i = Var_Xi(E[Y|X_i])/Var(Y)`

`S_Ti = 1 - Var_X~i(E[Y|X~i])/Var(Y)`

## 7. Calibration

`theta* = argmin_theta Σ(y_obs-y_model(theta))²`

Metrics: R², RMSE and MAE. Synthetic benchmarks verify software behavior only.

## 8. Dosing optimization

`u* = argmin_u J(u)`

The objective rewards a modeled terminal response and penalizes exposure subject to dose bounds/budget. Its solution is model-optimal, not clinically recommended.
