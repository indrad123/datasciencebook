import math
import pytest
from datasciencebook.sampling_distributions import finite_population_correction, sample_means, standard_error

def test_standard_error_and_correction():
    assert standard_error(10, 25) == 2
    assert finite_population_correction(100, 100) == 0
    assert math.isclose(finite_population_correction(100, 10), math.sqrt(90/99))

def test_reproducible_sampling_distribution():
    a=sample_means([1,2,3,4],2,5,seed=7)
    assert a==sample_means([1,2,3,4],2,5,seed=7)
    assert len(a)==5

def test_invalid_inputs():
    with pytest.raises(ValueError): standard_error(1,0)
    with pytest.raises(ValueError): finite_population_correction(10,11)
    with pytest.raises(ValueError): sample_means([1,2],3,2,replace=False)
