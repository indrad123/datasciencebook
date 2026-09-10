"""Measures of centre, position, and spread for Chapter 16."""

import math


def _numbers(values, minimum=1):
    numbers = [float(value) for value in values]
    if len(numbers) < minimum or not all(math.isfinite(value) for value in numbers):
        raise ValueError(f"values must contain at least {minimum} finite number(s)")
    return numbers


def mean(values):
    """Return the arithmetic mean."""
    numbers = _numbers(values)
    return sum(numbers) / len(numbers)


def weighted_mean(values, weights):
    """Return a weighted mean for finite, non-negative weights."""
    numbers = _numbers(values)
    weights = [float(weight) for weight in weights]
    if len(numbers) != len(weights) or not all(math.isfinite(weight) and weight >= 0 for weight in weights):
        raise ValueError("weights must be finite, non-negative, and match values")
    total_weight = sum(weights)
    if total_weight <= 0:
        raise ValueError("weights must have a positive sum")
    return sum(value * weight for value, weight in zip(numbers, weights)) / total_weight


def quantile(values, probability):
    """Return a linearly interpolated sample quantile using index (n - 1) * p."""
    numbers = sorted(_numbers(values))
    probability = float(probability)
    if not math.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("probability must be between zero and one")
    position = (len(numbers) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return numbers[lower]
    fraction = position - lower
    return numbers[lower] + fraction * (numbers[upper] - numbers[lower])


def median(values):
    """Return the median, equivalent to the 0.5 quantile."""
    return quantile(values, 0.5)


def interquartile_range(values):
    """Return Q3 minus Q1 under the module's quantile convention."""
    return quantile(values, 0.75) - quantile(values, 0.25)


def five_number_summary(values):
    """Return minimum, Q1, median, Q3, and maximum."""
    numbers = _numbers(values)
    return {
        "minimum": min(numbers),
        "q1": quantile(numbers, 0.25),
        "median": median(numbers),
        "q3": quantile(numbers, 0.75),
        "maximum": max(numbers),
    }


def sample_variance(values):
    """Return variance with the n - 1 sample denominator."""
    numbers = _numbers(values, minimum=2)
    centre = mean(numbers)
    return sum((value - centre) ** 2 for value in numbers) / (len(numbers) - 1)


def sample_standard_deviation(values):
    """Return the sample standard deviation in the variable's units."""
    return math.sqrt(sample_variance(values))
