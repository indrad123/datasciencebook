"""Sampling-distribution helpers for Chapter 19."""

import math
import random


def standard_error(standard_deviation, sample_size):
    standard_deviation = float(standard_deviation)
    if not math.isfinite(standard_deviation) or standard_deviation < 0 or not isinstance(sample_size, int) or sample_size <= 0:
        raise ValueError("standard deviation must be non-negative and sample size positive")
    return standard_deviation / math.sqrt(sample_size)


def finite_population_correction(population_size, sample_size):
    if not isinstance(population_size, int) or not isinstance(sample_size, int) or population_size <= 1 or not 0 < sample_size <= population_size:
        raise ValueError("sizes must be valid integers with sample no larger than population")
    return math.sqrt((population_size - sample_size) / (population_size - 1))


def sample_means(population, sample_size, repetitions, seed=0, replace=True):
    values = [float(value) for value in population]
    if not values or not all(math.isfinite(value) for value in values):
        raise ValueError("population must contain finite values")
    if not isinstance(sample_size, int) or sample_size <= 0 or not isinstance(repetitions, int) or repetitions <= 0:
        raise ValueError("sample size and repetitions must be positive integers")
    if not replace and sample_size > len(values):
        raise ValueError("sample cannot exceed population without replacement")
    rng = random.Random(seed)
    means = []
    for _ in range(repetitions):
        sample = rng.choices(values, k=sample_size) if replace else rng.sample(values, sample_size)
        means.append(sum(sample) / sample_size)
    return means
