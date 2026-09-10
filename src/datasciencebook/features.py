"""Dependency-light feature engineering helpers."""

import math


def safe_ratio(numerator, denominator):
    if denominator is None or denominator == 0:
        return None
    if numerator is None:
        return None
    return float(numerator) / float(denominator)


def cyclic_encode(position, period):
    if period <= 0:
        raise ValueError("period must be positive")
    angle = 2 * math.pi * float(position) / float(period)
    return math.sin(angle), math.cos(angle)


def lag(values, periods=1):
    values = list(values)
    if not isinstance(periods, int) or periods < 1:
        raise ValueError("periods must be a positive integer")
    return [None] * min(periods, len(values)) + values[:-periods] if periods < len(values) else [None] * len(values)


def trailing_mean(values, window, minimum_history=None):
    values = list(values)
    if not isinstance(window, int) or window < 1:
        raise ValueError("window must be a positive integer")
    minimum = window if minimum_history is None else minimum_history
    if not isinstance(minimum, int) or not 1 <= minimum <= window:
        raise ValueError("minimum_history must be between one and window")
    result = []
    for index in range(len(values)):
        history = [value for value in values[max(0, index - window):index] if value is not None]
        result.append(sum(history) / len(history) if len(history) >= minimum else None)
    return result


def fit_categories(values, include_other=True):
    categories = sorted({value for value in values if value is not None}, key=str)
    if include_other and "OTHER" not in categories:
        categories.append("OTHER")
    return tuple(categories)


def one_hot(value, categories):
    categories = tuple(categories)
    if len(categories) != len(set(categories)):
        raise ValueError("categories must be unique")
    selected = value if value in categories else "OTHER"
    if selected not in categories:
        raise ValueError("unseen category and no OTHER category")
    return {f"category_{category}": int(category == selected) for category in categories}


def interaction(left, right):
    if left is None or right is None:
        return None
    return float(left) * float(right)


def feature_record(name, formula, available_at, unit=None, version="1.0"):
    if not all(isinstance(item, str) and item.strip() for item in (name, formula, available_at, version)):
        raise ValueError("name, formula, available_at, and version are required")
    return {"name": name, "formula": formula, "available_at": available_at, "unit": unit, "version": version}
