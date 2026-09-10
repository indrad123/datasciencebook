"""Clustering helpers for Chapter 39."""
from __future__ import annotations
import numpy as np
from sklearn.base import clone
from sklearn.metrics import silhouette_samples,silhouette_score,adjusted_rand_score

def finite_matrix(values):
    x=np.asarray(values,dtype=float)
    if x.ndim!=2 or len(x)<2 or not np.isfinite(x).all(): raise ValueError("values must be a finite matrix with at least two rows")
    return x

def fit_scaler(values):
    x=finite_matrix(values); center=x.mean(0); scale=x.std(0); scale[scale==0]=1; return center,scale

def apply_scaler(values,center,scale):
    x=finite_matrix(values); c=np.asarray(center); s=np.asarray(scale)
    if x.shape[1]!=len(c) or len(c)!=len(s) or np.any(s<=0):raise ValueError("invalid scaler")
    return (x-c)/s

def fit_clusters(model,values,seed=39):
    x=finite_matrix(values); m=clone(model)
    if "random_state" in m.get_params():m.set_params(random_state=seed)
    labels=m.fit_predict(x); return m,labels

def cluster_profile(values,labels):
    x=finite_matrix(values); lab=np.asarray(labels)
    if len(lab)!=len(x):raise ValueError("labels must align")
    return {int(k):{"count":int((lab==k).sum()),"mean":x[lab==k].mean(0).tolist()} for k in sorted(set(lab))}

def silhouette_report(values,labels):
    x=finite_matrix(values); lab=np.asarray(labels); groups=set(lab)
    if len(lab)!=len(x) or len(groups)<2 or len(groups)>=len(x):raise ValueError("silhouette requires aligned non-trivial clusters")
    scores=silhouette_samples(x,lab)
    return {"mean":float(silhouette_score(x,lab)),"minimum":float(scores.min()),"negative_count":int((scores<0).sum())}

def partition_agreement(labels_a,labels_b):
    a=np.asarray(labels_a);b=np.asarray(labels_b)
    if len(a)==0 or len(a)!=len(b):raise ValueError("partitions must align")
    return float(adjusted_rand_score(a,b))
