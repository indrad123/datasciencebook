import pytest

from datasciencebook.problem_definition import (
    is_actionable,
    is_available_at_use_time,
    missing_fields,
    readiness_score,
    upper_bound_value,
)


def complete_specification():
    return {field: "defined" for field in (
        "decision", "owner", "unit", "population", "outcome", "horizon",
        "use_time", "action", "baseline", "success_criteria"
    )}


def test_readiness_and_missing_fields():
    specification = complete_specification()
    assert missing_fields(specification) == []
    assert readiness_score(specification) == pytest.approx(1.0)
    specification["owner"] = " "
    assert missing_fields(specification) == ["owner"]
    assert readiness_score(specification) == pytest.approx(0.9)


def test_value_time_and_actionability():
    assert upper_bound_value(20_000, 0.02, 0.25, 30) == pytest.approx(3_000)
    assert is_available_at_use_time(8, 10)
    assert not is_available_at_use_time(12, 10)
    assert is_actionable(True, True, True, 200)
    assert not is_actionable(True, True, True, 0)


def test_invalid_inputs():
    with pytest.raises(TypeError):
        missing_fields([])
    with pytest.raises(ValueError):
        upper_bound_value(10, 1.2, 0.5, 2)
    with pytest.raises(ValueError):
        is_actionable(True, True, True, -1)
