import numpy as np
import pytest
from datasciencebook.training_controls import *

def test_initialization_dropout_and_penalty():
 assert initialize_weights(4,3,"xavier",2).shape==(4,3)
 x=np.ones(10000);assert abs(dropout(x,.25,True,2).mean()-1)<.03
 assert np.array_equal(dropout(x,.5,False),x)
 assert l2_penalty([np.ones((2,2))],.1)==.2

def test_normalization():
 X=np.array([[1,10],[3,14],[5,18]],float);s=fit_standardizer(X);Z=apply_standardizer(X,s);assert np.allclose(Z.mean(0),0)
 B,_=batch_normalize(X);assert np.allclose(B.mean(0),0)

def test_invalid():
 with pytest.raises(ValueError):dropout([1],1)
