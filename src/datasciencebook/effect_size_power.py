"""Effect-size and prospective-power helpers for Chapter 22."""

import math


def normal_cdf(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("value must be finite")
    return 0.5 * (1 + math.erf(value / math.sqrt(2)))


def cohens_d(mean_a, mean_b, pooled_standard_deviation):
    sd = float(pooled_standard_deviation)
    difference = float(mean_a) - float(mean_b)
    if not math.isfinite(sd) or sd <= 0 or not math.isfinite(difference):
        raise ValueError("means must be finite and standard deviation positive")
    return difference / sd


def binary_effects(events_treatment, total_treatment, events_control, total_control):
    counts = (events_treatment, total_treatment, events_control, total_control)
    if not all(isinstance(x, int) for x in counts) or total_treatment <= 0 or total_control <= 0:
        raise ValueError("counts must be valid integers")
    if not 0 <= events_treatment <= total_treatment or not 0 <= events_control <= total_control:
        raise ValueError("event counts cannot exceed totals")
    treatment = events_treatment / total_treatment
    control = events_control / total_control
    risk_difference = treatment - control
    risk_ratio = math.inf if control == 0 and treatment > 0 else (math.nan if control == 0 else treatment / control)
    return risk_difference, risk_ratio


def two_sided_z_power(effect_size, sample_size_per_group, alpha=0.05):
    """Approximate power for two equal independent normal groups."""
    effect_size, alpha = float(effect_size), float(alpha)
    if not math.isfinite(effect_size) or not isinstance(sample_size_per_group, int) or sample_size_per_group <= 1 or not 0 < alpha < 1:
        raise ValueError("effect, sample size, and alpha are invalid")
    critical = 1.959963984540054 if math.isclose(alpha, 0.05) else _inverse_normal(1 - alpha / 2)
    noncentrality = abs(effect_size) * math.sqrt(sample_size_per_group / 2)
    return 1 - normal_cdf(critical - noncentrality) + normal_cdf(-critical - noncentrality)


def required_sample_size(effect_size, target_power=0.80, alpha=0.05, maximum=1_000_000):
    if not 0 < target_power < 1:
        raise ValueError("target power must lie between zero and one")
    for size in range(2, maximum + 1):
        if two_sided_z_power(effect_size, size, alpha) >= target_power:
            return size
    raise ValueError("target not reached within maximum")


def _inverse_normal(probability):
    if not 0 < probability < 1:
        raise ValueError("probability must lie between zero and one")
    low, high = -8.0, 8.0
    for _ in range(80):
        middle = (low + high) / 2
        if normal_cdf(middle) < probability:
            low = middle
        else:
            high = middle
    return (low + high) / 2
