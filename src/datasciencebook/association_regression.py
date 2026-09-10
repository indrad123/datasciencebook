"""Correlation and simple-regression helpers for Chapter 23."""

import math


def _paired(x, y):
    xs, ys = [float(v) for v in x], [float(v) for v in y]
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("paired inputs must have equal length of at least two")
    if not all(math.isfinite(v) for v in xs + ys):
        raise ValueError("values must be finite")
    return xs, ys


def covariance(x, y):
    xs, ys = _paired(x, y)
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / (len(xs) - 1)


def pearson_correlation(x, y):
    xs, ys = _paired(x, y)
    sx = math.sqrt(covariance(xs, xs))
    sy = math.sqrt(covariance(ys, ys))
    if sx == 0 or sy == 0:
        raise ValueError("both variables must vary")
    return covariance(xs, ys) / (sx * sy)


def _ranks(values):
    indexed = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(indexed):
        end = start + 1
        while end < len(indexed) and indexed[end][1] == indexed[start][1]:
            end += 1
        average_rank = (start + 1 + end) / 2
        for position in range(start, end):
            ranks[indexed[position][0]] = average_rank
        start = end
    return ranks


def spearman_correlation(x, y):
    xs, ys = _paired(x, y)
    return pearson_correlation(_ranks(xs), _ranks(ys))


def simple_linear_regression(x, y):
    xs, ys = _paired(x, y)
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    denominator = sum((v - mx) ** 2 for v in xs)
    if denominator == 0:
        raise ValueError("predictor must vary")
    slope = sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / denominator
    intercept = my - slope * mx
    fitted = [intercept + slope * value for value in xs]
    residuals = [actual - predicted for actual, predicted in zip(ys, fitted)]
    sse = sum(value ** 2 for value in residuals)
    sst = sum((value - my) ** 2 for value in ys)
    r_squared = 1 - sse / sst if sst else 1.0
    rmse = math.sqrt(sse / len(xs))
    return {"intercept": intercept, "slope": slope, "fitted": fitted, "residuals": residuals, "r_squared": r_squared, "rmse": rmse}


def predict(intercept, slope, values):
    if not math.isfinite(float(intercept)) or not math.isfinite(float(slope)):
        raise ValueError("coefficients must be finite")
    result = [float(intercept) + float(slope) * float(value) for value in values]
    if not all(math.isfinite(v) for v in result):
        raise ValueError("predictions must be finite")
    return result
