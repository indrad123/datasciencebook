"""Validated numerical-integration helpers for Chapter 10."""

import numpy as np


def _validated_xy(x_values, y_values):
    x = np.asarray(x_values, dtype=float)
    y = np.asarray(y_values, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or x.size != y.size or x.size < 2:
        raise ValueError("x and y must be one-dimensional arrays of equal length at least two")
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("x and y must contain only finite values")
    if not np.all(np.diff(x) > 0):
        raise ValueError("x values must be strictly increasing")
    return x, y


def left_riemann(x_values, y_values):
    """Approximate an integral using left-endpoint rectangles."""
    x, y = _validated_xy(x_values, y_values)
    return float(np.sum(y[:-1] * np.diff(x)))


def trapezoidal(x_values, y_values):
    """Approximate an integral using trapezoids, including unequal intervals."""
    x, y = _validated_xy(x_values, y_values)
    return float(np.sum((y[:-1] + y[1:]) * 0.5 * np.diff(x)))


def cumulative_trapezoidal(x_values, y_values, initial=0.0):
    """Return cumulative trapezoidal accumulation aligned with x."""
    x, y = _validated_xy(x_values, y_values)
    start = float(initial)
    if not np.isfinite(start):
        raise ValueError("initial value must be finite")
    increments = (y[:-1] + y[1:]) * 0.5 * np.diff(x)
    return np.concatenate(([start], start + np.cumsum(increments)))
