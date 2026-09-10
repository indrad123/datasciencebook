"""Transparent representation and latent-space utilities."""
import numpy as np

def fit_linear_autoencoder(data, latent_dimension):
    x=np.asarray(data,float)
    if x.ndim!=2 or x.shape[0]<2 or not np.all(np.isfinite(x)): raise ValueError("data must be a finite matrix with at least two rows")
    if not 1<=latent_dimension<x.shape[1]: raise ValueError("latent dimension must be smaller than feature count")
    mean=x.mean(axis=0); _,_,vt=np.linalg.svd(x-mean,full_matrices=False)
    return mean,vt[:latent_dimension].T

def encode(data, mean, components):
    x=np.asarray(data,float); m=np.asarray(mean,float); c=np.asarray(components,float)
    if x.ndim!=2 or m.ndim!=1 or c.ndim!=2 or x.shape[1]!=m.size or c.shape[0]!=m.size: raise ValueError("incompatible encoder shapes")
    return (x-m)@c

def decode(latent, mean, components):
    z=np.asarray(latent,float);m=np.asarray(mean,float);c=np.asarray(components,float)
    if z.ndim!=2 or c.ndim!=2 or z.shape[1]!=c.shape[1] or m.size!=c.shape[0]: raise ValueError("incompatible decoder shapes")
    return z@c.T+m

def reconstruction_error(data, reconstruction):
    x=np.asarray(data,float);r=np.asarray(reconstruction,float)
    if x.shape!=r.shape or x.ndim!=2 or not np.all(np.isfinite(x)) or not np.all(np.isfinite(r)): raise ValueError("inputs must be equal finite matrices")
    return np.mean((x-r)**2,axis=1)

def interpolate_latent(start, end, steps):
    a=np.asarray(start,float);b=np.asarray(end,float)
    if a.shape!=b.shape or a.ndim!=1 or steps<2: raise ValueError("vectors must match and steps must exceed one")
    return np.linspace(a,b,steps)

def reparameterize(mean, log_variance, noise):
    mean,log_variance,noise=(np.asarray(v,float) for v in (mean,log_variance,noise))
    if mean.shape!=log_variance.shape or mean.shape!=noise.shape or not np.all(np.isfinite(mean+log_variance+noise)): raise ValueError("inputs must be equal finite arrays")
    return mean+np.exp(0.5*log_variance)*noise
