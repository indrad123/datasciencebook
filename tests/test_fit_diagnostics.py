import pytest

from datasciencebook.fit_diagnostics import (
    bias_variance_at_point,
    diagnose_losses,
    early_stopping_epoch,
    generalization_gap,
    mean_squared_error,
    select_by_validation,
)


def test_losses_and_selection():
    assert mean_squared_error([1, 2], [1, 4]) == pytest.approx(2)
    assert generalization_gap(0.1, 0.3) == pytest.approx(0.2)
    candidates = [
        {"name": "simple", "training_loss": 0.3, "validation_loss": 0.35},
        {"name": "complex", "training_loss": 0.05, "validation_loss": 0.5},
    ]
    assert select_by_validation(candidates)["name"] == "simple"


def test_bias_variance_decomposition():
    result = bias_variance_at_point([8, 10, 12], truth=11, noise_variance=2)
    assert result["mean_prediction"] == pytest.approx(10)
    assert result["squared_bias"] == pytest.approx(1)
    assert result["variance"] == pytest.approx(8 / 3)
    assert result["expected_error"] == pytest.approx(17 / 3)


def test_stopping_and_diagnosis():
    result = early_stopping_epoch([0.8, 0.6, 0.5, 0.52, 0.55], patience=1)
    assert result == {"epoch": 3, "validation_loss": 0.5}
    assert diagnose_losses(0.6, 0.65, 0.4, 0.2) == "underfitting_signal"
    assert diagnose_losses(0.1, 0.5, 0.4, 0.2) == "overfitting_signal"


def test_invalid_inputs():
    with pytest.raises(ValueError):
        mean_squared_error([], [])
    with pytest.raises(ValueError):
        bias_variance_at_point([], 1)
    with pytest.raises(ValueError):
        bias_variance_at_point([1], 1, -1)
    with pytest.raises(ValueError):
        early_stopping_epoch([1], patience=-1)
