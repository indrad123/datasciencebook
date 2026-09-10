import pytest

from datasciencebook.data_quality import (
    classify_measurement_scale,
    measurement_errors,
    stratified_sample,
    systematic_sample,
)


def test_scales_and_sampling():
    assert classify_measurement_scale("ordinal").startswith("ordered categories")
    assert systematic_sample(range(10), 5) == [0, 2, 4, 6, 8]
    sample = stratified_sample({"A": [1, 2, 3], "B": [4, 5, 6]}, {"A": 2, "B": 1}, seed=14)
    assert sample == [1, 3, 5]


def test_measurement_error_summary():
    result = measurement_errors([12, 19, 33], [10, 20, 30])
    assert result["errors"] == pytest.approx([2, -1, 3])
    assert result["bias"] == pytest.approx(4 / 3)
    assert result["mean_absolute_error"] == pytest.approx(2)


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        classify_measurement_scale("numeric")
    with pytest.raises(ValueError):
        systematic_sample([1, 2], 3)
    with pytest.raises(ValueError):
        measurement_errors([1], [1, 2])
