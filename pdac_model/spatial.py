"""2-D heterogeneous stroma and conservative diffusion-reaction prototype."""
import numpy as np
from .core import diffusion

def stroma_map(grid=81,size_um=100.,r_h_m=20e-9):
    x=np.linspace(0,size_um,grid); X,Y=np.meshgrid(x,x); dist=np.sqrt((X-size_um/2)**2+(Y-size_um/2)**2)
    xi=20e-9+60e-9*(1-np.exp(-dist/30.))
    D=np.vectorize(lambda q: diffusion(1.,r_h_m,q))(xi)*1e12 # um2/s
    return x,X,Y,xi,D

def _harmonic(a,b):
    """Harmonic face diffusivity; returns zero if both neighboring values are zero."""
    a=np.asarray(a,float); b=np.asarray(b,float)
    return np.where(a+b>0, 2*a*b/(a+b), 0.0)

def diffuse_2d(D,steps=300,dx_um=1.25,decay=.0005,source_strength=1.):
    """Solve dC/dt = div(D grad C) - decay*C with conservative face fluxes.

    The left/top array edge (row 0) is a fixed normalized source boundary. The
    remaining outer boundaries are zero-flux. D may vary spatially. Harmonic
    face averaging preserves flux continuity across heterogeneous interfaces.
    This remains a qualitative research prototype, not patient-specific transport.
    """
    D=np.asarray(D,float)
    if D.ndim!=2 or D.size==0 or np.any(~np.isfinite(D)) or np.any(D<0):
        raise ValueError("D must be a finite non-negative 2-D array")
    if dx_um<=0 or steps<0 or decay<0:
        raise ValueError("invalid solver parameter")
    c=np.zeros_like(D); c[0,:]=source_strength
    maxD=float(np.max(D))
    dt=.2*dx_um**2/(4*maxD+1e-12)
    for _ in range(int(steps)):
        # Face diffusivities. Boundary faces not represented here have zero flux.
        De=_harmonic(D[:,:-1],D[:,1:])
        Ds=_harmonic(D[:-1,:],D[1:,:])
        fx=np.zeros((D.shape[0],D.shape[1]+1))
        fy=np.zeros((D.shape[0]+1,D.shape[1]))
        fx[:,1:-1]=De*(c[:,1:]-c[:,:-1])/dx_um
        fy[1:-1,:]=Ds*(c[1:,:]-c[:-1,:])/dx_um
        div=(fx[:,1:]-fx[:,:-1]+fy[1:,:]-fy[:-1,:])/dx_um
        c=np.maximum(c+dt*(div-decay*c),0.0)
        c[0,:]=source_strength
    return c,dt*steps
