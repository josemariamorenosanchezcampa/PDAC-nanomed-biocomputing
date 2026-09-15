# Methods — v4.0.0

## 1. Transport
Effective diffusion is Stokes–Einstein diffusion multiplied by a steric-hindrance term and a 0.5·sigma prefactor. A dimensionless delivery factor is D_eff / D_ref. This bridge is phenomenological and requires calibration.

## 2. Intracellular score
The algebraic score is w1/GPX4 + w2·ROS + w3·Fe2. It is a phenomenological score in model units, not a biochemical conservation law or probability. GPX4, ROS and Fe2 must either be normalized to declared reference scales before combination, or the fitted weights must carry the reciprocal units needed to make the terms commensurate. The bundled default values are illustrative model units. A logistic map provides a bounded normalized response and may be interpreted as a probability only after outcome calibration.

## 3. Spatial model
A heterogeneous xi(x,y) field generates D(x,y). The solver discretizes ∇·(D∇C) in conservative flux form, using harmonic face diffusivities across heterogeneous interfaces, zero-flux outer boundaries except for a fixed source boundary, and an explicit time step chosen from the maximum diffusivity. This is a qualitative prototype, not patient-specific transport.

## 4. Dynamics
The deterministic model tracks GPX4-like state G, ROS-like state R, and lipid-peroxidation state L. The SDE version adds Wiener noise and is integrated with Euler–Maruyama. Kinetic constants in the bundled example are illustrative hypotheses.

## 5. Sensitivity
LHS-PRCC uses rank transforms, residual regressions with intercepts, p-values, and bootstrap 95% intervals. Sobol indices are computed from independent A/B Monte Carlo matrices: first-order via a Saltelli covariance estimator and total-effect via the Jansen estimator. Inputs are independent uniforms over declared ranges.

## 6. Calibration
Positive weights are estimated by L-BFGS-B against fractional death. Evaluation reports R², RMSE and MAE. The bundled benchmark is generated synthetically and is a software verification example only.

## 7. Dose optimization
A seven-control piecewise schedule is optimized with SLSQP. The objective rewards final lipid-peroxidation state while penalizing integrated squared exposure and enforcing a total dose budget. This is mathematical optimization under the model, not a recommended human regimen.
