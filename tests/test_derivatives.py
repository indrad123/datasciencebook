import pytest

from datasciencebook.derivatives import (
    average_rate,
    central_difference,
    forward_difference,
    tangent_line,
)


def test_rate_and_numerical_derivatives():
    assert average_rate(120, 180, 2, 5) == pytest.approx(20)
    square = lambda x: x**2
    assert forward_difference(square, 3, 1e-6) == pytest.approx(6, rel=1e-5)
    assert central_difference(square, 3, 1e-5) == pytest.approx(6)
    assert tangent_line(square, 3, [2, 3, 4]) == pytest.approx([3, 9, 15])


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        average_rate(1, 2, 3, 3)
    with pytest.raises(ValueError):
        central_difference(lambda x: x, 1, 0)
    with pytest.raises(ValueError):
        forward_difference(lambda x: x, float("inf"))
    with pytest.raises(ValueError):
        tangent_line(lambda x: x, 1, [float("nan")])
