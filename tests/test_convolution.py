import numpy as np
import pytest
from datasciencebook.convolution import *
def test_convolution_pool_shape():
 x=np.arange(25).reshape(5,5);k=np.ones((3,3));assert convolve2d(x,k).shape==(3,3);assert max_pool2d(x).shape==(2,2)
 assert output_size(32,3,1,1)==32 and conv_parameter_count(3,3,3,16)==448
def test_edge_and_field():
 x=np.zeros((5,5));x[:,3:]=1;k=np.array([[-1,0,1]]);assert convolve2d(x,k).max()>0;assert receptive_field([(3,1),(2,2),(3,1)])==8
def test_invalid():
 with pytest.raises(ValueError):output_size(2,3)
