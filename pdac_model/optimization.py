"""Constrained dosing optimization over a mechanistic ODE prototype."""
import numpy as np
from scipy.optimize import minimize
from .dynamics import simulate_ode

def optimize_schedule(days=7,n_doses=7,max_daily=1.,total_budget=3.5,exposure_penalty_weight=.2,seed=42,**kwargs):
    """Optimize a model-unit schedule; exposure penalty is not a toxicity model."""
    if "toxicity_weight" in kwargs:
        exposure_penalty_weight=kwargs.pop("toxicity_weight")
    if kwargs:
        raise TypeError(f"unexpected keyword(s): {sorted(kwargs)}")
    t=np.linspace(0,days,141); bins=np.minimum((t/(days/n_doses)).astype(int),n_doses-1)
    def objective(u):
        exposure=u[bins]; # piecewise exposure approximated by repeated short integrations
        y=np.array([.3,20.,1.]); traj=[y.copy()]
        for i in range(1,len(t)):
            seg=simulate_ode(np.array([t[i-1],t[i]]),float(exposure[i-1]),tuple(y))
            y=seg[-1]; traj.append(y.copy())
        lpo=np.asarray(traj)[:,2]; benefit=lpo[-1]; tox=np.trapz(exposure**2,t)
        return -benefit+exposure_penalty_weight*tox
    cons={'type':'ineq','fun':lambda u: total_budget-np.sum(u)}
    res=minimize(objective,np.full(n_doses,total_budget/n_doses),bounds=[(0,max_daily)]*n_doses,constraints=cons,method='SLSQP',options={'maxiter':150})
    return res.x,res.fun,res.success
