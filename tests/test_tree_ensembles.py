import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from datasciencebook.tree_ensembles import *


def test_tree_profile_and_regression_report():
    x=[[0],[1],[2],[3]]; y=[0,1,4,9]
    m=fit_with_seed(DecisionTreeRegressor(max_depth=2),x,y)
    assert leaf_profile(m)["depth"]<=2
    assert regression_report(m,x,y)["mae"]>=0


def test_forest_report_and_importance():
    x=[[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]; y=[0,0,0,1,1,1]
    m=fit_with_seed(RandomForestClassifier(n_estimators=20),x,y)
    assert classification_report(m,x,y)["roc_auc"]>.8
    assert len(permutation_scores(m,x,y,"roc_auc",repeats=2))==2


def test_invalid():
    with pytest.raises(ValueError): validate_xy([],[])
    with pytest.raises(ValueError): classification_report(object(),[[1]],[1],1.2)
    with pytest.raises(ValueError): leaf_profile(object())
