import pytest

from datasciencebook.confidence_intervals import bootstrap_mean_interval, normal_interval, wilson_interval


def test_normal_interval():
    low, high = normal_interval(100, 2)
    assert low == pytest.approx(96.080072)
    assert high == pytest.approx(103.919928)


def test_wilson_interval():
    low, high = wilson_interval(50, 100)
    assert low == pytest.approx(0.403832, abs=1e-6)
    assert high == pytest.approx(0.596168, abs=1e-6)


def test_bootstrap_is_reproducible():
    first = bootstrap_mean_interval([1, 2, 3, 4, 5], repetitions=500, seed=12)
    assert first == bootstrap_mean_interval([1, 2, 3, 4, 5], repetitions=500, seed=12)
    assert first[0] < 3 < first[1]


@pytest.mark.parametrize("call", [
    lambda: normal_interval(1, -1),
    lambda: wilson_interval(11, 10),
    lambda: bootstrap_mean_interval([], repetitions=100),
    lambda: bootstrap_mean_interval([1, 2], confidence_level=1, repetitions=100),
])
def test_invalid_inputs(call):
    with pytest.raises(ValueError):
        call()
