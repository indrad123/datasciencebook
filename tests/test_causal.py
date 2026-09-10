import numpy as np
import pytest
from datasciencebook.causal import difference_in_means,ipw_weights,weighted_effect,standardized_mean_difference

def test_effect_and_weights():
    y=[4,6,3,5];t=[1,1,0,0];p=[.5]*4
    assert difference_in_means(y,t)==1
    w=ipw_weights(t,p);assert np.allclose(w,2)
    assert weighted_effect(y,t,w)==1

def test_balance_and_invalid():
    assert standardized_mean_difference([1,2,1,2],[0,0,1,1])==0
    with pytest.raises(ValueError): ipw_weights([0,2],[.2,.8])
