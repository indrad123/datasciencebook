import pytest

from datasciencebook.proportions import (
    fraction,
    percentage,
    percentage_change,
    percentage_point_change,
    unit_rate,
    weighted_percentage,
)


def test_core_calculations():
    assert fraction(3, 8) == pytest.approx(0.375)
    assert unit_rate(1440, 3) == pytest.approx(480)
    assert percentage(1170, 1250) == pytest.approx(93.6)
    assert percentage_change(800, 920) == pytest.approx(15)
    assert percentage_point_change(6, 4) == pytest.approx(-2)
    assert weighted_percentage([960, 1425], [1000, 1500]) == pytest.approx(95.4)


@pytest.mark.parametrize("call", [
    lambda: fraction(1, 0),
    lambda: unit_rate(10, 0),
    lambda: percentage_change(0, 10),
    lambda: weighted_percentage([1], [0]),
])
def test_zero_reference_rejected(call):
    with pytest.raises(ValueError):
        call()


def test_invalid_weighted_inputs_rejected():
    with pytest.raises(ValueError):
        weighted_percentage([1, 2], [3])
    with pytest.raises(ValueError):
        weighted_percentage([4], [3])
