"""Validated vector, distance, and similarity helpers for Chapter 7."""

import math


def _paired(a, b):
    left = list(a)
    right = list(b)
    if not left or len(left) != len(right):
        raise ValueError("vectors must have the same non-zero dimension")
    return left, right


def magnitude(vector):
    """Return the Euclidean norm of a non-empty vector."""
    values = list(vector)
    if not values:
        raise ValueError("vector must not be empty")
    return math.sqrt(sum(value * value for value in values))


def unit_vector(vector):
    """Return a Euclidean unit vector in the input direction."""
    values = list(vector)
    norm = magnitude(values)
    if norm == 0:
        raise ValueError("zero vector has no unit direction")
    return [value / norm for value in values]


def dot_product(a, b):
    """Return the dot product of equal-dimensional vectors."""
    left, right = _paired(a, b)
    return sum(x * y for x, y in zip(left, right))


def euclidean_distance(a, b):
    """Return straight-line distance between equal-dimensional vectors."""
    left, right = _paired(a, b)
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(left, right)))


def manhattan_distance(a, b):
    """Return the sum of absolute component differences."""
    left, right = _paired(a, b)
    return sum(abs(x - y) for x, y in zip(left, right))


def cosine_similarity(a, b):
    """Return directional similarity for two non-zero vectors."""
    left, right = _paired(a, b)
    norm_left = magnitude(left)
    norm_right = magnitude(right)
    if norm_left == 0 or norm_right == 0:
        raise ValueError("cosine similarity requires non-zero vectors")
    return dot_product(left, right) / (norm_left * norm_right)
