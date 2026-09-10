import pytest

from datasciencebook.optimization import gradient_descent_1d, grid_search_1d


def test_grid_and_gradient_search():
    loss = lambda w: (w - 4) ** 2 + 2
    gradient = lambda w: 2 * (w - 4)
    assert grid_search_1d(loss, [0, 2, 4, 6]) == pytest.approx((4, 2))
    history = gradient_descent_1d(loss, gradient, 0, learning_rate=0.2, steps=100)
    assert history[-1][1] == pytest.approx(4, abs=1e-7)
    assert history[-1][2] == pytest.approx(2)
    assert all(b[2] <= a[2] for a, b in zip(history, history[1:]))


def test_invalid_configuration_rejected():
    with pytest.raises(ValueError):
        grid_search_1d(lambda x: x, [])
    with pytest.raises(ValueError):
        gradient_descent_1d(lambda x: x*x, lambda x: 2*x, 1, learning_rate=0)
    with pytest.raises(ValueError):
        gradient_descent_1d(lambda x: x*x, lambda x: 2*x, 1, steps=0)
