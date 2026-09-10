"""Dependency-light split and cross-validation helpers."""

import random


def holdout_indices(size, train_fraction=0.6, validation_fraction=0.2, seed=0, shuffle=True):
    if not isinstance(size, int) or size < 3:
        raise ValueError("size must be an integer of at least three")
    if train_fraction <= 0 or validation_fraction <= 0 or train_fraction + validation_fraction >= 1:
        raise ValueError("fractions must be positive and leave a test portion")
    indices = list(range(size))
    if shuffle:
        random.Random(seed).shuffle(indices)
    train_end = int(size * train_fraction)
    validation_end = train_end + int(size * validation_fraction)
    if train_end == 0 or validation_end == train_end or validation_end == size:
        raise ValueError("each split must contain at least one observation")
    return {"train": indices[:train_end], "validation": indices[train_end:validation_end], "test": indices[validation_end:]}


def kfold_indices(size, folds=5, seed=0, shuffle=True):
    if not isinstance(size, int) or size < 2:
        raise ValueError("size must be at least two")
    if not isinstance(folds, int) or not 2 <= folds <= size:
        raise ValueError("folds must be between two and size")
    indices = list(range(size))
    if shuffle:
        random.Random(seed).shuffle(indices)
    parts = [indices[offset::folds] for offset in range(folds)]
    result = []
    for fold in range(folds):
        validation = parts[fold]
        training = [index for part_number, part in enumerate(parts) if part_number != fold for index in part]
        result.append((training, validation))
    return result


def grouped_holdout(groups, test_groups):
    test_groups = set(test_groups)
    if not test_groups:
        raise ValueError("test_groups must not be empty")
    training = [index for index, group in enumerate(groups) if group not in test_groups]
    testing = [index for index, group in enumerate(groups) if group in test_groups]
    if not training or not testing:
        raise ValueError("both partitions must contain observations")
    return training, testing


def expanding_window_splits(size, initial_train, validation_size, step=None, gap=0):
    if not all(isinstance(value, int) for value in (size, initial_train, validation_size, gap)):
        raise TypeError("split sizes must be integers")
    step = validation_size if step is None else step
    if not isinstance(step, int):
        raise TypeError("step must be an integer")
    if size < 2 or initial_train < 1 or validation_size < 1 or step < 1 or gap < 0:
        raise ValueError("invalid split configuration")
    splits = []
    train_end = initial_train
    while train_end + gap + validation_size <= size:
        training = list(range(train_end))
        validation = list(range(train_end + gap, train_end + gap + validation_size))
        splits.append((training, validation))
        train_end += step
    if not splits:
        raise ValueError("configuration produces no split")
    return splits


def summarize_scores(scores):
    scores = [float(score) for score in scores]
    if not scores:
        raise ValueError("scores must not be empty")
    mean = sum(scores) / len(scores)
    return {"folds": len(scores), "mean": mean, "minimum": min(scores), "maximum": max(scores), "range": max(scores) - min(scores)}


def select_lowest_loss(losses):
    if not isinstance(losses, dict) or not losses:
        raise ValueError("losses must be a non-empty dictionary")
    return min(losses, key=lambda name: (float(losses[name]), str(name)))
