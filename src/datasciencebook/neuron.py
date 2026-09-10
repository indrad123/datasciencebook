"""Small, transparent utilities for a single artificial neuron."""
import numpy as np

def _array(values, name):
    a=np.asarray(values,dtype=float)
    if not np.all(np.isfinite(a)): raise ValueError(f"{name} must be finite")
    return a

def linear_output(x, weights, bias=0.0):
    x=_array(x,"x"); w=_array(weights,"weights")
    if x.ndim!=1 or w.ndim!=1 or x.shape!=w.shape: raise ValueError("x and weights must be equal-length vectors")
    if not np.isfinite(bias): raise ValueError("bias must be finite")
    return float(x@w+bias)

def sigmoid(z):
    z=_array(z,"z"); out=np.empty_like(z)
    positive=z>=0; out[positive]=1/(1+np.exp(-z[positive])); ez=np.exp(z[~positive]); out[~positive]=ez/(1+ez)
    return float(out) if out.ndim==0 else out

def binary_cross_entropy(y, probability, epsilon=1e-12):
    y=_array(y,"y"); p=_array(probability,"probability")
    if y.shape!=p.shape or np.any((y!=0)&(y!=1)): raise ValueError("y must be binary and match probability")
    if np.any((p<0)|(p>1)) or not 0<epsilon<.5: raise ValueError("probabilities or epsilon are invalid")
    p=np.clip(p,epsilon,1-epsilon)
    return float(np.mean(-(y*np.log(p)+(1-y)*np.log(1-p))))

def neuron_probabilities(X, weights, bias=0.0):
    X=_array(X,"X"); w=_array(weights,"weights")
    if X.ndim!=2 or w.ndim!=1 or X.shape[1]!=w.size: raise ValueError("X and weights have incompatible shapes")
    return sigmoid(X@w+float(bias))

def train_logistic_neuron(X, y, learning_rate=0.1, epochs=1000):
    X=_array(X,"X"); y=_array(y,"y")
    if X.ndim!=2 or y.ndim!=1 or len(y)!=len(X) or len(y)==0: raise ValueError("X and y have incompatible shapes")
    if np.any((y!=0)&(y!=1)): raise ValueError("y must be binary")
    if learning_rate<=0 or epochs<1 or int(epochs)!=epochs: raise ValueError("learning_rate and epochs must be positive")
    w=np.zeros(X.shape[1]); b=0.0; history=[]
    for _ in range(int(epochs)):
        p=sigmoid(X@w+b); history.append(binary_cross_entropy(y,p)); error=p-y
        w-=learning_rate*(X.T@error/len(X)); b-=learning_rate*float(np.mean(error))
    return {"weights":w,"bias":b,"loss_history":np.asarray(history)}

def classify(probabilities, threshold=0.5):
    p=_array(probabilities,"probabilities")
    if np.any((p<0)|(p>1)) or not 0<threshold<1: raise ValueError("invalid probability or threshold")
    return (p>=threshold).astype(int)
