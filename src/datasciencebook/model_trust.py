"""Metrics and diagnostics for calibrated, explainable predictions."""
import numpy as np
def _binary(y,p):
 y=np.asarray(y,dtype=int);p=np.asarray(p,dtype=float)
 if y.ndim!=1 or p.ndim!=1 or len(y)!=len(p) or len(y)==0: raise ValueError("aligned nonempty vectors required")
 if not np.all(np.isin(y,[0,1])) or not np.all(np.isfinite(p)) or np.any((p<0)|(p>1)): raise ValueError("binary outcomes and probabilities required")
 return y,p
def brier_score(y,p):
 y,p=_binary(y,p);return float(np.mean((p-y)**2))
def reliability_table(y,p,n_bins=10):
 y,p=_binary(y,p)
 if not isinstance(n_bins,int) or n_bins<2: raise ValueError("n_bins must be at least two")
 idx=np.minimum((p*n_bins).astype(int),n_bins-1);rows=[]
 for b in range(n_bins):
  m=idx==b
  if np.any(m): rows.append((b,int(m.sum()),float(p[m].mean()),float(y[m].mean())))
 return rows
def expected_calibration_error(y,p,n_bins=10):
 rows=reliability_table(y,p,n_bins);n=sum(r[1] for r in rows)
 return float(sum(r[1]/n*abs(r[2]-r[3]) for r in rows))
def permutation_importance(model,x,y,score,seed=0):
 x=np.asarray(x,dtype=float);y=np.asarray(y);base=score(y,model.predict_proba(x)[:,1]);rng=np.random.default_rng(seed);out=[]
 for j in range(x.shape[1]):
  z=x.copy();rng.shuffle(z[:,j]);out.append(score(y,model.predict_proba(z)[:,1])-base)
 return np.asarray(out)
