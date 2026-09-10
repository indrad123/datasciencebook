import math

import pytest

from datasciencebook.summaries import (
    five_number_summary,
    interquartile_range,
    mean,
    median,
    quantile,
    sample_standard_deviation,
    sample_variance,
    weighted_mean,
)


def test_centre_and_quantiles():
    values = [1, 2, 3, 4, 5]
    assert mean(values) == 3
    assert median(values) == 3
    assert quantile(values, 0.25) == 2
    assert interquartile_range(values) == 2
    assert five_number_summary(values) == {"minimum": 1, "q1": 2, "median": 3, "q3": 4, "maximum": 5}


def test_weighted_mean_and_sample_spread():
    assert weighted_mean([10, 20], [1, 3]) == 17.5
    assert sample_variance([1, 2, 3, 4, 5]) == 2.5
    assert math.isclose(sample_standard_deviation([1, 2, 3, 4, 5]), math.sqrt(2.5))


@pytest.mark.parametrize("values", [[], [1, float("nan")]])
def test_invalid_values(values):
    with pytest.raises(ValueError):
        mean(values)


def test_invalid_arguments():
    with pytest.raises(ValueError):
        quantile([1, 2], 1.1)
    with pytest.raises(ValueError):
        weighted_mean([1, 2], [0, 0])
    with pytest.raises(ValueError):
        sample_variance([1])
