"""Dependency-light helpers for provenance and data-quality checks."""

from collections import Counter
from datetime import datetime


def missing_rate(values):
    values = list(values)
    if not values:
        raise ValueError("values must not be empty")
    return sum(value is None or (isinstance(value, str) and not value.strip()) for value in values) / len(values)


def duplicate_keys(keys):
    counts = Counter(keys)
    return {key: count for key, count in counts.items() if count > 1}


def range_violations(values, minimum=None, maximum=None):
    if minimum is None and maximum is None:
        raise ValueError("at least one boundary is required")
    violations = []
    for index, value in enumerate(values):
        if value is None:
            continue
        if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
            violations.append(index)
    return violations


def chronological_violations(start_times, end_times):
    starts, ends = list(start_times), list(end_times)
    if len(starts) != len(ends):
        raise ValueError("time collections must have equal length")
    return [index for index, (start, end) in enumerate(zip(starts, ends))
            if start is not None and end is not None and end < start]


def join_reconciliation(left_keys, right_keys):
    left, right = list(left_keys), list(right_keys)
    left_set, right_set = set(left), set(right)
    return {
        "left_rows": len(left),
        "right_rows": len(right),
        "matched_unique_keys": len(left_set & right_set),
        "left_only_keys": sorted(left_set - right_set),
        "right_only_keys": sorted(right_set - left_set),
        "duplicate_left_keys": duplicate_keys(left),
        "duplicate_right_keys": duplicate_keys(right),
    }


def age_hours(observed_at, checked_at):
    if not isinstance(observed_at, datetime) or not isinstance(checked_at, datetime):
        raise TypeError("timestamps must be datetime values")
    hours = (checked_at - observed_at).total_seconds() / 3600
    if hours < 0:
        raise ValueError("observed_at must not be in the future")
    return hours


def quality_gate(results):
    """Return pass status and failed rule names from {name: bool}."""
    if not isinstance(results, dict) or not results:
        raise ValueError("results must be a non-empty dictionary")
    failed = [name for name, passed in results.items() if not bool(passed)]
    return {"passed": not failed, "failed_rules": failed}
