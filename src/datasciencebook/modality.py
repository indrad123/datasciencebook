"""Utilities for comparing model candidates across data modalities."""
import numpy as np

def relative_improvement(baseline, candidate, higher_is_better=True):
    if not np.isfinite(baseline) or not np.isfinite(candidate) or baseline==0: raise ValueError("scores must be finite and baseline non-zero")
    return (candidate-baseline)/abs(baseline) if higher_is_better else (baseline-candidate)/abs(baseline)

def value_per_compute(improvement, training_hours, inference_ms):
    if not np.isfinite(improvement) or training_hours<=0 or inference_ms<=0: raise ValueError("invalid comparison inputs")
    return improvement/(training_hours*np.log1p(inference_ms))

def window_count(length, window, stride=1):
    if length<1 or window<1 or stride<1 or window>length: raise ValueError("invalid window configuration")
    return (length-window)//stride+1

def leakage_safe_split(groups, test_groups):
    g=np.asarray(groups);chosen=set(test_groups)
    if g.ndim!=1 or g.size==0 or not chosen: raise ValueError("groups and test groups are required")
    test=np.array([v in chosen for v in g]);
    if test.all() or not test.any(): raise ValueError("split must contain train and test rows")
    return ~test,test

def candidate_summary(names, quality, training_hours, inference_ms):
    if not (len(names)==len(quality)==len(training_hours)==len(inference_ms)) or not names: raise ValueError("candidate columns must align")
    rows=[]
    for n,q,h,m in zip(names,quality,training_hours,inference_ms):
        if h<=0 or m<=0 or not np.isfinite(q): raise ValueError("invalid candidate value")
        rows.append({"name":str(n),"quality":float(q),"training_hours":float(h),"inference_ms":float(m)})
    return rows
