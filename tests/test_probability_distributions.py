import math
import pytest
from datasciencebook.probability_distributions import bernoulli_pmf, binomial_pmf, exponential_cdf, normal_cdf, poisson_pmf, uniform_cdf

def test_discrete_models():
    assert bernoulli_pmf(1, .2) == .2
    assert math.isclose(binomial_pmf(2, 4, .5), .375)
    assert math.isclose(poisson_pmf(0, 2), math.exp(-2))

def test_continuous_models():
    assert uniform_cdf(5, 0, 10) == .5
    assert normal_cdf(0) == .5
    assert math.isclose(exponential_cdf(2, .5), 1-math.exp(-1))

def test_invalid_inputs():
    with pytest.raises(ValueError): bernoulli_pmf(2, .5)
    with pytest.raises(ValueError): binomial_pmf(5, 4, .5)
    with pytest.raises(ValueError): poisson_pmf(-1, 2)
    with pytest.raises(ValueError): normal_cdf(0, 0, 0)
