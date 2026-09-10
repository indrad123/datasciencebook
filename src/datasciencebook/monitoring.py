"""Small production-model monitoring utilities."""
import numpy as np
def _array(x):
 a=np.asarray(x,dtype=float)
 if a.ndim!=1 or len(a)==0 or not np.all(np.isfinite(a)): raise ValueError("finite nonempty vector required")
 return a
def population_stability_index(reference,current,bins=10,epsilon=1e-6):
 r,c=_array(reference),_array(current)
 if bins<2: raise ValueError("at least two bins required")
 edges=np.unique(np.quantile(r,np.linspace(0,1,bins+1)));edges[0]=-np.inf;edges[-1]=np.inf
 pr=np.histogram(r,edges)[0]/len(r);pc=np.histogram(c,edges)[0]/len(c);pr=np.maximum(pr,epsilon);pc=np.maximum(pc,epsilon)
 return float(np.sum((pc-pr)*np.log(pc/pr)))
def latency_summary(milliseconds):
 x=_array(milliseconds)
 if np.any(x<0): raise ValueError("latency cannot be negative")
 return {"p50":float(np.quantile(x,.5)),"p95":float(np.quantile(x,.95)),"p99":float(np.quantile(x,.99))}
def missing_rate(values):
 a=np.asarray(values,dtype=float)
 if a.ndim!=1 or len(a)==0: raise ValueError("nonempty vector required")
 return float(np.mean(np.isnan(a)))
def breach(value,warning,critical,higher_is_worse=True):
 if higher_is_worse:return "critical" if value>=critical else "warning" if value>=warning else "ok"
 return "critical" if value<=critical else "warning" if value<=warning else "ok"
