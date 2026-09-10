import pytest

from datasciencebook.functions import linear_points, linear_value, line_intersection, slope_between


def test_linear_helpers():
    assert linear_value(50, 4, 300) == pytest.approx(500)
    assert slope_between(50, 500, 100, 700) == pytest.approx(4)
    assert line_intersection(4, 300, 6, 180) == pytest.approx((60, 540))
    assert linear_points([0, 1, 2], 2, 1) == [(0, 1), (1, 3), (2, 5)]


def test_undefined_cases_rejected():
    with pytest.raises(ValueError):
        slope_between(1, 2, 1, 5)
    with pytest.raises(ValueError):
        line_intersection(2, 1, 2, 5)
