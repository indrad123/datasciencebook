import pytest

from datasciencebook.equations import evaluate_linear, solve_both_sides, solve_linear, verify_linear


def test_evaluate_and_solve_linear():
    assert evaluate_linear(18, 60, 120) == pytest.approx(1200)
    assert solve_linear(18, 120, 1200) == pytest.approx(60)
    assert verify_linear(18, 120, 1200, 60)


def test_both_sides_classification():
    assert solve_both_sides(4, 90, 2, 210) == ("unique", 60)
    assert solve_both_sides(3, 6, 3, 6) == ("infinite", None)
    assert solve_both_sides(2, 10, 2, 13) == ("none", None)


def test_invalid_input_rejected():
    with pytest.raises(ValueError):
        solve_linear(0, 2, 5)
    with pytest.raises(ValueError):
        verify_linear(1, 0, 1, 1, tolerance=-1)
