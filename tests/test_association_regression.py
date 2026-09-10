import pytest

from datasciencebook.association_regression import covariance, pearson_correlation, predict, simple_linear_regression, spearman_correlation


def test_covariance_and_correlations():
    assert covariance([1, 2, 3], [2, 4, 6]) == pytest.approx(2)
    assert pearson_correlation([1, 2, 3], [2, 4, 6]) == pytest.approx(1)
    assert spearman_correlation([1, 2, 3, 4], [1, 4, 9, 16]) == pytest.approx(1)
    assert spearman_correlation([1, 2, 2, 4], [4, 3, 3, 1]) == pytest.approx(-1)


def test_simple_regression_and_prediction():
    result = simple_linear_regression([5, 10, 15, 20], [36, 44, 52, 60])
    assert result["intercept"] == pytest.approx(28)
    assert result["slope"] == pytest.approx(1.6)
    assert result["r_squared"] == pytest.approx(1)
    assert result["rmse"] == pytest.approx(0)
    assert predict(result["intercept"], result["slope"], [25]) == pytest.approx([68])


@pytest.mark.parametrize("call", [lambda: covariance([1], [2]), lambda: pearson_correlation([1, 1], [2, 3]), lambda: simple_linear_regression([1, 1], [2, 3]), lambda: predict(0, 1, [float("nan")])])
def test_invalid(call):
    with pytest.raises(ValueError):
        call()
