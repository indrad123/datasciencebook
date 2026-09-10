"""Elementary probability-distribution functions for Chapter 18."""

import math


def _probability(value, name="probability"):
    value = float(value)
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"{name} must be between zero and one")
    return value


def bernoulli_pmf(outcome, probability):
    probability = _probability(probability)
    if outcome not in (0, 1):
        raise ValueError("outcome must be zero or one")
    return probability if outcome == 1 else 1 - probability


def binomial_pmf(successes, trials, probability):
    probability = _probability(probability)
    if not isinstance(trials, int) or not isinstance(successes, int) or trials < 0 or not 0 <= successes <= trials:
        raise ValueError("successes and trials must be valid integers")
    return math.comb(trials, successes) * probability**successes * (1 - probability) ** (trials - successes)


def poisson_pmf(count, rate):
    rate = float(rate)
    if not isinstance(count, int) or count < 0 or not math.isfinite(rate) or rate < 0:
        raise ValueError("count and rate must be non-negative")
    return math.exp(-rate) * rate**count / math.factorial(count)


def uniform_cdf(value, lower, upper):
    value, lower, upper = map(float, (value, lower, upper))
    if not all(map(math.isfinite, (value, lower, upper))) or upper <= lower:
        raise ValueError("finite bounds must satisfy lower < upper")
    return min(1.0, max(0.0, (value - lower) / (upper - lower)))


def normal_cdf(value, mean=0, standard_deviation=1):
    value, mean, standard_deviation = map(float, (value, mean, standard_deviation))
    if not all(map(math.isfinite, (value, mean, standard_deviation))) or standard_deviation <= 0:
        raise ValueError("standard deviation must be positive")
    return 0.5 * (1 + math.erf((value - mean) / (standard_deviation * math.sqrt(2))))


def exponential_cdf(value, rate):
    value, rate = float(value), float(rate)
    if not math.isfinite(value) or not math.isfinite(rate) or rate <= 0:
        raise ValueError("value must be finite and rate positive")
    return 0.0 if value < 0 else 1 - math.exp(-rate * value)
