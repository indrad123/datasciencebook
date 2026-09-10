"""Small unit conversion helpers introduced in Chapter 1."""


def grams_to_kilograms(grams: float) -> float:
    """Convert a non-negative mass from grams to kilograms."""
    if grams < 0:
        raise ValueError("Mass cannot be negative in this context.")
    return grams / 1_000


def kilograms_to_grams(kilograms: float) -> float:
    """Convert a non-negative mass from kilograms to grams."""
    if kilograms < 0:
        raise ValueError("Mass cannot be negative in this context.")
    return kilograms * 1_000


def labelled_product_mass_grams(
    cartons: int, packs_per_carton: int, grams_per_pack: float
) -> float:
    """Calculate labelled product mass without packaging mass."""
    values = (cartons, packs_per_carton, grams_per_pack)
    if any(value < 0 for value in values):
        raise ValueError("Counts and labelled mass must be non-negative.")
    return cartons * packs_per_carton * grams_per_pack

