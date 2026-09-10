"""Reusable helpers for introductory functions and straight lines."""


def linear_value(x, slope, intercept=0.0):
    """Evaluate slope*x + intercept."""
    return slope * x + intercept


def slope_between(x1, y1, x2, y2):
    """Calculate slope between two distinct x coordinates."""
    if x2 == x1:
        raise ValueError("x coordinates must be different")
    return (y2 - y1) / (x2 - x1)


def line_intersection(m1, b1, m2, b2):
    """Return the intersection of two non-parallel lines."""
    if m1 == m2:
        raise ValueError("parallel or identical lines have no unique intersection")
    x = (b2 - b1) / (m1 - m2)
    return x, linear_value(x, m1, b1)


def linear_points(inputs, slope, intercept=0.0):
    """Return ordered pairs for a linear function."""
    return [(x, linear_value(x, slope, intercept)) for x in inputs]
