import numpy as np
import pytest
from datasciencebook.recommendation import latent_scores,ndcg_at_k,popularity_scores,precision_recall_at_k,rank_unseen

def test_scores_ranking_and_metrics():
    x=np.array([[2,0,1],[0,3,1],[1,0,4]],float)
    assert np.allclose(popularity_scores(x),[3,3,6]);assert latent_scores(x,2).shape==x.shape
    assert rank_unseen([.9,.8,.7],[1,0,0],2).tolist()==[1,2]
    assert precision_recall_at_k({1,3},[1,2,3],2)==(.5,.5)
    assert 0<ndcg_at_k({1,3},[1,2,3],3)<=1

def test_invalid():
    with pytest.raises(ValueError): latent_scores([[1,0],[0,1]],2)
    with pytest.raises(ValueError): rank_unseen([1,2],[1,1],1)
