import numpy as np
import pytest
from datasciencebook.backpropagation import finite_difference,forward,gradients,initialize,train

def test_gradient_and_xor_training():
 X=np.array([[0,0],[0,1],[1,0],[1,1]],float);y=np.array([0,1,1,0]);p=initialize(2,4,2);_,c=forward(X,p);g=gradients(y,p,c)
 assert np.isclose(g['W1'][0,0],finite_difference(X,y,p,'W1',(0,0)),rtol=1e-4)
 p,h,n=train(X,y,4,.5,4000,2);assert np.array_equal((forward(X,p)[0]>=.5).astype(int),y) and h[-1]<h[0]

def test_invalid_data():
 with pytest.raises(ValueError):train([[1]],[2])
