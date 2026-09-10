"""Small, transparent attention utilities for teaching sequence models."""
import numpy as np

def stable_softmax(values, axis=-1):
    x=np.asarray(values,float)
    if x.size==0 or np.any(np.isnan(x)) or np.any(np.isposinf(x)) or np.any(np.all(np.isneginf(x),axis=axis)): raise ValueError("values must contain a finite option")
    shifted=x-np.max(x,axis=axis,keepdims=True); exp=np.exp(shifted)
    return exp/np.sum(exp,axis=axis,keepdims=True)

def sinusoidal_positions(length, dimension):
    if length<1 or dimension<1: raise ValueError("length and dimension must be positive")
    positions=np.arange(length)[:,None]; indices=np.arange(0,dimension,2)
    angles=positions/np.power(10000.0,indices/dimension)
    result=np.zeros((length,dimension)); result[:,0::2]=np.sin(angles)
    if dimension>1: result[:,1::2]=np.cos(angles[:,:result[:,1::2].shape[1]])
    return result

def causal_mask(length):
    if length<1: raise ValueError("length must be positive")
    return np.tril(np.ones((length,length),dtype=bool))

def padding_mask(lengths, maximum=None):
    lengths=np.asarray(lengths)
    if lengths.ndim!=1 or lengths.size==0 or not np.issubdtype(lengths.dtype,np.integer) or np.any(lengths<0): raise ValueError("lengths must be non-negative integers")
    width=int(lengths.max()) if maximum is None else int(maximum)
    if width<1 or np.any(lengths>width): raise ValueError("maximum is too small")
    return np.arange(width)[None,:] < lengths[:,None]

def scaled_dot_product_attention(query, key, value, mask=None):
    q,k,v=(np.asarray(a,float) for a in (query,key,value))
    if any(a.ndim!=2 or not np.all(np.isfinite(a)) for a in (q,k,v)): raise ValueError("query, key, and value must be finite matrices")
    if q.shape[1]!=k.shape[1] or k.shape[0]!=v.shape[0]: raise ValueError("incompatible attention shapes")
    scores=q@k.T/np.sqrt(q.shape[1])
    if mask is not None:
        m=np.asarray(mask,bool)
        if m.shape!=scores.shape or np.any(~m.all(axis=1) & (m.sum(axis=1)==0)): raise ValueError("mask has an invalid shape or blocked row")
        scores=np.where(m,scores,-np.inf)
    weights=stable_softmax(scores,axis=1)
    return weights@v,weights

def masked_mean(sequence, mask):
    x=np.asarray(sequence,float); m=np.asarray(mask,bool)
    if x.ndim!=3 or m.shape!=x.shape[:2] or np.any(m.sum(axis=1)==0): raise ValueError("incompatible sequence and mask")
    return (x*m[:,:,None]).sum(axis=1)/m.sum(axis=1)[:,None]
