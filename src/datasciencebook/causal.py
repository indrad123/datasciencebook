"""Transparent utilities for introductory causal estimation."""
import numpy as np

def _vectors(*values):
    a=[np.asarray(v,dtype=float) for v in values]
    if not a or any(x.ndim!=1 for x in a) or len({len(x) for x in a})!=1 or len(a[0])==0: raise ValueError("aligned nonempty vectors required")
    if any(not np.all(np.isfinite(x)) for x in a): raise ValueError("finite values required")
    return a

def difference_in_means(outcome,treatment):
    y,t=_vectors(outcome,treatment)
    if not np.all(np.isin(t,[0,1])) or len(np.unique(t))<2: raise ValueError("two binary treatment groups required")
    return float(y[t==1].mean()-y[t==0].mean())

def ipw_weights(treatment,propensity,estimand="ate",clip=.01):
    t,p=_vectors(treatment,propensity)
    if not np.all(np.isin(t,[0,1])) or not 0<clip<.5: raise ValueError("invalid treatment or clip")
    p=np.clip(p,clip,1-clip)
    if estimand=="ate": return t/p+(1-t)/(1-p)
    if estimand=="att": return t+(1-t)*p/(1-p)
    raise ValueError("estimand must be ate or att")

def weighted_effect(outcome,treatment,weights):
    y,t,w=_vectors(outcome,treatment,weights)
    if np.any(w<=0) or not np.all(np.isin(t,[0,1])): raise ValueError("positive weights and binary treatment required")
    return float(np.average(y[t==1],weights=w[t==1])-np.average(y[t==0],weights=w[t==0]))

def standardized_mean_difference(covariate,treatment,weights=None):
    x,t=_vectors(covariate,treatment); w=np.ones(len(x)) if weights is None else _vectors(weights)[0]
    if not np.all(np.isin(t,[0,1])) or np.any(w<=0): raise ValueError("invalid treatment or weights")
    means=[np.average(x[t==g],weights=w[t==g]) for g in [0,1]]
    vars_=[np.average((x[t==g]-means[g])**2,weights=w[t==g]) for g in [0,1]]
    scale=np.sqrt(sum(vars_)/2)
    return float((means[1]-means[0])/scale) if scale else 0.0
