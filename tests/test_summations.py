import pytest

from datasciencebook.summations import conditional_sum, finite_sum, sum_squared_errors, weighted_sum


def test_valid_summations():
    assert finite_sum([42, 38, 45, 35]) == 160
    assert weighted_sum([20, 30, 25], [10, 5, 8]) == 550
    assert sum_squared_errors([10, 12, 9], [11, 10, 9]) == 5
    assert conditional_sum([80, 120, 150, 90], lambda value: value > 100) == 270


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        finite_sum([])
    with pytest.raises(ValueError):
        weighted_sum([1, 2], [1])
    with pytest.raises(ValueError):
        sum_squared_errors([1], [])
