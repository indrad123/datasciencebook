import numpy as np
import pytest
from sklearn.ensemble import IsolationForest
from datasciencebook.anomaly import anomaly_scores,fit_detector,precision_at_capacity,robust_fit,robust_scores,select_for_review

def test_robust_and_model_scores_rank_extreme_row():
    x=np.array([[0,0],[.1,-.1],[-.1,.1],[8,9]],float)
    c,s=robust_fit(x); assert np.argmax(robust_scores(x,c,s))==3
    model=fit_detector(IsolationForest(n_estimators=50,contamination=.25),x)
    scores=anomaly_scores(model,x); selected=select_for_review(scores,1)
    assert selected[0]==3 and precision_at_capacity([0,0,0,1],selected)==1

def test_rejects_bad_inputs():
    with pytest.raises(ValueError): robust_fit([[1,2],[1,3]])
    with pytest.raises(ValueError): select_for_review([1,2],0)
