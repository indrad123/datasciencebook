import numpy as np
import pytest
from datasciencebook.dimensionality import apply_scaler,fit_pca,fit_scaler,reconstruction_error,top_loadings,variance_summary

def test_pca_round_trip_and_variance():
    x=np.array([[1,2,1],[2,4,0],[3,6,1],[4,8,0]],float)
    c,s=fit_scaler(x); z=apply_scaler(x,c,s); model,scores=fit_pca(z,3)
    assert scores.shape==(4,3)
    assert np.isclose(variance_summary(model)["cumulative"][-1],1)
    assert reconstruction_error(z,model.inverse_transform(scores))<1e-10
    assert len(top_loadings(model,["a","b","c"],2)[0])==2

def test_rejects_constant_and_bad_component_count():
    with pytest.raises(ValueError): fit_scaler([[1,2],[1,3]])
    with pytest.raises(ValueError): fit_pca([[1,2],[2,3]],3)
