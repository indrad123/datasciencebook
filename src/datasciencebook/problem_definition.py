"""Dependency-light checks for analytical problem formulation."""

REQUIRED_FIELDS = (
    "decision",
    "owner",
    "unit",
    "population",
    "outcome",
    "horizon",
    "use_time",
    "action",
    "baseline",
    "success_criteria",
)


def missing_fields(specification, required_fields=REQUIRED_FIELDS):
    if not isinstance(specification, dict):
        raise TypeError("specification must be a dictionary")
    missing = []
    for field in required_fields:
        value = specification.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            missing.append(field)
    return missing


def readiness_score(specification, required_fields=REQUIRED_FIELDS):
    fields = tuple(required_fields)
    if not fields:
        raise ValueError("required_fields must not be empty")
    return (len(fields) - len(missing_fields(specification, fields))) / len(fields)


def upper_bound_value(volume, event_rate, preventable_fraction, value_per_prevented_event):
    volume = float(volume)
    event_rate = float(event_rate)
    preventable_fraction = float(preventable_fraction)
    value_per_prevented_event = float(value_per_prevented_event)
    if volume < 0 or value_per_prevented_event < 0:
        raise ValueError("volume and value must be non-negative")
    if not 0 <= event_rate <= 1 or not 0 <= preventable_fraction <= 1:
        raise ValueError("rates must be between zero and one")
    return volume * event_rate * preventable_fraction * value_per_prevented_event


def is_available_at_use_time(available_at, use_time):
    return available_at <= use_time


def is_actionable(result_before_decision, actor_authorized, action_affects_outcome, capacity):
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("capacity must be a non-negative integer")
    return bool(result_before_decision and actor_authorized and action_affects_outcome and capacity > 0)
