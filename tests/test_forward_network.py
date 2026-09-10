import numpy as np
import pytest
from datasciencebook.forward_network import activation,dense_forward,forward_network,multiclass_cross_entropy,parameter_count

def test_activations_and_softmax():
    assert np.array_equal(activation([-1,2],"relu"),[0,2])
    assert np.allclose(activation([[1000,1001]],"softmax").sum(axis=1),1)

def test_shapes_trace_and_parameters():
    layers=[{"weights":np.ones((2,3)),"bias":np.zeros(3),"activation":"relu"},{"weights":np.ones((3,2)),"bias":np.zeros(2),"activation":"softmax"}]
    out,trace=forward_network([[1,2]],layers,True)
    assert out.shape==(1,2) and len(trace)==2 and parameter_count(layers)==17
    assert multiclass_cross_entropy([1],out)>0

def test_invalid_shape():
    with pytest.raises(ValueError): dense_forward([[1,2]],np.ones((3,2)),[0,0])
    with pytest.raises(ValueError): activation([1],"mystery")
