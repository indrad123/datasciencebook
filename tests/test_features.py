import pytest

from datasciencebook.features import (
    cyclic_encode,
    feature_record,
    fit_categories,
    interaction,
    lag,
    one_hot,
    safe_ratio,
    trailing_mean,
)


def test_ratio_cycle_and_interaction():
    assert safe_ratio(90, 100) == pytest.approx(0.9)
    assert safe_ratio(1, 0) is None
    sine, cosine = cyclic_encode(0, 12)
    assert sine == pytest.approx(0)
    assert cosine == pytest.approx(1)
    assert interaction(1, 0.15) == pytest.approx(0.15)


def test_lag_and_trailing_history_exclude_current():
    values = [10, 20, 30, 40]
    assert lag(values, 1) == [None, 10, 20, 30]
    assert trailing_mean(values, 2) == [None, None, 15, 25]
    assert trailing_mean(values, 2, minimum_history=1) == [None, 10, 15, 25]


def test_category_fit_and_transform():
    categories = fit_categories(["Jakarta", "Dubai", "Jakarta"])
    assert categories == ("Dubai", "Jakarta", "OTHER")
    assert one_hot("Jakarta", categories)["category_Jakarta"] == 1
    assert one_hot("Surabaya", categories)["category_OTHER"] == 1


def test_registry_and_invalid_inputs():
    record = feature_record("demand_lag_1", "previous completed week", "forecast origin", "cartons")
    assert record["version"] == "1.0"
    with pytest.raises(ValueError):
        cyclic_encode(1, 0)
    with pytest.raises(ValueError):
        lag([1, 2], 0)
    with pytest.raises(ValueError):
        trailing_mean([1, 2], 2, minimum_history=3)
    with pytest.raises(ValueError):
        one_hot("A", ("A", "A"))
