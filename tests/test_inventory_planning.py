import numpy as np
import pytest
from datasciencebook.inventory_planning import *

def test_metrics_and_policy():
    assert np.isclose(wape([10, 20], [12, 18]), 4 / 30)
    assert service_quantile([-2, 0, 2], .5) == 0
    assert inventory_position(30, 10, 4) == 36
    assert order_up_to_quantity(53, 36, 12) == 24

def test_target_cost_and_coherence():
    report = lead_time_target([20, 22], [-3, 1, 5], .75)
    assert report["target"] > report["point_demand"]
    assert newsvendor_cost([8, 10, 12], 10, 1, 3) == 8 / 3
    assert coherent_total([[1, 2], [3, 4]]).tolist() == [4, 6]

def test_invalid_inputs():
    with pytest.raises(ValueError): wape([0, 0], [1, 2])
    with pytest.raises(ValueError): service_quantile([1, 2], 1)
    with pytest.raises(ValueError): inventory_position(-1)
    with pytest.raises(ValueError): order_up_to_quantity(10, 2, 0)
    with pytest.raises(ValueError): coherent_total([1, 2])
