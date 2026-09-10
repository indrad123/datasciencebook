import pytest

from datasciencebook.group_comparisons import chi_square_independence, kruskal_wallis, one_way_anova, permutation_anova


def test_chi_square():
    result = chi_square_independence([[20, 10], [10, 20]])
    assert result["statistic"] == pytest.approx(6.6666666667)
    assert result["df"] == 1
    assert result["expected"] == [[15, 15], [15, 15]]


def test_anova_and_ranks():
    groups = [[8, 9, 10], [12, 13, 14], [16, 17, 18]]
    result = one_way_anova(groups)
    assert result["f_statistic"] == pytest.approx(48)
    assert result["eta_squared"] == pytest.approx(0.9411764706)
    assert kruskal_wallis(groups)["h_statistic"] == pytest.approx(7.2)


def test_permutation_reproducibility():
    groups = [[8, 9, 10], [12, 13, 14], [16, 17, 18]]
    assert permutation_anova(groups, 99, 42) == permutation_anova(groups, 99, 42)


@pytest.mark.parametrize("call", [lambda: chi_square_independence([[0, 0], [1, 2]]), lambda: one_way_anova([[1], [2]]), lambda: kruskal_wallis([[1, 1], [1, 1]]), lambda: permutation_anova([[1, 2], [3, 4]], 0)])
def test_invalid(call):
    with pytest.raises(ValueError):
        call()
