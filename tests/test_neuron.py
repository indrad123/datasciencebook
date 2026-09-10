import numpy as np
import pytest
from datasciencebook.neuron import binary_cross_entropy,classify,linear_output,neuron_probabilities,sigmoid,train_logistic_neuron

def test_linear_and_sigmoid():
    assert linear_output([2,3],[.5,-1],1)==-1
    assert sigmoid(0)==.5

def test_training_learns_or_gate():
    X=np.array([[0,0],[0,1],[1,0],[1,1]],float); y=np.array([0,1,1,1])
    fit=train_logistic_neuron(X,y,.5,3000)
    assert np.array_equal(classify(neuron_probabilities(X,fit['weights'],fit['bias'])),y)
    assert fit['loss_history'][-1] < fit['loss_history'][0]

def test_loss_and_validation():
    assert binary_cross_entropy([0,1],[.1,.9]) < .11
    with pytest.raises(ValueError): linear_output([1,2],[1])
    with pytest.raises(ValueError): train_logistic_neuron([[1]],[2])
