"""Confidence-interval helpers for Chapter 20."""

import math
import random


def normal_interval(estimate, standard_error, critical_value=1.959963984540054):
    """Return estimate plus or minus a critical value times its standard error."""
    estimate = float(estimate)
    standard_error = float(standard_error)
    critical_value = float(critical_value)
    if not all(math.isfinite(x) for x in (estimate, standard_error, critical_value)):
        raise ValueError("inputs must be finite")
    if standard_error < 0 or critical_value <= 0:
        raise ValueError("standard error must be non-negative and critical value positive")
    margin = critical_value * standard_error
    return estimate - margin, estimate + margin


def wilson_interval(successes, trials, critical_value=1.959963984540054):
    """Return a Wilson score interval for a binomial proportion."""
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("counts must be integers")
    critical_value = float(critical_value)
    if trials <= 0 or successes < 0 or successes > trials or not math.isfinite(critical_value) or critical_value <= 0:
        raise ValueError("counts and critical value are invalid")
    proportion = successes / trials
    z2 = critical_value**2
    denominator = 1 + z2 / trials
    centre = (proportion + z2 / (2 * trials)) / denominator
    half_width = critical_value * math.sqrt(proportion * (1 - proportion) / trials + z2 / (4 * trials**2)) / denominator
    return centre - half_width, centre + half_width


def bootstrap_mean_interval(values, confidence_level=0.95, repetitions=2000, seed=0):
    """Return a percentile bootstrap interval for a population mean."""
    data = [float(value) for value in values]
    confidence_level = float(confidence_level)
    if not data or not all(math.isfinite(value) for value in data):
        raise ValueError("values must be a non-empty finite sequence")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence level must lie between zero and one")
    if not isinstance(repetitions, int) or repetitions < 100:
        raise ValueError("repetitions must be an integer of at least 100")
    rng = random.Random(seed)
    size = len(data)
    means = sorted(sum(rng.choices(data, k=size)) / size for _ in range(repetitions))
    alpha = 1 - confidence_level

    def percentile(probability):
        position = probability * (repetitions - 1)
        lower = int(math.floor(position))
        upper = int(math.ceil(position))
        fraction = position - lower
        return means[lower] * (1 - fraction) + means[upper] * fraction

    return percentile(alpha / 2), percentile(1 - alpha / 2)
