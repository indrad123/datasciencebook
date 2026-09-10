import pytest

from datasciencebook.units import (
    grams_to_kilograms,
    kilograms_to_grams,
    labelled_product_mass_grams,
)


def test_grams_to_kilograms():
    assert grams_to_kilograms(24_480) == pytest.approx(24.48)


def test_kilograms_to_grams():
    assert kilograms_to_grams(3.5) == pytest.approx(3_500)


def test_labelled_product_mass():
    assert labelled_product_mass_grams(24, 12, 85) == pytest.approx(24_480)


@pytest.mark.parametrize("value", [-0.001, -1, -100])
def test_negative_mass_is_rejected(value):
    with pytest.raises(ValueError):
        grams_to_kilograms(value)


def test_negative_count_is_rejected():
    with pytest.raises(ValueError):
        labelled_product_mass_grams(-1, 12, 85)

