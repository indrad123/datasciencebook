"""Forecast evaluation and inventory-planning helpers for Chapter 59."""
import numpy as np

def finite_vector(values, minimum=1):
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or len(x) < minimum or not np.isfinite(x).all():
        raise ValueError("values must be a finite one-dimensional vector")
    return x

def wape(actual, forecast):
    a, f = finite_vector(actual), finite_vector(forecast)
    if a.shape != f.shape or np.sum(np.abs(a)) == 0:
        raise ValueError("aligned actuals with nonzero scale are required")
    return float(np.sum(np.abs(a - f)) / np.sum(np.abs(a)))

def service_quantile(errors, service_level):
    e = finite_vector(errors, 2)
    if not 0 < service_level < 1:
        raise ValueError("service_level must lie between zero and one")
    return float(np.quantile(e, service_level, method="linear"))

def inventory_position(on_hand, on_order=0, backorders=0):
    values = np.asarray([on_hand, on_order, backorders], dtype=float)
    if not np.isfinite(values).all() or np.any(values < 0):
        raise ValueError("inventory inputs must be finite and nonnegative")
    return float(on_hand + on_order - backorders)

def order_up_to_quantity(target, position, case_pack=1):
    values = np.asarray([target, position, case_pack], dtype=float)
    if not np.isfinite(values).all() or target < 0 or case_pack <= 0:
        raise ValueError("target and position must be finite and case_pack positive")
    raw = max(0.0, target - position)
    return float(np.ceil(raw / case_pack) * case_pack)

def lead_time_target(point_forecast, errors, service_level):
    f = finite_vector(point_forecast)
    buffer = max(0.0, service_quantile(errors, service_level))
    return {"point_demand": float(f.sum()), "safety_stock": buffer,
            "target": float(f.sum() + buffer)}

def newsvendor_cost(demand, stock, holding_cost, shortage_cost):
    d = finite_vector(demand)
    if not np.isfinite([stock, holding_cost, shortage_cost]).all() or stock < 0 or holding_cost < 0 or shortage_cost < 0:
        raise ValueError("stock and costs must be finite and nonnegative")
    leftover = np.maximum(stock - d, 0)
    shortage = np.maximum(d - stock, 0)
    return float(np.mean(holding_cost * leftover + shortage_cost * shortage))

def coherent_total(bottom_forecasts):
    x = np.asarray(bottom_forecasts, dtype=float)
    if x.ndim != 2 or x.size == 0 or not np.isfinite(x).all():
        raise ValueError("bottom_forecasts must be a finite two-dimensional array")
    return x.sum(axis=0)
