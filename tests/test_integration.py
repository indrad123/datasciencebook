import numpy as np
import pytest

from datasciencebook.integration import cumulative_trapezoidal, left_riemann, trapezoidal


def test_numerical_integrals():
    x = [0, 1, 2, 3]
    y = [0, 2, 4, 6]
    assert left_riemann(x, y) == pytest.approx(6)
    assert trapezoidal(x, y) == pytest.approx(9)
    assert cumulative_trapezoidal(x, y, initial=10).tolist() == pytest.approx([10, 11, 14, 19])


def test_unequal_intervals_and_invalid_data():
    assert trapezoidal([0, 1, 3], [2, 2, 2]) == pytest.approx(6)
    for x, y in [([0], [1]), ([0, 1], [1]), ([0, 0], [1, 2]), ([1, 0], [1, 2])]:
        with pytest.raises(ValueError):
            trapezoidal(x, y)
    with pytest.raises(ValueError):
        cumulative_trapezoidal([0, 1], [1, 2], initial=np.nan)
