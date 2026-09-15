"""Calibration and external validation utilities."""
import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from .core import ferroptosis_score, death_probability

def predict(X,w,midpoint=75.,scale=15.):
    scores=np.array([ferroptosis_score(g,r,f,w) for g,r,f in X[:,0:3]])
    return death_probability(scores,midpoint,scale)

def fit_weights(X,y,initial=(1,1,1)):
    def loss(w): return np.mean((predict(X,w)-y)**2)
    res=minimize(loss,initial,bounds=[(.001,20)]*3,method='L-BFGS-B')
    return res.x,res.fun,res.success

def metrics(y,p):
    return {'r2':float(r2_score(y,p)),'rmse':float(mean_squared_error(y,p)**.5),'mae':float(mean_absolute_error(y,p))}
