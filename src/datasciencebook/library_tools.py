"""Inspection helpers for Appendix B library examples."""
from importlib import import_module
import numpy as np

def array_report(values):
    x=np.asarray(values)
    if x.size==0 or not np.issubdtype(x.dtype,np.number) or not np.isfinite(x.astype(float)).all():
        raise ValueError("values must be a finite numeric array")
    return {"shape":x.shape,"ndim":x.ndim,"dtype":str(x.dtype),"mean":float(x.mean())}

def frame_contract(frame, required, unique=None):
    if not hasattr(frame,"columns") or not hasattr(frame,"isna"):
        raise ValueError("frame must be dataframe-like")
    required=list(required)
    missing=[c for c in required if c not in frame.columns]
    duplicate_rows=int(frame.duplicated(subset=unique).sum()) if unique else int(frame.duplicated().sum())
    return {"rows":int(len(frame)),"columns":int(len(frame.columns)),"missing_columns":missing,
            "missing_values":int(frame[required].isna().sum().sum()) if not missing else None,
            "duplicate_rows":duplicate_rows,"valid":not missing and duplicate_rows==0 and int(frame[required].isna().sum().sum())==0}

def installed_versions(names):
    output={}
    for name in names:
        if not isinstance(name,str) or not name:
            raise ValueError("package names must be nonempty strings")
        module=import_module(name)
        output[name]=getattr(module,"__version__","unknown")
    return output
