import numpy as np
import pytest
from datasciencebook.survival import kaplan_meier,survival_at,median_survival,restricted_mean_survival

def test_known_product_limit_curve():
    c=kaplan_meier([2,3,3,5],[1,1,0,1])
    assert np.allclose(c["survival"],[.75,.5,0])
    assert np.array_equal(c["at_risk"],[4,3,1])
    assert np.allclose(survival_at(c,[1,2,4]),[1,.75,.5])
    assert median_survival(c)==3
    assert restricted_mean_survival(c,4)==pytest.approx(3.25)

def test_invalid_inputs():
    with pytest.raises(ValueError): kaplan_meier([-1],[1])
    with pytest.raises(ValueError): kaplan_meier([1],[2])
