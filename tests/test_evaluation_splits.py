import pytest

from datasciencebook.evaluation_splits import (
    expanding_window_splits,
    grouped_holdout,
    holdout_indices,
    kfold_indices,
    select_lowest_loss,
    summarize_scores,
)


def test_holdout_is_reproducible_and_complete():
    first = holdout_indices(10, seed=7)
    second = holdout_indices(10, seed=7)
    assert first == second
    combined = first["train"] + first["validation"] + first["test"]
    assert sorted(combined) == list(range(10))
    assert len(set(combined)) == 10


def test_kfold_uses_each_validation_row_once():
    splits = kfold_indices(10, folds=5, shuffle=False)
    validation = [index for _, fold in splits for index in fold]
    assert sorted(validation) == list(range(10))
    assert all(not set(train) & set(valid) for train, valid in splits)


def test_groups_and_expanding_time():
    train, test = grouped_holdout(["A", "A", "B", "C"], {"C"})
    assert train == [0, 1, 2]
    assert test == [3]
    splits = expanding_window_splits(12, initial_train=6, validation_size=2, step=2, gap=1)
    assert splits[0] == (list(range(6)), [7, 8])
    assert splits[1] == (list(range(8)), [9, 10])


def test_score_summary_selection_and_errors():
    assert summarize_scores([0.2, 0.3])["mean"] == pytest.approx(0.25)
    assert select_lowest_loss({"A": 0.4, "B": 0.3}) == "B"
    with pytest.raises(ValueError):
        holdout_indices(2)
    with pytest.raises(ValueError):
        kfold_indices(3, folds=4)
    with pytest.raises(ValueError):
        expanding_window_splits(5, 4, 2)
    with pytest.raises(ValueError):
        summarize_scores([])
