"""Distribution-shape and outlier-screening helpers for Chapter 17."""

import math

from datasciencebook.summaries import mean, median, quantile, sample_standard_deviation


def _numbers(values, minimum=1):
    numbers = [float(value) for value in values]
    if len(numbers) < minimum or not all(math.isfinite(value) for value in numbers):
        raise ValueError(f"values must contain at least {minimum} finite number(s)")
    return numbers


def moment_skewness(values):
    """Return the adjusted Fisher-Pearson sample skewness coefficient."""
    numbers = _numbers(values, minimum=3)
    centre = mean(numbers)
    sd = sample_standard_deviation(numbers)
    if sd == 0:
        return 0.0
    n = len(numbers)
    return n / ((n - 1) * (n - 2)) * sum(((value - centre) / sd) ** 3 for value in numbers)


def bowley_skewness(values):
    """Return quartile-based Bowley skewness."""
    numbers = _numbers(values)
    q1, q2, q3 = (quantile(numbers, p) for p in (0.25, 0.5, 0.75))
    width = q3 - q1
    return 0.0 if width == 0 else (q3 + q1 - 2 * q2) / width


def iqr_fences(values, multiplier=1.5):
    """Return conventional lower and upper IQR screening fences."""
    numbers = _numbers(values)
    multiplier = float(multiplier)
    if not math.isfinite(multiplier) or multiplier < 0:
        raise ValueError("multiplier must be finite and non-negative")
    q1, q3 = quantile(numbers, 0.25), quantile(numbers, 0.75)
    width = q3 - q1
    return q1 - multiplier * width, q3 + multiplier * width


def iqr_flags(values, multiplier=1.5):
    """Return a Boolean flag for each value outside the IQR fences."""
    numbers = _numbers(values)
    lower, upper = iqr_fences(numbers, multiplier)
    return [value < lower or value > upper for value in numbers]


def median_absolute_deviation(values):
    """Return the median absolute deviation from the sample median."""
    numbers = _numbers(values)
    centre = median(numbers)
    return median(abs(value - centre) for value in numbers)


def robust_z_scores(values, consistency=0.6744897501960817):
    """Return median/MAD-based standardized scores; reject zero-MAD data."""
    numbers = _numbers(values)
    centre = median(numbers)
    mad = median_absolute_deviation(numbers)
    if mad == 0:
        raise ValueError("robust z-scores are undefined when MAD is zero")
    return [consistency * (value - centre) / mad for value in numbers]
