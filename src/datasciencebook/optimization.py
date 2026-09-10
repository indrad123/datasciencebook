"""Small, transparent optimisation helpers for Chapter 11."""

import math


def grid_search_1d(objective, candidates):
    """Return the finite candidate with the smallest finite objective."""
    points = [float(value) for value in candidates]
    if not points or not all(math.isfinite(value) for value in points):
        raise ValueError("candidates must be a non-empty finite sequence")
    scored = [(point, float(objective(point))) for point in points]
    if not all(math.isfinite(score) for _, score in scored):
        raise ValueError("objective values must be finite")
    return min(scored, key=lambda item: item[1])


def gradient_descent_1d(objective, gradient, start, learning_rate=0.1, steps=50, tolerance=1e-8):
    """Run one-dimensional gradient descent and return iteration records."""
    x = float(start)
    rate = float(learning_rate)
    tol = float(tolerance)
    if not math.isfinite(x) or not math.isfinite(rate) or rate <= 0:
        raise ValueError("start must be finite and learning_rate must be positive")
    if not isinstance(steps, int) or steps < 1 or not math.isfinite(tol) or tol < 0:
        raise ValueError("steps must be positive and tolerance non-negative")
    history = []
    for iteration in range(steps + 1):
        value = float(objective(x))
        slope = float(gradient(x))
        if not math.isfinite(value) or not math.isfinite(slope):
            raise ValueError("objective and gradient must remain finite")
        history.append((iteration, x, value, slope))
        if abs(slope) <= tol or iteration == steps:
            break
        x -= rate * slope
    return history
