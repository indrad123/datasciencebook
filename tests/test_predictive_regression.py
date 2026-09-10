import pytest
from datasciencebook.predictive_regression import *


def test_linear_fit():
    x=[[0],[1],[2],[3]]; y=[1,3,5,7]
    b,w=linear_fit(x,y,steps=3000)
    assert b==pytest.approx(1,abs=.01) and w[0]==pytest.approx(2,abs=.01)
    assert mean_absolute_error(y,linear_predict(x,b,w))<.01


def test_logistic_fit_and_standardize():
    x=[[-2],[-1],[1],[2]]; y=[0,0,1,1]
    means,scales=standardize_fit(x); z=standardize_apply(x,means,scales)
    b,w=logistic_fit(z,y,steps=3000)
    p=probability_predict(z,b,w)
    assert p[0]<.1 and p[-1]>.9 and log_loss(y,p)<.2


def test_invalid():
    with pytest.raises(ValueError): linear_fit([],[])
    with pytest.raises(ValueError): logistic_fit([[1]],[2])
    with pytest.raises(ValueError): log_loss([1],[1.2])
