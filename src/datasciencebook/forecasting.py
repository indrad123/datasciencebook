"""Transparent forecasting helpers for Chapter 42."""
import numpy as np

def finite_series(values,min_length=2):
    x=np.asarray(values,dtype=float)
    if x.ndim!=1 or len(x)<min_length or not np.isfinite(x).all(): raise ValueError("values must be a finite one-dimensional series")
    return x

def naive_forecast(history,horizon):
    x=finite_series(history)
    if not isinstance(horizon,int) or horizon<1: raise ValueError("horizon must be positive")
    return np.repeat(x[-1],horizon)

def seasonal_naive_forecast(history,horizon,season):
    x=finite_series(history)
    if not isinstance(season,int) or season<1 or len(x)<season or not isinstance(horizon,int) or horizon<1: raise ValueError("invalid horizon or season")
    return np.resize(x[-season:],horizon)

def drift_forecast(history,horizon):
    x=finite_series(history)
    if not isinstance(horizon,int) or horizon<1: raise ValueError("horizon must be positive")
    slope=(x[-1]-x[0])/(len(x)-1); return x[-1]+slope*np.arange(1,horizon+1)

def mae(actual,predicted):
    a=finite_series(actual);p=finite_series(predicted)
    if a.shape!=p.shape: raise ValueError("series must align")
    return float(np.mean(np.abs(a-p)))

def rmse(actual,predicted):
    a=finite_series(actual);p=finite_series(predicted)
    if a.shape!=p.shape: raise ValueError("series must align")
    return float(np.sqrt(np.mean((a-p)**2)))

def mase(actual,predicted,training,season=1):
    a=finite_series(actual);p=finite_series(predicted);t=finite_series(training,season+1)
    if a.shape!=p.shape or not isinstance(season,int) or season<1: raise ValueError("invalid aligned series or season")
    scale=np.mean(np.abs(t[season:]-t[:-season]))
    if scale==0: raise ValueError("training naive scale is zero")
    return float(np.mean(np.abs(a-p))/scale)

def rolling_origins(length,initial,horizon,step=1):
    if not all(isinstance(v,int) for v in [length,initial,horizon,step]) or initial<2 or horizon<1 or step<1 or initial+horizon>length: raise ValueError("invalid rolling-origin configuration")
    return [(0,end,end,end+horizon) for end in range(initial,length-horizon+1,step)]
