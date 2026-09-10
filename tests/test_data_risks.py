import math
import pytest
from datasciencebook.data_risks import (
    audit_feature_availability, complete_case_mean, group_rate, missing_rate,
    missing_rates, random_split_indices, standardized_mean_difference,
    temporal_split_indices,
)


def test_missingness_and_complete_cases():
    assert missing_rate([1, None, 3, None]) == .5
    assert complete_case_mean([1, None, 3]) == 2
    assert missing_rates([{"x": 1}, {"x": None}], ["x"]) == {"x": .5}


def test_group_and_balance_diagnostics():
    rows = [{"g": "A", "y": 1}, {"g": "A", "y": 0}, {"g": "B", "y": 1}]
    assert group_rate(rows, "g", "y") == {"A": .5, "B": 1.0}
    assert math.isclose(standardized_mean_difference([1, 2, 3], [2, 3, 4]), -1.0)


def test_splits_and_leakage_audit():
    train, test = random_split_indices(10, .2, 7)
    assert len(train) == 8 and len(test) == 2 and not set(train) & set(test)
    assert temporal_split_indices([1, 2, 3, 4], 3) == ([0, 1], [2, 3])
    assert audit_feature_availability([1, 4, 2], [2, 3, 2]) == [False, True, False]


def test_invalid_inputs():
    with pytest.raises(ValueError): missing_rate([])
    with pytest.raises(ValueError): complete_case_mean([None])
    with pytest.raises(ValueError): random_split_indices(1)
    with pytest.raises(ValueError): temporal_split_indices([1, 2], 3)
