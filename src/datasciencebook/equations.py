"""Small, validated helpers for introductory linear equations."""

from math import isclose


def evaluate_linear(a, x, b=0.0):
    """Evaluate a*x + b."""
    return a * x + b


def solve_linear(a, b, c):
    """Solve a*x + b = c for a unique x."""
    if a == 0:
        raise ValueError("a must not be zero for a unique solution")
    return (c - b) / a


def solve_both_sides(a, b, c, d):
    """Solve a*x + b = c*x + d and classify non-unique cases."""
    coefficient = a - c
    constant = d - b
    if coefficient == 0:
        return ("infinite", None) if constant == 0 else ("none", None)
    return "unique", constant / coefficient


def verify_linear(a, b, c, x, *, tolerance=1e-9):
    """Check a*x + b = c within a numerical tolerance."""
    if tolerance < 0:
        raise ValueError("tolerance must not be negative")
    return isclose(evaluate_linear(a, x, b), c, abs_tol=tolerance)
