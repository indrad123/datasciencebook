"""Two-layer binary network with explicit backpropagation."""
import numpy as np

def _data(X,y):
    X=np.asarray(X,float);y=np.asarray(y,float)
    if X.ndim!=2 or y.ndim!=1 or len(X)!=len(y) or len(y)==0 or not np.all(np.isfinite(X)) or np.any((y!=0)&(y!=1)): raise ValueError("invalid X or y")
    return X,y

def initialize(input_size,hidden_size,seed=0):
    if input_size<1 or hidden_size<1: raise ValueError("sizes must be positive")
    r=np.random.default_rng(seed)
    return {"W1":r.normal(0,np.sqrt(1/input_size),(input_size,hidden_size)),"b1":np.zeros(hidden_size),"W2":r.normal(0,np.sqrt(1/hidden_size),(hidden_size,1)),"b2":np.zeros(1)}

def forward(X,p):
    X=np.asarray(X,float);z1=X@p["W1"]+p["b1"];a1=np.tanh(z1);z2=a1@p["W2"]+p["b2"];prob=1/(1+np.exp(-np.clip(z2,-500,500)))
    return prob[:,0],{"X":X,"a1":a1,"prob":prob}

def loss(y,prob):
    y=np.asarray(y,float);q=np.clip(np.asarray(prob,float),1e-12,1-1e-12)
    return float(np.mean(-(y*np.log(q)+(1-y)*np.log(1-q))))

def gradients(y,p,cache):
    y=np.asarray(y,float)[:,None];n=len(y);dz2=(cache["prob"]-y)/n
    dW2=cache["a1"].T@dz2;db2=dz2.sum(0);da1=dz2@p["W2"].T;dz1=da1*(1-cache["a1"]**2)
    return {"W1":cache["X"].T@dz1,"b1":dz1.sum(0),"W2":dW2,"b2":db2}

def train(X,y,hidden_size=4,learning_rate=.1,epochs=2000,seed=0):
    X,y=_data(X,y)
    if learning_rate<=0 or epochs<1: raise ValueError("invalid training settings")
    p=initialize(X.shape[1],hidden_size,seed);history=[];norms=[]
    for _ in range(int(epochs)):
        prob,c=forward(X,p);history.append(loss(y,prob));g=gradients(y,p,c);norms.append(float(np.sqrt(sum(np.sum(v*v) for v in g.values()))))
        for k in p:p[k]-=learning_rate*g[k]
    return p,np.asarray(history),np.asarray(norms)

def finite_difference(X,y,p,key,index,epsilon=1e-5):
    plus={k:v.copy() for k,v in p.items()};minus={k:v.copy() for k,v in p.items()};plus[key][index]+=epsilon;minus[key][index]-=epsilon
    return (loss(y,forward(X,plus)[0])-loss(y,forward(X,minus)[0]))/(2*epsilon)
