"""Validated calculations for ratios, rates, and percentages."""


def _require_nonzero(value, name):
    if value == 0:
        raise ValueError(f"{name} must not be zero")


def fraction(numerator, denominator):
    """Return numerator divided by denominator."""
    _require_nonzero(denominator, "denominator")
    return numerator / denominator


def unit_rate(amount, reference):
    """Return an amount per one reference unit."""
    _require_nonzero(reference, "reference")
    return amount / reference


def percentage(part, whole):
    """Return part as a percentage of whole."""
    return fraction(part, whole) * 100


def percentage_change(old, new):
    """Return relative change from old to new as a percentage."""
    _require_nonzero(old, "old value")
    return (new - old) / old * 100


def percentage_point_change(old_percent, new_percent):
    """Return new percentage minus old percentage in percentage points."""
    return new_percent - old_percent


def weighted_percentage(parts, wholes):
    """Return the percentage formed from combined parts and wholes."""
    if len(parts) != len(wholes):
        raise ValueError("parts and wholes must have the same length")
    if any(whole < 0 for whole in wholes):
        raise ValueError("wholes must not be negative")
    if any(part < 0 for part in parts):
        raise ValueError("parts must not be negative")
    if any(part > whole for part, whole in zip(parts, wholes)):
        raise ValueError("each part must not exceed its whole")
    return percentage(sum(parts), sum(wholes))
