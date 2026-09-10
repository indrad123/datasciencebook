"""Error-analysis and deployment-readiness utilities."""
import numpy as np

def error_labels(actual, probability, threshold=0.5):
    y=np.asarray(actual);p=np.asarray(probability,float)
    if y.shape!=p.shape or y.ndim!=1 or not np.all(np.isin(y,[0,1])) or not np.all(np.isfinite(p)) or np.any((p<0)|(p>1)) or not 0<=threshold<=1: raise ValueError("invalid binary predictions")
    pred=(p>=threshold).astype(int)
    labels=np.full(y.size,"TN",object);labels[(y==1)&(pred==1)]="TP";labels[(y==0)&(pred==1)]="FP";labels[(y==1)&(pred==0)]="FN"
    return labels

def slice_error_rates(actual, probability, groups, threshold=0.5):
    y=np.asarray(actual);p=np.asarray(probability,float);g=np.asarray(groups)
    if y.shape!=p.shape or y.shape!=g.shape: raise ValueError("columns must align")
    labels=error_labels(y,p,threshold);rows=[]
    for value in np.unique(g):
        take=g==value;rows.append({"group":str(value),"count":int(take.sum()),"error_rate":float(np.mean(np.isin(labels[take],["FP","FN"]))),"false_negative_rate":float(np.mean(labels[take]=="FN"))})
    return rows

def review_queue(probability, capacity, centre=0.5):
    p=np.asarray(probability,float)
    if p.ndim!=1 or capacity<1 or capacity>p.size or not np.all(np.isfinite(p)) or np.any((p<0)|(p>1)): raise ValueError("invalid queue inputs")
    distance=np.round(np.abs(p-centre),12)
    return np.lexsort((np.arange(p.size),distance))[:capacity]

def readiness_report(checks):
    required=("owner","intended_use","test_slices","fallback","monitoring","rollback")
    if not isinstance(checks,dict): raise ValueError("checks must be a mapping")
    missing=[name for name in required if not checks.get(name)]
    return {"ready":not missing,"missing":missing}
