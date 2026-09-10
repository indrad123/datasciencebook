"""Dependency-light utilities that bridge statistical summaries and ML evaluation."""


def mean_baseline(training_targets):
    values = [float(v) for v in training_targets]
    if not values:
        raise ValueError("training_targets must not be empty")
    return sum(values) / len(values)


def predict_constant(value, n):
    if n < 1:
        raise ValueError("n must be positive")
    return [float(value)] * n


def mean_absolute_error(actual, predicted):
    actual, predicted = list(actual), list(predicted)
    if not actual or len(actual) != len(predicted):
        raise ValueError("sequences must be non-empty and have equal length")
    return sum(abs(float(a) - float(p)) for a, p in zip(actual, predicted)) / len(actual)


def fit_simple_line(x, y):
    x, y = [float(v) for v in x], [float(v) for v in y]
    if len(x) < 2 or len(x) != len(y):
        raise ValueError("x and y must have equal length of at least two")
    x_bar, y_bar = sum(x) / len(x), sum(y) / len(y)
    denominator = sum((v - x_bar) ** 2 for v in x)
    if denominator == 0:
        raise ValueError("x must vary")
    slope = sum((a - x_bar) * (b - y_bar) for a, b in zip(x, y)) / denominator
    return y_bar - slope * x_bar, slope


def predict_line(x, intercept, slope):
    return [float(intercept) + float(slope) * float(v) for v in x]
