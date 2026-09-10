import numpy as np
import pytest
from datasciencebook.model_trust import brier_score,reliability_table,expected_calibration_error
def test_perfect_probabilities():
 assert brier_score([0,1],[0,1])==0
 assert expected_calibration_error([0,1],[0,1],2)==0
 assert sum(r[1] for r in reliability_table([0,1],[0,1],2))==2
def test_invalid():
 with pytest.raises(ValueError): brier_score([0,1],[.2,1.2])
