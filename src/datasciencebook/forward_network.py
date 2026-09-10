"""Forward propagation utilities for small dense neural networks."""
import numpy as np

def _finite(x,name):
    a=np.asarray(x,dtype=float)
    if not np.all(np.isfinite(a)): raise ValueError(f"{name} must be finite")
    return a

def activation(x,kind):
    x=_finite(x,"x")
    if kind=="identity": return x
    if kind=="relu": return np.maximum(x,0)
    if kind=="tanh": return np.tanh(x)
    if kind=="sigmoid":
        out=np.empty_like(x); pos=x>=0; out[pos]=1/(1+np.exp(-x[pos])); ez=np.exp(x[~pos]); out[~pos]=ez/(1+ez); return out
    if kind=="softmax":
        if x.ndim<1: raise ValueError("softmax needs a vector or matrix")
        shifted=x-np.max(x,axis=-1,keepdims=True); e=np.exp(shifted); return e/e.sum(axis=-1,keepdims=True)
    raise ValueError("unknown activation")

def dense_forward(X,weights,bias,kind="relu"):
    X=_finite(X,"X"); W=_finite(weights,"weights"); b=_finite(bias,"bias")
    if X.ndim!=2 or W.ndim!=2 or b.ndim!=1 or X.shape[1]!=W.shape[0] or W.shape[1]!=b.size: raise ValueError("incompatible dense-layer shapes")
    z=X@W+b
    return {"preactivation":z,"activation":activation(z,kind)}

def forward_network(X,layers,return_trace=False):
    a=_finite(X,"X")
    if a.ndim!=2 or not layers: raise ValueError("X must be a matrix and layers cannot be empty")
    trace=[]
    for layer in layers:
        result=dense_forward(a,layer["weights"],layer["bias"],layer.get("activation","relu")); trace.append(result); a=result["activation"]
    return (a,trace) if return_trace else a

def multiclass_cross_entropy(y,probabilities,epsilon=1e-12):
    y=np.asarray(y); p=_finite(probabilities,"probabilities")
    if y.ndim!=1 or p.ndim!=2 or len(y)!=len(p) or np.any(y<0) or np.any(y>=p.shape[1]): raise ValueError("labels and probabilities are incompatible")
    if np.any(p<0) or not np.allclose(p.sum(axis=1),1): raise ValueError("rows must be probabilities")
    return float(-np.mean(np.log(np.clip(p[np.arange(len(y)),y.astype(int)],epsilon,1))))

def parameter_count(layers):
    total=0
    for layer in layers:
        W=np.asarray(layer["weights"]); b=np.asarray(layer["bias"])
        if W.ndim!=2 or b.ndim!=1 or W.shape[1]!=b.size: raise ValueError("invalid layer")
        total+=W.size+b.size
    return int(total)
