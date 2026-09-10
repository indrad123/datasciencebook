"""Small, explicit helpers for translating mathematical notation into code."""
from __future__ import annotations

import math
from collections.abc import Callable, Iterable


def _numbers(values: Iterable[float], name: str = "values") -> list[float]:
    try:
        result = [float(value) for value in values]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain numbers") from exc
    if not result or not all(math.isfinite(value) for value in result):
        raise ValueError(f"{name} must be non-empty and finite")
    return result


def sigma(values: Iterable[float]) -> float:
    """Return the finite sum represented by sigma notation."""
    return math.fsum(_numbers(values))


def weighted_sum(values: Iterable[float], weights: Iterable[float]) -> float:
    """Return sum_i w_i x_i after validating aligned finite sequences."""
    x = _numbers(values)
    w = _numbers(weights, "weights")
    if len(x) != len(w):
        raise ValueError("values and weights must have equal length")
    return math.fsum(value * weight for value, weight in zip(x, w))


def dot(left: Iterable[float], right: Iterable[float]) -> float:
    """Return the dot product of two equal-length vectors."""
    return weighted_sum(left, right)


def euclidean_norm(values: Iterable[float]) -> float:
    """Return the Euclidean norm of a vector."""
    x = _numbers(values)
    return math.sqrt(math.fsum(value * value for value in x))


def empirical_probability(events: Iterable[bool]) -> float:
    """Return the observed fraction of true events."""
    result = list(events)
    if not result or any(type(value) is not bool for value in result):
        raise ValueError("events must be a non-empty sequence of booleans")
    return sum(result) / len(result)


def central_difference(function: Callable[[float], float], x: float, step: float = 1e-5) -> float:
    """Approximate f'(x) with a central finite difference."""
    if not callable(function):
        raise ValueError("function must be callable")
    x, step = float(x), float(step)
    if not math.isfinite(x) or not math.isfinite(step) or step <= 0:
        raise ValueError("x must be finite and step must be positive and finite")
    result = (float(function(x + step)) - float(function(x - step))) / (2 * step)
    if not math.isfinite(result):
        raise ValueError("function must produce finite numeric values")
    return result
