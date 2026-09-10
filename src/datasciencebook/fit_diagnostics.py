"""Dependency-light diagnostics for fit, bias, and variance."""


def mean_squared_error(actual, predicted):
    actual, predicted = list(actual), list(predicted)
    if not actual or len(actual) != len(predicted):
        raise ValueError("actual and predicted must be non-empty and equal length")
    return sum((float(a) - float(p)) ** 2 for a, p in zip(actual, predicted)) / len(actual)


def generalization_gap(training_loss, validation_loss):
    return float(validation_loss) - float(training_loss)


def bias_variance_at_point(predictions, truth, noise_variance=0.0):
    predictions = [float(value) for value in predictions]
    if not predictions:
        raise ValueError("predictions must not be empty")
    if noise_variance < 0:
        raise ValueError("noise_variance must be non-negative")
    mean_prediction = sum(predictions) / len(predictions)
    squared_bias = (mean_prediction - float(truth)) ** 2
    variance = sum((value - mean_prediction) ** 2 for value in predictions) / len(predictions)
    return {
        "mean_prediction": mean_prediction,
        "squared_bias": squared_bias,
        "variance": variance,
        "noise": float(noise_variance),
        "expected_error": squared_bias + variance + float(noise_variance),
    }


def select_by_validation(candidates):
    if not candidates:
        raise ValueError("candidates must not be empty")
    required = {"name", "training_loss", "validation_loss"}
    if any(not required.issubset(candidate) for candidate in candidates):
        raise ValueError("every candidate requires name and losses")
    return min(candidates, key=lambda item: (float(item["validation_loss"]), str(item["name"])))


def early_stopping_epoch(validation_losses, patience=0):
    losses = [float(value) for value in validation_losses]
    if not losses:
        raise ValueError("validation_losses must not be empty")
    if not isinstance(patience, int) or patience < 0:
        raise ValueError("patience must be a non-negative integer")
    best_index, best_loss, stale = 0, losses[0], 0
    for index, loss in enumerate(losses[1:], start=1):
        if loss < best_loss:
            best_index, best_loss, stale = index, loss, 0
        else:
            stale += 1
            if stale > patience:
                break
    return {"epoch": best_index + 1, "validation_loss": best_loss}


def diagnose_losses(training_loss, validation_loss, acceptable_loss, gap_tolerance):
    training_loss, validation_loss = float(training_loss), float(validation_loss)
    if min(training_loss, validation_loss, acceptable_loss, gap_tolerance) < 0:
        raise ValueError("losses and thresholds must be non-negative")
    if training_loss > acceptable_loss and validation_loss > acceptable_loss:
        return "underfitting_signal"
    if validation_loss - training_loss > gap_tolerance:
        return "overfitting_signal"
    return "no_simple_signal"
