import math
import pytest

from datasciencebook.notation import central_difference, dot, empirical_probability, euclidean_norm, sigma, weighted_sum


def test_sums_vectors_and_probability():
    assert sigma([1, 2, 3]) == 6
    assert weighted_sum([10, 20], [0.25, 0.75]) == 17.5
    assert dot([1, 2], [3, 4]) == 11
    assert euclidean_norm([3, 4]) == 5
    assert empirical_probability([True, False, True, True]) == 0.75


def test_derivative():
    assert math.isclose(central_difference(lambda x: x**2, 3), 6, rel_tol=1e-8)


@pytest.mark.parametrize("call", [
    lambda: sigma([]),
    lambda: weighted_sum([1], [1, 2]),
    lambda: empirical_probability([]),
    lambda: empirical_probability([1, 0]),
    lambda: central_difference(lambda x: x, 1, 0),
])
def test_invalid_inputs(call):
    with pytest.raises(ValueError):
        call()
