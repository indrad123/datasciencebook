"""Reusable anomaly-detection helpers for Chapter 41."""
from __future__ import annotations
import numpy as np
from sklearn.base import clone

def finite_matrix(values):
    x=np.asarray(values,dtype=float)
    if x.ndim!=2 or len(x)<2 or x.shape[1]<1 or not np.isfinite(x).all():
        raise ValueError("values must be a finite matrix with at least two rows")
    return x

def robust_fit(values):
    x=finite_matrix(values); centre=np.median(x,axis=0); mad=np.median(np.abs(x-centre),axis=0)
    if np.any(mad==0): raise ValueError("every feature must have non-zero MAD")
    return centre,1.4826*mad

def robust_scores(values,centre,scale):
    x=finite_matrix(values); c=np.asarray(centre,float); s=np.asarray(scale,float)
    if c.shape!=(x.shape[1],) or s.shape!=c.shape or np.any(s<=0): raise ValueError("invalid robust parameters")
    return np.max(np.abs((x-c)/s),axis=1)

def fit_detector(model,values,seed=41):
    x=finite_matrix(values); fitted=clone(model)
    if "random_state" in fitted.get_params(): fitted.set_params(random_state=seed)
    fitted.fit(x); return fitted

def anomaly_scores(model,values):
    x=finite_matrix(values)
    if not hasattr(model,"score_samples"): raise ValueError("model must provide score_samples")
    return -np.asarray(model.score_samples(x),float)

def select_for_review(scores,capacity):
    s=np.asarray(scores,float)
    if s.ndim!=1 or len(s)==0 or not np.isfinite(s).all() or not isinstance(capacity,int) or not 1<=capacity<=len(s):
        raise ValueError("scores and capacity are invalid")
    return np.argsort(-s,kind="stable")[:capacity]

def precision_at_capacity(labels,selected):
    y=np.asarray(labels); idx=np.asarray(selected)
    if y.ndim!=1 or idx.ndim!=1 or len(idx)==0 or np.any(idx<0) or np.any(idx>=len(y)):
        raise ValueError("labels and selected indices are invalid")
    return float(np.mean(y[idx].astype(bool)))
