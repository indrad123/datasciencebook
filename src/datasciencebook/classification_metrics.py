"""Dependency-light classification metrics for Chapter 35."""

from __future__ import annotations


def confusion_counts(actual, predicted):
    """Return TN, FP, FN, TP for binary labels."""
    y = list(actual)
    p = list(predicted)
    if len(y) != len(p) or not y:
        raise ValueError("actual and predicted must have equal non-zero length")
    if not set(y + p) <= {0, 1, False, True}:
        raise ValueError("labels must be binary")
    tn = fp = fn = tp = 0
    for a, b in zip(y, p):
        if a == 1 and b == 1: tp += 1
        elif a == 0 and b == 1: fp += 1
        elif a == 1 and b == 0: fn += 1
        else: tn += 1
    return {"tn": tn, "fp": fp, "fn": fn, "tp": tp}


def classification_summary(actual, predicted):
    """Calculate common binary metrics, using zero for undefined ratios."""
    c = confusion_counts(actual, predicted)
    tn, fp, fn, tp = c["tn"], c["fp"], c["fn"], c["tp"]
    n = tn + fp + fn + tp
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    specificity = tn / (tn + fp) if tn + fp else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    balanced = (recall + specificity) / 2
    return {**c, "accuracy": (tp + tn) / n, "precision": precision,
            "recall": recall, "specificity": specificity, "f1": f1,
            "balanced_accuracy": balanced}


def threshold_predictions(scores, threshold):
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between zero and one")
    values = list(scores)
    if any(s < 0 or s > 1 for s in values):
        raise ValueError("scores must be between zero and one")
    return [int(s >= threshold) for s in values]


def expected_error_cost(actual, predicted, false_positive_cost, false_negative_cost):
    if false_positive_cost < 0 or false_negative_cost < 0:
        raise ValueError("costs cannot be negative")
    c = confusion_counts(actual, predicted)
    return c["fp"] * false_positive_cost + c["fn"] * false_negative_cost


def threshold_table(actual, scores, thresholds, false_positive_cost=1.0,
                    false_negative_cost=1.0):
    rows = []
    for threshold in thresholds:
        predicted = threshold_predictions(scores, threshold)
        summary = classification_summary(actual, predicted)
        summary["threshold"] = threshold
        summary["alerts"] = summary["tp"] + summary["fp"]
        summary["cost"] = expected_error_cost(actual, predicted,
                                                false_positive_cost,
                                                false_negative_cost)
        rows.append(summary)
    return rows


def best_threshold(actual, scores, thresholds, false_positive_cost=1.0,
                   false_negative_cost=1.0):
    rows = threshold_table(actual, scores, thresholds, false_positive_cost,
                           false_negative_cost)
    if not rows:
        raise ValueError("at least one threshold is required")
    return min(rows, key=lambda row: (row["cost"], -row["recall"], row["alerts"]))
