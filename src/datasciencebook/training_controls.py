"""Initialization, regularisation, and normalization helpers."""
import numpy as np

def initialize_weights(fan_in,fan_out,scheme="xavier",seed=0):
    if fan_in<1 or fan_out<1: raise ValueError("fan sizes must be positive")
    r=np.random.default_rng(seed)
    if scheme=="xavier": scale=np.sqrt(2/(fan_in+fan_out))
    elif scheme=="he": scale=np.sqrt(2/fan_in)
    elif scheme=="small": scale=.01
    else: raise ValueError("unknown scheme")
    return r.normal(0,scale,(fan_in,fan_out))

def l2_penalty(weights,strength):
    if strength<0: raise ValueError("strength cannot be negative")
    arrays=[np.asarray(w,float) for w in weights]
    if any(not np.all(np.isfinite(w)) for w in arrays): raise ValueError("weights must be finite")
    return float(.5*strength*sum(np.sum(w*w) for w in arrays))

def dropout(x,rate,training=True,seed=0):
    x=np.asarray(x,float)
    if not 0<=rate<1 or not np.all(np.isfinite(x)): raise ValueError("invalid dropout input")
    if not training or rate==0:return x.copy()
    mask=np.random.default_rng(seed).random(x.shape)>=rate
    return x*mask/(1-rate)

def fit_standardizer(X,epsilon=1e-8):
    X=np.asarray(X,float)
    if X.ndim!=2 or len(X)==0 or not np.all(np.isfinite(X)): raise ValueError("X must be a finite matrix")
    return {"mean":X.mean(0),"scale":np.sqrt(X.var(0)+epsilon)}

def apply_standardizer(X,state):
    X=np.asarray(X,float);mean=np.asarray(state["mean"]);scale=np.asarray(state["scale"])
    if X.ndim!=2 or X.shape[1]!=mean.size or scale.shape!=mean.shape or np.any(scale<=0): raise ValueError("incompatible state")
    return (X-mean)/scale

def batch_normalize(X,gamma=None,beta=None,epsilon=1e-5):
    X=np.asarray(X,float)
    if X.ndim!=2 or len(X)==0 or epsilon<=0: raise ValueError("invalid batch")
    gamma=np.ones(X.shape[1]) if gamma is None else np.asarray(gamma,float);beta=np.zeros(X.shape[1]) if beta is None else np.asarray(beta,float)
    if gamma.shape!=(X.shape[1],) or beta.shape!=gamma.shape: raise ValueError("invalid affine parameters")
    normalized=(X-X.mean(0))/np.sqrt(X.var(0)+epsilon)
    return gamma*normalized+beta,{"mean":X.mean(0),"variance":X.var(0)}

def activation_variances(X,layer_sizes,scheme="xavier",seed=0):
    a=np.asarray(X,float);result=[]
    for i,size in enumerate(layer_sizes):
        W=initialize_weights(a.shape[1],size,scheme,seed+i);a=np.tanh(a@W);result.append(float(a.var()))
    return np.asarray(result)
