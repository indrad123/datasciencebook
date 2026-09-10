import pytest

from datasciencebook.ml_bridge import (
    fit_simple_line,
    mean_absolute_error,
    mean_baseline,
    predict_constant,
    predict_line,
)


def test_baseline_and_mae():
    baseline = mean_baseline([12, 18, 15, 15])
    assert baseline == 15
    assert mean_absolute_error([10, 20], predict_constant(baseline, 2)) == 5


def test_simple_line():
    intercept, slope = fit_simple_line([1, 2, 3], [3, 5, 7])
    assert intercept == pytest.approx(1)
    assert slope == pytest.approx(2)
    assert predict_line([4], intercept, slope) == pytest.approx([9])


def test_invalid_inputs():
    with pytest.raises(ValueError):
        mean_baseline([])
    with pytest.raises(ValueError):
        mean_absolute_error([1], [])
    with pytest.raises(ValueError):
        fit_simple_line([1, 1], [2, 3])
