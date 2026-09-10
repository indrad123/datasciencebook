import pytest
from sklearn.svm import SVC
from datasciencebook.distance_margin import *

def test_scaling_and_neighbours():
    x=[[0,10],[2,20],[4,30]]; m,s=fit_scaler(x); z=apply_scaler(x,m,s)
    assert z.shape==(3,2) and nearest_indices([0,10],x,2)==[0,1]

def test_svm_report():
    x=[[-2,-2],[-1,-1],[1,1],[2,2]]; y=[0,0,1,1]
    m=fit_with_seed(SVC(kernel='linear',probability=True),x,y)
    assert binary_report(m,x,y)['accuracy']==1 and support_summary(m)['total']>=2

def test_invalid():
    with pytest.raises(ValueError): fit_scaler([])
    with pytest.raises(ValueError): nearest_indices([0],[[0]],0)
    with pytest.raises(ValueError): support_summary(object())
