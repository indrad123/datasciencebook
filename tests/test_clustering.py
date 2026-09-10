import pytest
from sklearn.cluster import KMeans
from datasciencebook.clustering import *

def test_cluster_workflow():
    x=[[0,0],[0,.2],[5,5],[5,5.2]];c,s=fit_scaler(x);z=apply_scaler(x,c,s)
    m,l=fit_clusters(KMeans(n_clusters=2,n_init=10),z)
    assert len(cluster_profile(x,l))==2 and silhouette_report(z,l)['mean']>.8
    assert partition_agreement(l,l)==1

def test_invalid():
    with pytest.raises(ValueError):finite_matrix([])
    with pytest.raises(ValueError):cluster_profile([[1],[2]],[0])
    with pytest.raises(ValueError):silhouette_report([[1],[2]],[0,0])
