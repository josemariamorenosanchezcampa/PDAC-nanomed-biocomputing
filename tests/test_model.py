import numpy as np
from pdac_model.core import diffusion,phi_death,death_probability
from pdac_model.sensitivity import sobol_jansen
from pdac_model.dynamics import simulate_ode,simulate_sde
from pdac_model.spatial import stroma_map,diffuse_2d

def test_diffusion_physics():
    assert diffusion(1,10e-9,45e-9)>diffusion(1,30e-9,45e-9)
    assert diffusion(1,20e-9,70e-9)>diffusion(1,20e-9,20e-9)
def test_gate_and_response():
    assert phi_death(.2,50,20,b_mirna=True)==0
    assert phi_death(.1,50,20)>phi_death(.4,50,20)
def test_probability_bounds():
    p=death_probability(np.array([-1e6,0,1e6])); assert np.all((p>=0)&(p<=1))
def test_dynamics_finite_reproducible():
    t=np.linspace(0,2,50); a=simulate_ode(t); b=simulate_sde(t,seed=1); c=simulate_sde(t,seed=1)
    assert np.isfinite(a).all() and np.allclose(b,c)
def test_spatial_solver_nonnegative():
    x,_,_,_,D=stroma_map(grid=31); c,_=diffuse_2d(D,20,x[1]-x[0]); assert np.min(c)>=0 and np.isfinite(c).all()

def test_spatial_constant_field_symmetry():
    D=np.ones((21,21))*0.5
    c,_=diffuse_2d(D,40,1.0,decay=0.0)
    assert np.allclose(c[:,0],c[:,-1],atol=1e-12)
    assert np.allclose(c[0,:],1.0)
def test_sobol_additive_sanity():
    bounds=[(0,1),(0,1)]
    def m(X): return X[:,0]+.2*X[:,1]
    s1,st=sobol_jansen(m,bounds,n=100000,seed=3)
    assert st[0]>st[1] and s1[0]>s1[1]
    expected=np.array([1/1.04, .04/1.04])
    assert np.allclose(s1,expected,atol=.03) and np.allclose(st,expected,atol=.03)
