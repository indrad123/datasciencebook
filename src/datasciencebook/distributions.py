"""Frequency and empirical-distribution helpers for Chapter 15."""

import math


def frequency_table(values):
    """Return sorted value, count, and relative-frequency rows."""
    items = list(values)
    if not items:
        raise ValueError("values must not be empty")
    counts = {}
    for value in items:
        counts[value] = counts.get(value, 0) + 1
    return [(value, counts[value], counts[value] / len(items)) for value in sorted(counts, key=str)]


def contingency_table(row_values, column_values):
    """Return labels and a rectangular count matrix for two categorical variables."""
    rows, columns = list(row_values), list(column_values)
    if not rows or len(rows) != len(columns):
        raise ValueError("variables must be non-empty and equal length")
    row_labels = sorted(set(rows), key=str)
    column_labels = sorted(set(columns), key=str)
    matrix = [[sum(r == rv and c == cv for r, c in zip(rows, columns)) for cv in column_labels] for rv in row_labels]
    return row_labels, column_labels, matrix


def histogram_counts(values, bin_edges):
    """Count finite numeric values in left-closed bins, including the last right edge."""
    numbers = [float(value) for value in values]
    edges = [float(edge) for edge in bin_edges]
    if not numbers or len(edges) < 2 or not all(math.isfinite(value) for value in numbers + edges):
        raise ValueError("values and edges must be finite and non-empty")
    if any(right <= left for left, right in zip(edges, edges[1:])):
        raise ValueError("bin edges must increase strictly")
    counts = [0] * (len(edges) - 1)
    for value in numbers:
        if value < edges[0] or value > edges[-1]:
            continue
        index = len(counts) - 1 if value == edges[-1] else next((i for i in range(len(counts)) if edges[i] <= value < edges[i + 1]), None)
        if index is not None:
            counts[index] += 1
    return counts


def empirical_cdf(values):
    """Return sorted unique values and cumulative relative frequencies."""
    table = frequency_table(values)
    cumulative = 0.0
    result = []
    for value, _, relative in table:
        cumulative += relative
        result.append((value, cumulative))
    return result
