"""Sampling and measurement-error helpers for Chapter 14."""

import math
import random


def classify_measurement_scale(kind):
    """Return a plain-language description for a named measurement scale."""
    descriptions = {
        "nominal": "categories without an intrinsic order",
        "ordinal": "ordered categories with unspecified gaps",
        "interval": "numeric values with meaningful equal differences but no true zero",
        "ratio": "numeric values with meaningful equal differences and a true zero",
    }
    key = str(kind).strip().lower()
    if key not in descriptions:
        raise ValueError("kind must be nominal, ordinal, interval, or ratio")
    return descriptions[key]


def systematic_sample(values, sample_size, start=0):
    """Select an approximately evenly spaced sample from an ordered finite frame."""
    items = list(values)
    if not isinstance(sample_size, int) or sample_size <= 0 or sample_size > len(items):
        raise ValueError("sample_size must be a positive integer no larger than the frame")
    step = len(items) / sample_size
    if not isinstance(start, int) or start < 0 or start >= math.ceil(step):
        raise ValueError("start must be an eligible integer within the first interval")
    return [items[min(int(start + i * step), len(items) - 1)] for i in range(sample_size)]


def stratified_sample(groups, sample_sizes, seed):
    """Sample without replacement from each named group."""
    if set(groups) != set(sample_sizes):
        raise ValueError("groups and sample_sizes must have the same keys")
    rng = random.Random(seed)
    selected = []
    for name, values in groups.items():
        items = list(values)
        size = sample_sizes[name]
        if not isinstance(size, int) or size <= 0 or size > len(items):
            raise ValueError("each requested sample size must be valid")
        selected.extend(rng.sample(items, size))
    return selected


def measurement_errors(observed, reference):
    """Return signed errors, bias, and mean absolute error against reference values."""
    observed_values = [float(value) for value in observed]
    reference_values = [float(value) for value in reference]
    if not observed_values or len(observed_values) != len(reference_values):
        raise ValueError("observed and reference must be non-empty and equal length")
    if not all(math.isfinite(value) for value in observed_values + reference_values):
        raise ValueError("measurements must be finite")
    errors = [value - truth for value, truth in zip(observed_values, reference_values)]
    return {
        "errors": errors,
        "bias": sum(errors) / len(errors),
        "mean_absolute_error": sum(abs(error) for error in errors) / len(errors),
    }
