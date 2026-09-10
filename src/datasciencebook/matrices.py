"""Validated matrix and linear-system helpers for Chapter 8."""

import numpy as np


def as_matrix(values):
    """Return a finite, non-empty two-dimensional float array."""
    matrix = np.asarray(values, dtype=float)
    if matrix.ndim != 2 or matrix.size == 0 or not np.isfinite(matrix).all():
        raise ValueError("matrix must be finite, non-empty, and two-dimensional")
    return matrix


def matrix_product(a, b):
    """Return a validated matrix product."""
    left = as_matrix(a)
    right = np.asarray(b, dtype=float)
    if right.ndim not in (1, 2) or right.size == 0 or not np.isfinite(right).all():
        raise ValueError("right operand must be a finite non-empty vector or matrix")
    if left.shape[1] != right.shape[0]:
        raise ValueError("inside dimensions must match")
    return left @ right


def solve_system(coefficients, outcomes):
    """Solve a square full-rank linear system and return solution diagnostics."""
    matrix = as_matrix(coefficients)
    vector = np.asarray(outcomes, dtype=float)
    if vector.ndim != 1 or vector.size != matrix.shape[0] or not np.isfinite(vector).all():
        raise ValueError("outcomes must match the matrix row count")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("exact solver requires a square coefficient matrix")
    if np.linalg.matrix_rank(matrix) < matrix.shape[1]:
        raise ValueError("coefficient matrix must have full rank")
    solution = np.linalg.solve(matrix, vector)
    residual = matrix @ solution - vector
    return solution, residual, float(np.linalg.cond(matrix))
