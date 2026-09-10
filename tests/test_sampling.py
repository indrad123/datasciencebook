import pytest

from datasciencebook.sampling import (
    arithmetic_mean,
    mean_estimation_error,
    sampling_fraction,
    simple_random_sample,
)


def test_population_and_sample_calculations():
    population = [10, 20, 30, 40, 50]
    sample = simple_random_sample(population, 3, seed=13)
    assert sample == [30, 50, 40]
    assert arithmetic_mean(population) == pytest.approx(30)
    assert sampling_fraction(3, 5) == pytest.approx(0.6)
    assert mean_estimation_error(population, sample) == pytest.approx(10)


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        arithmetic_mean([])
    with pytest.raises(ValueError):
        sampling_fraction(6, 5)
    with pytest.raises(ValueError):
        simple_random_sample([1, 2], 0, seed=13)
