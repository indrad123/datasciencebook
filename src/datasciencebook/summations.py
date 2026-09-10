"""Validated helpers for finite sums used in Chapter 6."""


def finite_sum(values):
    """Return the sum of a non-empty iterable of numeric values."""
    items = list(values)
    if not items:
        raise ValueError("values must not be empty")
    return sum(items)


def weighted_sum(values, weights):
    """Return the termwise weighted sum for equal-length non-empty inputs."""
    value_items = list(values)
    weight_items = list(weights)
    if not value_items or len(value_items) != len(weight_items):
        raise ValueError("values and weights must have the same non-zero length")
    return sum(value * weight for value, weight in zip(value_items, weight_items))


def sum_squared_errors(actual, predicted):
    """Return the sum of squared termwise prediction errors."""
    actual_items = list(actual)
    predicted_items = list(predicted)
    if not actual_items or len(actual_items) != len(predicted_items):
        raise ValueError("actual and predicted must have the same non-zero length")
    return sum((observed - estimate) ** 2 for observed, estimate in zip(actual_items, predicted_items))


def conditional_sum(values, predicate):
    """Return the sum of values for which predicate(value) is true."""
    return sum(value for value in values if predicate(value))
