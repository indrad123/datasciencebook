"""Validated helpers for exponential and logarithmic calculations."""

import math


def compound_value(initial, rate, periods):
    """Return initial * (1 + rate) ** periods."""
    if initial < 0:
        raise ValueError("initial must not be negative")
    if rate <= -1:
        raise ValueError("rate must be greater than -1")
    return initial * (1 + rate) ** periods


def log_base(value, base):
    """Return logarithm of a positive value in a valid base."""
    if value <= 0:
        raise ValueError("value must be positive")
    if base <= 0 or base == 1:
        raise ValueError("base must be positive and not equal to 1")
    return math.log(value) / math.log(base)


def time_to_target(initial, target, rate):
    """Solve target = initial * (1 + rate) ** periods."""
    if initial <= 0 or target <= 0:
        raise ValueError("initial and target must be positive")
    if rate <= -1 or rate == 0:
        raise ValueError("rate must define non-zero valid exponential change")
    periods = math.log(target / initial) / math.log(1 + rate)
    if periods < 0:
        raise ValueError("target is not reached in non-negative time at this rate")
    return periods
