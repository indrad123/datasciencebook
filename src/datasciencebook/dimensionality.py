"""Small, explicit utilities for dimensionality-reduction workflows."""
import numpy as np
from sklearn.decomposition import PCA

def finite_matrix(values):
    x=np.asarray(values,dtype=float)
    if x.ndim!=2 or x.shape[0]<2 or x.shape[1]<1 or not np.isfinite(x).all():
        raise ValueError("values must be a finite two-dimensional matrix with at least two rows")
    return x

def fit_scaler(values):
    x=finite_matrix(values); centre=x.mean(axis=0); scale=x.std(axis=0)
    if np.any(scale==0): raise ValueError("every feature must vary")
    return centre,scale

def apply_scaler(values,centre,scale):
    x=finite_matrix(values); c=np.asarray(centre,float); s=np.asarray(scale,float)
    if c.shape!=(x.shape[1],) or s.shape!=c.shape or np.any(s<=0): raise ValueError("invalid scaling parameters")
    return (x-c)/s

def fit_pca(values,n_components=None,seed=40):
    x=finite_matrix(values)
    if n_components is not None and (not isinstance(n_components,int) or not 1<=n_components<=min(x.shape)):
        raise ValueError("n_components is outside the feasible range")
    model=PCA(n_components=n_components,svd_solver="full",random_state=seed).fit(x)
    return model,model.transform(x)

def variance_summary(model):
    ratio=np.asarray(model.explained_variance_ratio_,float)
    return {"ratio":ratio,"cumulative":np.cumsum(ratio)}

def reconstruction_error(original,reconstructed):
    a=finite_matrix(original); b=finite_matrix(reconstructed)
    if a.shape!=b.shape: raise ValueError("matrices must have the same shape")
    return float(np.sqrt(np.mean((a-b)**2)))

def top_loadings(model,feature_names,top_n=3):
    names=list(feature_names)
    if len(names)!=model.components_.shape[1] or not 1<=top_n<=len(names): raise ValueError("invalid names or top_n")
    result=[]
    for row in model.components_:
        order=np.argsort(np.abs(row))[::-1][:top_n]
        result.append([(names[i],float(row[i])) for i in order])
    return result
