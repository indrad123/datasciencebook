import pytest

from datasciencebook.classification_metrics import (
    best_threshold, classification_summary, confusion_counts,
    expected_error_cost, threshold_predictions,
)


def test_counts_and_summary():
    actual = [1, 1, 0, 0, 0]
    predicted = [1, 0, 1, 0, 0]
    assert confusion_counts(actual, predicted) == {"tn": 2, "fp": 1, "fn": 1, "tp": 1}
    result = classification_summary(actual, predicted)
    assert result["accuracy"] == pytest.approx(0.6)
    assert result["precision"] == pytest.approx(0.5)
    assert result["recall"] == pytest.approx(0.5)


def test_cost_and_threshold_selection():
    actual = [1, 1, 0, 0]
    scores = [0.9, 0.4, 0.6, 0.1]
    assert expected_error_cost(actual, [1, 0, 1, 0], 2, 10) == 12
    result = best_threshold(actual, scores, [0.3, 0.5, 0.7], 2, 10)
    assert result["threshold"] == 0.3


def test_invalid_inputs():
    with pytest.raises(ValueError): confusion_counts([1], [])
    with pytest.raises(ValueError): threshold_predictions([1.2], 0.5)
    with pytest.raises(ValueError): threshold_predictions([0.2], -0.1)
    with pytest.raises(ValueError): expected_error_cost([1], [1], -1, 1)
