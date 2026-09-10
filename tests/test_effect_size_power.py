import pytest
from datasciencebook.effect_size_power import binary_effects, cohens_d, required_sample_size, two_sided_z_power


def test_effect_sizes():
    assert cohens_d(105, 100, 10) == 0.5
    difference, ratio = binary_effects(90, 1000, 80, 1000)
    assert difference == pytest.approx(0.01)
    assert ratio == pytest.approx(1.125)


def test_power_and_sample_size():
    assert two_sided_z_power(0.5, 64) == pytest.approx(0.8074, abs=0.001)
    assert required_sample_size(0.5) == 63


@pytest.mark.parametrize("call", [lambda: cohens_d(1, 0, 0), lambda: binary_effects(2, 1, 0, 1), lambda: two_sided_z_power(1, 1)])
def test_invalid(call):
    with pytest.raises(ValueError):
        call()
