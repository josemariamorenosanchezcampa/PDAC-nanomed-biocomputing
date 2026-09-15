"""Deterministic and stochastic ferroptosis dynamics."""
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t,y,exposure,theta):
    g,r,l=y
    kg,kdg,kdrug,kros,kdetox,kperox,krepair=theta
    dg=kg-kdg*g-kdrug*exposure*g
    dr=kros*exposure-kdetox*g*r
    dl=kperox*r-krepair*g*l
    return [dg,dr,dl]

def simulate_ode(t_eval,exposure=1.,y0=(.3,20.,1.),theta=(.03,.05,.12,2.,.08,.12,.05)):
    sol=solve_ivp(lambda t,y: rhs(t,y,exposure,theta),(float(t_eval[0]),float(t_eval[-1])),y0,t_eval=t_eval,rtol=1e-7,atol=1e-9)
    if not sol.success: raise RuntimeError(sol.message)
    return sol.y.T

def simulate_sde(t,exposure=1.,y0=(.3,20.,1.),theta=(.03,.05,.12,2.,.08,.12,.05),noise=(.01,.5,.05),seed=42):
    """Euler-Maruyama SDE prototype; noise amplitudes are hypotheses."""
    t=np.asarray(t,float); y=np.empty((len(t),3)); y[0]=y0; rng=np.random.default_rng(seed)
    for i in range(1,len(t)):
        dt=t[i]-t[i-1]; drift=np.asarray(rhs(t[i-1],y[i-1],exposure,theta)); dw=rng.normal(size=3)*np.sqrt(dt)
        y[i]=np.maximum(y[i-1]+drift*dt+np.asarray(noise)*dw,1e-9)
    return y
