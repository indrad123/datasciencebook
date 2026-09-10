import numpy as np
import pytest
from datasciencebook.generative import *

def test_linear_autoencoder():
    x=np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]],float);m,c=fit_linear_autoencoder(x,1)
    z=encode(x,m,c);r=decode(z,m,c)
    assert z.shape==(4,1) and np.allclose(r,x) and np.allclose(reconstruction_error(x,r),0)

def test_latent_operations():
    path=interpolate_latent([0,0],[2,4],3);assert path.tolist()==[[0,0],[1,2],[2,4]]
    assert np.allclose(reparameterize([1,2],[0,0],[.5,-.5]),[1.5,1.5])

def test_invalid():
    with pytest.raises(ValueError):fit_linear_autoencoder(np.ones((2,2)),2)
    with pytest.raises(ValueError):interpolate_latent([0],[1],1)
