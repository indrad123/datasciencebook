"""Hypothesis-testing helpers for Chapter 21."""

import math
import random


def normal_cdf(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("value must be finite")
    return 0.5 * (1 + math.erf(value / math.sqrt(2)))


def one_sample_z_test(sample_mean, null_mean, standard_error, alternative="two-sided"):
    """Return a z statistic and p-value for a mean with known standard error."""
    sample_mean, null_mean, standard_error = map(float, (sample_mean, null_mean, standard_error))
    if not all(math.isfinite(x) for x in (sample_mean, null_mean, standard_error)) or standard_error <= 0:
        raise ValueError("inputs must be finite and standard error positive")
    z = (sample_mean - null_mean) / standard_error
    if alternative == "two-sided":
        p = 2 * (1 - normal_cdf(abs(z)))
    elif alternative == "greater":
        p = 1 - normal_cdf(z)
    elif alternative == "less":
        p = normal_cdf(z)
    else:
        raise ValueError("alternative must be two-sided, greater, or less")
    return z, max(0.0, min(1.0, p))


def standardized_mean_difference(mean_a, mean_b, pooled_standard_deviation):
    pooled_standard_deviation = float(pooled_standard_deviation)
    if not math.isfinite(pooled_standard_deviation) or pooled_standard_deviation <= 0:
        raise ValueError("pooled standard deviation must be positive and finite")
    difference = float(mean_a) - float(mean_b)
    if not math.isfinite(difference):
        raise ValueError("means must be finite")
    return difference / pooled_standard_deviation


def bonferroni_alpha(family_alpha, tests):
    family_alpha = float(family_alpha)
    if not 0 < family_alpha < 1 or not isinstance(tests, int) or tests <= 0:
        raise ValueError("family alpha and number of tests are invalid")
    return family_alpha / tests


def permutation_mean_test(group_a, group_b, repetitions=5000, seed=0):
    """Return observed mean difference and a two-sided permutation p-value."""
    a, b = [float(x) for x in group_a], [float(x) for x in group_b]
    if not a or not b or not all(math.isfinite(x) for x in a + b):
        raise ValueError("groups must contain finite values")
    if not isinstance(repetitions, int) or repetitions < 100:
        raise ValueError("repetitions must be an integer of at least 100")
    observed = sum(a) / len(a) - sum(b) / len(b)
    combined = a + b
    rng = random.Random(seed)
    extreme = 0
    for _ in range(repetitions):
        shuffled = rng.sample(combined, len(combined))
        difference = sum(shuffled[:len(a)]) / len(a) - sum(shuffled[len(a):]) / len(b)
        extreme += abs(difference) >= abs(observed) - 1e-12
    return observed, (extreme + 1) / (repetitions + 1)
