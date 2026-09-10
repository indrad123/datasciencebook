"""Dependency-light utilities for connecting probabilities to simple decisions."""


def expected_loss_no_action(probability, late_loss):
    probability = float(probability)
    late_loss = float(late_loss)
    if not 0 <= probability <= 1:
        raise ValueError("probability must be between zero and one")
    if late_loss < 0:
        raise ValueError("late_loss must be non-negative")
    return probability * late_loss


def intervention_threshold(intervention_cost, avoided_loss):
    intervention_cost = float(intervention_cost)
    avoided_loss = float(avoided_loss)
    if intervention_cost < 0 or avoided_loss <= 0:
        raise ValueError("cost must be non-negative and avoided_loss positive")
    return intervention_cost / avoided_loss


def choose_intervention(probability, intervention_cost, avoided_loss):
    probability = float(probability)
    if not 0 <= probability <= 1:
        raise ValueError("probability must be between zero and one")
    return probability > intervention_threshold(intervention_cost, avoided_loss)


def select_with_capacity(probabilities, capacity):
    values = [float(value) for value in probabilities]
    if any(not 0 <= value <= 1 for value in values):
        raise ValueError("probabilities must be between zero and one")
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("capacity must be a non-negative integer")
    ranked = sorted(range(len(values)), key=lambda index: (-values[index], index))
    selected = set(ranked[:capacity])
    return [index in selected for index in range(len(values))]


def realized_cost(outcomes, actions, intervention_cost, late_loss):
    outcomes, actions = list(outcomes), list(actions)
    if not outcomes or len(outcomes) != len(actions):
        raise ValueError("outcomes and actions must be non-empty and equally sized")
    if any(value not in (0, 1, False, True) for value in outcomes + actions):
        raise ValueError("outcomes and actions must be binary")
    intervention_cost, late_loss = float(intervention_cost), float(late_loss)
    if intervention_cost < 0 or late_loss < 0:
        raise ValueError("costs must be non-negative")
    return sum(intervention_cost if action else late_loss * outcome for outcome, action in zip(outcomes, actions))
