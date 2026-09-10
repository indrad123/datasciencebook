"""Validated elementary probability helpers for Chapter 12."""

import math


def _probability(value, name):
    number = float(value)
    if not math.isfinite(number) or not 0 <= number <= 1:
        raise ValueError(f"{name} must be between 0 and 1")
    return number


def conditional_probability(joint_probability, condition_probability):
    """Return P(A|B) from P(A and B) and P(B)."""
    joint = _probability(joint_probability, "joint_probability")
    condition = _probability(condition_probability, "condition_probability")
    if condition == 0 or joint > condition:
        raise ValueError("conditioning event must be possible and contain the joint event")
    return joint / condition


def bayes_binary(prior, sensitivity, false_positive_rate):
    """Return P(condition|positive) for a binary alert."""
    p = _probability(prior, "prior")
    true_positive = _probability(sensitivity, "sensitivity")
    false_positive = _probability(false_positive_rate, "false_positive_rate")
    evidence = true_positive * p + false_positive * (1 - p)
    if evidence == 0:
        raise ValueError("a positive result has zero probability")
    return true_positive * p / evidence


def expected_value(values, probabilities):
    """Return the expectation of a finite discrete distribution."""
    numbers = [float(value) for value in values]
    probs = [_probability(value, "probability") for value in probabilities]
    if not numbers or len(numbers) != len(probs) or not all(math.isfinite(v) for v in numbers):
        raise ValueError("values and probabilities must be finite non-empty equal-length sequences")
    if not math.isclose(sum(probs), 1.0, rel_tol=0, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return sum(value * probability for value, probability in zip(numbers, probs))
