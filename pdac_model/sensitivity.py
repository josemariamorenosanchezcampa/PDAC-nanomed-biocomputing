"""LHS/PRCC and variance-based Sobol estimators."""
import numpy as np
from scipy.stats import rankdata, t as student_t

def lhs(bounds,n,seed=42):
    rng=np.random.default_rng(seed); k=len(bounds); u=rng.random((n,k)); x=np.empty_like(u)
    for j,(lo,hi) in enumerate(bounds):
        p=rng.permutation(n); x[:,j]=(p+u[:,j])/n*(hi-lo)+lo
    return x

def prcc(X,y):
    X=np.asarray(X,float); y=np.asarray(y,float); n,k=X.shape
    xr=np.apply_along_axis(rankdata,0,X); yr=rankdata(y); vals=[]
    for j in range(k):
        z=np.column_stack([np.ones(n),np.delete(xr,j,axis=1)])
        rx=xr[:,j]-z@np.linalg.lstsq(z,xr[:,j],rcond=None)[0]
        ry=yr-z@np.linalg.lstsq(z,yr,rcond=None)[0]
        vals.append(np.corrcoef(rx,ry)[0,1])
    vals=np.asarray(vals); df=n-k-1
    p=2*student_t.sf(np.abs(vals*np.sqrt(df/np.maximum(1-vals**2,np.finfo(float).eps))),df)
    return vals,p

def bootstrap_prcc(X,y,n_boot=300,seed=43):
    rng=np.random.default_rng(seed); n=len(y); d=[]
    for _ in range(n_boot):
        ix=rng.integers(0,n,n); d.append(prcc(X[ix],np.asarray(y)[ix])[0])
    d=np.asarray(d); return np.quantile(d,.025,axis=0),np.quantile(d,.975,axis=0)

def sobol_jansen(model,bounds,n=4096,seed=44):
    """Estimate first/total Sobol indices using independent A/B matrices.

    Uses Saltelli first-order covariance estimator and Jansen total-effect estimator.
    Returns S1, ST. Inputs are assumed mutually independent and uniform over bounds.
    """
    rng=np.random.default_rng(seed); k=len(bounds)
    def scale(U):
        lo=np.array([b[0] for b in bounds]); hi=np.array([b[1] for b in bounds]); return lo+U*(hi-lo)
    A=scale(rng.random((n,k))); B=scale(rng.random((n,k)))
    fA=np.asarray(model(A)); fB=np.asarray(model(B)); var=np.var(np.r_[fA,fB],ddof=1)
    if var <= 0: raise ValueError("model output variance is zero")
    s1=np.empty(k); st=np.empty(k)
    for j in range(k):
        AB=A.copy(); AB[:,j]=B[:,j]; fAB=np.asarray(model(AB))
        s1[j]=np.mean(fB*(fAB-fA))/var
        st[j]=np.mean((fA-fAB)**2)/(2*var)
    return s1,st
