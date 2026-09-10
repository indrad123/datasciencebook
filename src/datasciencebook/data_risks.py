"""Small, dependency-light diagnostics for missingness, bias, and leakage."""

from math import sqrt
from random import Random


def missing_rate(values):
    values = list(values)
    if not values:
        raise ValueError("values must not be empty")
    return sum(v is None for v in values) / len(values)


def missing_rates(rows, columns):
    rows = list(rows)
    if not rows:
        raise ValueError("rows must not be empty")
    return {c: missing_rate(row.get(c) for row in rows) for c in columns}


def complete_case_mean(values):
    observed = [float(v) for v in values if v is not None]
    if not observed:
        raise ValueError("at least one value must be observed")
    return sum(observed) / len(observed)


def standardized_mean_difference(group_a, group_b):
    a, b = [float(x) for x in group_a], [float(x) for x in group_b]
    if len(a) < 2 or len(b) < 2:
        raise ValueError("each group needs at least two observations")
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    va = sum((x - ma) ** 2 for x in a) / (len(a) - 1)
    vb = sum((x - mb) ** 2 for x in b) / (len(b) - 1)
    pooled = sqrt((va + vb) / 2)
    if pooled == 0:
        return 0.0 if ma == mb else float("inf")
    return (ma - mb) / pooled


def group_rate(rows, group_key, outcome_key):
    totals, positives = {}, {}
    for row in rows:
        group = row[group_key]
        totals[group] = totals.get(group, 0) + 1
        positives[group] = positives.get(group, 0) + int(bool(row[outcome_key]))
    return {g: positives[g] / totals[g] for g in totals}


def random_split_indices(n, test_fraction=0.25, seed=42):
    if n < 2 or not 0 < test_fraction < 1:
        raise ValueError("invalid split configuration")
    indices = list(range(n))
    Random(seed).shuffle(indices)
    cut = max(1, min(n - 1, round(n * (1 - test_fraction))))
    return indices[:cut], indices[cut:]


def temporal_split_indices(times, cutoff):
    train = [i for i, t in enumerate(times) if t < cutoff]
    test = [i for i, t in enumerate(times) if t >= cutoff]
    if not train or not test:
        raise ValueError("cutoff must leave observations on both sides")
    return train, test


def audit_feature_availability(feature_times, prediction_times):
    if len(feature_times) != len(prediction_times):
        raise ValueError("time sequences must have equal length")
    return [f > p for f, p in zip(feature_times, prediction_times)]
