"""Rate-of-change and numerical-derivative helpers for Chapter 9."""

import math


def _finite_number(value, name):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def average_rate(start_value, end_value, start_time, end_time):
    """Return change in value divided by change in time."""
    y0 = _finite_number(start_value, "start_value")
    y1 = _finite_number(end_value, "end_value")
    x0 = _finite_number(start_time, "start_time")
    x1 = _finite_number(end_time, "end_time")
    if x1 == x0:
        raise ValueError("time interval must be non-zero")
    return (y1 - y0) / (x1 - x0)


def forward_difference(function, point, step=1e-5):
    """Approximate a derivative with a forward difference."""
    x = _finite_number(point, "point")
    h = _finite_number(step, "step")
    if h == 0:
        raise ValueError("step must be non-zero")
    return (function(x + h) - function(x)) / h


def central_difference(function, point, step=1e-5):
    """Approximate a derivative with a centred difference."""
    x = _finite_number(point, "point")
    h = _finite_number(step, "step")
    if h == 0:
        raise ValueError("step must be non-zero")
    return (function(x + h) - function(x - h)) / (2 * h)


def tangent_line(function, point, inputs, step=1e-5):
    """Evaluate the numerical tangent line at supplied inputs."""
    x0 = _finite_number(point, "point")
    slope = central_difference(function, x0, step)
    y0 = _finite_number(function(x0), "function value")
    values = [_finite_number(value, "input") for value in inputs]
    return [y0 + slope * (value - x0) for value in values]
