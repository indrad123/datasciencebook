import pytest

from datasciencebook.distributions import contingency_table, empirical_cdf, frequency_table, histogram_counts


def test_frequency_and_cumulative_tables():
    assert frequency_table(["tea", "coffee", "tea"]) == [
        ("coffee", 1, pytest.approx(1 / 3)),
        ("tea", 2, pytest.approx(2 / 3)),
    ]
    assert empirical_cdf([1, 1, 3]) == [(1, pytest.approx(2 / 3)), (3, pytest.approx(1))]


def test_cross_table_and_histogram():
    rows, columns, matrix = contingency_table(["A", "A", "B"], ["yes", "no", "yes"])
    assert rows == ["A", "B"] and columns == ["no", "yes"]
    assert matrix == [[1, 1], [0, 1]]
    assert histogram_counts([0, 1, 2, 3, 4], [0, 2, 4]) == [2, 3]


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        frequency_table([])
    with pytest.raises(ValueError):
        contingency_table([1], [1, 2])
    with pytest.raises(ValueError):
        histogram_counts([1], [0, 0, 2])
