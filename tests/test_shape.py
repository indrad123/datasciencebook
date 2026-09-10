import math

import pytest

from datasciencebook.shape import bowley_skewness, iqr_fences, iqr_flags, median_absolute_deviation, moment_skewness, robust_z_scores


def test_shape_and_fences():
    symmetric = [1, 2, 3, 4, 5]
    assert math.isclose(moment_skewness(symmetric), 0.0, abs_tol=1e-12)
    assert bowley_skewness(symmetric) == 0
    assert iqr_fences(symmetric) == (-1.0, 7.0)
    assert iqr_flags([1, 2, 3, 4, 20]) == [False, False, False, False, True]


def test_mad_and_robust_scores():
    values = [1, 2, 3, 4, 20]
    assert median_absolute_deviation(values) == 1
    scores = robust_z_scores(values)
    assert math.isclose(scores[2], 0)
    assert scores[-1] > 3.5


def test_invalid_inputs():
    with pytest.raises(ValueError):
        moment_skewness([1, 2])
    with pytest.raises(ValueError):
        iqr_fences([1, 2], -1)
    with pytest.raises(ValueError):
        robust_z_scores([2, 2, 2])
