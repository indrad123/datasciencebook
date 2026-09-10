"""Validated population and sampling helpers for Chapter 13."""

import math
import random


def _finite_numbers(values, name):
    numbers = [float(value) for value in values]
    if not numbers or not all(math.isfinite(value) for value in numbers):
        raise ValueError(f"{name} must be a non-empty sequence of finite numbers")
    return numbers


def arithmetic_mean(values):
    """Return the arithmetic mean of finite values."""
    numbers = _finite_numbers(values, "values")
    return sum(numbers) / len(numbers)


def sampling_fraction(sample_size, population_size):
    """Return the fraction of a finite population included in a sample."""
    if not isinstance(sample_size, int) or not isinstance(population_size, int):
        raise TypeError("sample_size and population_size must be integers")
    if population_size <= 0 or sample_size <= 0 or sample_size > population_size:
        raise ValueError("require 0 < sample_size <= population_size")
    return sample_size / population_size


def simple_random_sample(values, sample_size, seed):
    """Draw values without replacement using an explicit seed."""
    items = list(values)
    if not isinstance(sample_size, int) or sample_size <= 0 or sample_size > len(items):
        raise ValueError("sample_size must be a positive integer no larger than the population")
    return random.Random(seed).sample(items, sample_size)


def mean_estimation_error(population_values, sample_values):
    """Return sample mean minus population mean."""
    return arithmetic_mean(sample_values) - arithmetic_mean(population_values)
