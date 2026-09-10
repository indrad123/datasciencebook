import numpy as np
import pytest
from datasciencebook.modality import *

def test_comparison_and_windows():
    assert np.isclose(relative_improvement(.8,.84),.05)
    assert np.isclose(relative_improvement(10,8,False),.2)
    assert window_count(100,20,10)==9 and value_per_compute(.1,2,10)>0

def test_group_split_and_summary():
    train,test=leakage_safe_split(['a','a','b','c'],['c']);assert train.tolist()==[True,True,True,False]
    assert candidate_summary(['x'],[.8],[1],[5])[0]['name']=='x'

def test_invalid():
    with pytest.raises(ValueError):window_count(5,6)
    with pytest.raises(ValueError):leakage_safe_split(['a'],['a'])
