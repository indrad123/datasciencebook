import numpy as np
import pytest
from datasciencebook.responsibility import *

def test_errors_and_slices():
    y=[0,1,0,1];p=[.1,.8,.7,.2];assert error_labels(y,p).tolist()==['TN','TP','FP','FN']
    rows=slice_error_rates(y,p,['a','a','b','b']);assert rows[0]['error_rate']==0 and rows[1]['error_rate']==1

def test_queue_and_readiness():
    assert review_queue([.1,.49,.51,.9],2).tolist()==[1,2]
    assert readiness_report({})['ready'] is False
    assert readiness_report({k:1 for k in ['owner','intended_use','test_slices','fallback','monitoring','rollback']})['ready']

def test_invalid():
    with pytest.raises(ValueError):error_labels([0],[1.2])
    with pytest.raises(ValueError):review_queue([.2],2)
