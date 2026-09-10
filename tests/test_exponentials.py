import pytest

from datasciencebook.exponentials import compound_value, log_base, time_to_target


def test_valid_calculations():
    assert compound_value(10000, 0.08, 2) == pytest.approx(11664)
    assert log_base(1000, 10) == pytest.approx(3)
    assert time_to_target(10000, 20000, 0.08) == pytest.approx(9.006468)


def test_invalid_domains_rejected():
    invalid_calls = [
        lambda: compound_value(-1, 0.1, 2),
        lambda: compound_value(10, -1, 2),
        lambda: log_base(0, 10),
        lambda: log_base(10, 1),
        lambda: time_to_target(0, 10, 0.1),
        lambda: time_to_target(10, 20, 0),
    ]
    for call in invalid_calls:
        with pytest.raises(ValueError):
            call()
