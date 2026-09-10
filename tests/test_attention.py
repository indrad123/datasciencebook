import numpy as np
import pytest
from datasciencebook.attention import *

def test_attention_and_masks():
    q=np.eye(3); out,w=scaled_dot_product_attention(q,q,q)
    assert out.shape==(3,3) and np.allclose(w.sum(axis=1),1)
    _,cw=scaled_dot_product_attention(q,q,q,causal_mask(3))
    assert np.allclose(cw[np.triu_indices(3,1)],0)

def test_positions_padding_and_mean():
    p=sinusoidal_positions(4,5); assert p.shape==(4,5) and np.allclose(p[0,0::2],0) and np.allclose(p[0,1::2],1)
    m=padding_mask([2,3],3); assert m.tolist()==[[True,True,False],[True,True,True]]
    x=np.arange(12).reshape(2,3,2); assert masked_mean(x,m).shape==(2,2)

def test_invalid():
    with pytest.raises(ValueError): scaled_dot_product_attention(np.ones((2,3)),np.ones((2,2)),np.ones((2,2)))
    with pytest.raises(ValueError): causal_mask(0)
