"""Small, dependency-light survival-analysis utilities."""
import numpy as np

def _validate(duration, event):
    d=np.asarray(duration,dtype=float); e=np.asarray(event,dtype=int)
    if d.ndim!=1 or e.ndim!=1 or len(d)!=len(e) or len(d)==0: raise ValueError("aligned nonempty vectors required")
    if not np.all(np.isfinite(d)) or np.any(d<=0): raise ValueError("durations must be positive and finite")
    if not np.all(np.isin(e,[0,1])): raise ValueError("events must be binary")
    return d,e

def kaplan_meier(duration,event):
    """Return product-limit estimates at observed event times."""
    d,e=_validate(duration,event); times=np.unique(d[e==1]); s=1.0; surv=[]; risk=[]; events=[]
    for t in times:
        n=int(np.sum(d>=t)); q=int(np.sum((d==t)&(e==1))); s*=1-q/n
        risk.append(n);events.append(q);surv.append(s)
    return {"time":times,"at_risk":np.asarray(risk),"events":np.asarray(events),"survival":np.asarray(surv)}

def survival_at(curve,times):
    q=np.asarray(times,dtype=float); out=np.ones(q.shape,dtype=float)
    if np.any(q<0): raise ValueError("times must be nonnegative")
    for i,t in np.ndenumerate(q):
        j=np.searchsorted(curve["time"],t,side="right")-1
        if j>=0: out[i]=curve["survival"][j]
    return out

def median_survival(curve):
    hit=np.flatnonzero(curve["survival"]<=.5)
    return float(curve["time"][hit[0]]) if len(hit) else float("inf")

def restricted_mean_survival(curve,tau):
    if not np.isfinite(tau) or tau<=0: raise ValueError("tau must be positive")
    points=np.r_[0,curve["time"][curve["time"]<tau],tau]
    return float(np.sum(np.diff(points)*survival_at(curve,points[:-1])))
