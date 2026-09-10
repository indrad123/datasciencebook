import pytest
from datasciencebook.hypothesis_tests import bonferroni_alpha, one_sample_z_test, permutation_mean_test, standardized_mean_difference


def test_z_test_and_effect_size():
    z, p = one_sample_z_test(104, 100, 2)
    assert z == 2
    assert p == pytest.approx(0.0455003)
    assert standardized_mean_difference(12, 10, 4) == 0.5


def test_multiplicity_and_permutation_reproducibility():
    assert bonferroni_alpha(0.05, 5) == pytest.approx(0.01)
    first = permutation_mean_test([8, 9, 10], [1, 2, 3], repetitions=500, seed=21)
    assert first == permutation_mean_test([8, 9, 10], [1, 2, 3], repetitions=500, seed=21)


@pytest.mark.parametrize("call", [lambda: one_sample_z_test(1, 0, 0), lambda: bonferroni_alpha(1, 2), lambda: permutation_mean_test([], [1], 100)])
def test_invalid(call):
    with pytest.raises(ValueError):
        call()
