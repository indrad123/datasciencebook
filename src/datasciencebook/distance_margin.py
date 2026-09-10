"""Distance and margin helpers for Chapter 38."""
from __future__ import annotations
import numpy as np
from sklearn.base import clone
from sklearn.metrics import accuracy_score, roc_auc_score

def validate_xy(features,target):
    x=np.asarray(features,dtype=float); y=np.asarray(target)
    if x.ndim!=2 or len(x)==0 or len(x)!=len(y) or not np.isfinite(x).all(): raise ValueError("features and target must be finite and aligned")
    return x,y

def fit_scaler(features):
    x=np.asarray(features,dtype=float)
    if x.ndim!=2 or len(x)==0 or not np.isfinite(x).all(): raise ValueError("features must be a finite matrix")
    mean=x.mean(axis=0); scale=x.std(axis=0); scale[scale==0]=1
    return mean,scale

def apply_scaler(features,mean,scale):
    x=np.asarray(features,dtype=float); mean=np.asarray(mean); scale=np.asarray(scale)
    if x.ndim!=2 or x.shape[1]!=len(mean) or len(mean)!=len(scale) or np.any(scale<=0): raise ValueError("invalid scaling inputs")
    return (x-mean)/scale

def euclidean_distances(query,reference):
    q=np.asarray(query,dtype=float); r=np.asarray(reference,dtype=float)
    if q.ndim!=1 or r.ndim!=2 or r.shape[1]!=len(q): raise ValueError("dimensions do not align")
    return np.sqrt(((r-q)**2).sum(axis=1))

def nearest_indices(query,reference,k):
    d=euclidean_distances(query,reference)
    if not isinstance(k,int) or k<=0 or k>len(d): raise ValueError("k must be a valid positive integer")
    return np.argsort(d,kind="stable")[:k].tolist()

def fit_with_seed(model,features,target,seed=38):
    x,y=validate_xy(features,target); m=clone(model)
    if "random_state" in m.get_params(): m.set_params(random_state=seed)
    return m.fit(x,y)

def binary_report(model,features,target):
    x,y=validate_xy(features,target)
    if not set(np.unique(y))<={0,1}: raise ValueError("target must be binary")
    pred=model.predict(x); result={"accuracy":float(accuracy_score(y,pred))}
    score=model.predict_proba(x)[:,1] if hasattr(model,"predict_proba") else model.decision_function(x)
    result["roc_auc"]=float(roc_auc_score(y,score)); return result

def support_summary(model):
    if not hasattr(model,"support_"): raise ValueError("model has no fitted support vectors")
    return {"total":int(len(model.support_)),"by_class":[int(v) for v in model.n_support_]}
