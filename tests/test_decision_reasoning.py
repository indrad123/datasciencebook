import pytest

from datasciencebook.decision_reasoning import (
    choose_intervention,
    expected_loss_no_action,
    intervention_threshold,
    realized_cost,
    select_with_capacity,
)


def test_threshold_and_choice():
    assert intervention_threshold(12, 80) == pytest.approx(0.15)
    assert expected_loss_no_action(0.2, 80) == pytest.approx(16)
    assert choose_intervention(0.2, 12, 80)
    assert not choose_intervention(0.1, 12, 80)


def test_capacity_and_realized_cost():
    actions = select_with_capacity([0.1, 0.8, 0.3, 0.6], 2)
    assert actions == [False, True, False, True]
    assert realized_cost([0, 1, 1, 0], actions, 12, 80) == 104


def test_invalid_inputs():
    with pytest.raises(ValueError):
        expected_loss_no_action(1.2, 80)
    with pytest.raises(ValueError):
        intervention_threshold(12, 0)
    with pytest.raises(ValueError):
        select_with_capacity([0.2], -1)
    with pytest.raises(ValueError):
        realized_cost([1], [], 12, 80)
