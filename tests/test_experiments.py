import pytest

from datasciencebook.experiments import (
    conversion_effect,
    deterministic_assignment,
    difference_in_means,
    permutation_difference,
    sample_ratio_mismatch,
)


def test_assignment_is_stable_and_binary():
    first = [deterministic_assignment(i) for i in range(100)]
    second = [deterministic_assignment(i) for i in range(100)]
    assert first == second
    assert set(first) == {0, 1}


def test_continuous_and_binary_effects():
    result = difference_in_means([10, 12, 14], [11, 15, 16])
    assert result["effect"] == pytest.approx(2.0)
    binary = conversion_effect(20, 100, 25, 100)
    assert binary["risk_difference"] == pytest.approx(0.05)
    assert binary["relative_lift"] == pytest.approx(0.25)


def test_ratio_and_permutation_reproducibility():
    assert sample_ratio_mismatch(50, 100)["z_score"] == 0
    a = permutation_difference([1, 2, 3], [4, 5, 6], 99, 42)
    assert a == permutation_difference([1, 2, 3], [4, 5, 6], 99, 42)


@pytest.mark.parametrize("call", [
    lambda: deterministic_assignment("x", treatment_share=1),
    lambda: difference_in_means([], [1]),
    lambda: conversion_effect(11, 10, 2, 10),
    lambda: sample_ratio_mismatch(11, 10),
    lambda: permutation_difference([1], [2], 0),
])
def test_invalid_inputs(call):
    with pytest.raises(ValueError):
        call()
