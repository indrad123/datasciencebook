import pytest

from datasciencebook.probability import bayes_binary, conditional_probability, expected_value


def test_probability_calculations():
    assert conditional_probability(0.12, 0.30) == pytest.approx(0.4)
    assert bayes_binary(0.02, 0.90, 0.05) == pytest.approx(18 / 67)
    assert expected_value([0, 100], [0.8, 0.2]) == pytest.approx(20)


def test_invalid_probabilities_rejected():
    with pytest.raises(ValueError):
        conditional_probability(0.1, 0)
    with pytest.raises(ValueError):
        conditional_probability(0.4, 0.3)
    with pytest.raises(ValueError):
        bayes_binary(1.2, 0.9, 0.1)
    with pytest.raises(ValueError):
        expected_value([1, 2], [0.2, 0.2])
