from datetime import datetime, timedelta

import pytest

from datasciencebook.provenance_quality import (
    age_hours,
    chronological_violations,
    duplicate_keys,
    join_reconciliation,
    missing_rate,
    quality_gate,
    range_violations,
)


def test_completeness_uniqueness_and_ranges():
    assert missing_rate([1, None, "", 4]) == pytest.approx(0.5)
    assert duplicate_keys(["S1", "S2", "S1"]) == {"S1": 2}
    assert range_violations([4, -1, None, 12], minimum=0, maximum=10) == [1, 3]


def test_time_and_join_checks():
    starts = [3, 5, None]
    ends = [4, 2, 9]
    assert chronological_violations(starts, ends) == [1]
    report = join_reconciliation(["S1", "S2", "S2"], ["S2", "S3"])
    assert report["matched_unique_keys"] == 1
    assert report["left_only_keys"] == ["S1"]
    assert report["duplicate_left_keys"] == {"S2": 2}


def test_freshness_and_gate():
    now = datetime(2026, 8, 30, 8)
    assert age_hours(now - timedelta(hours=6), now) == pytest.approx(6)
    assert quality_gate({"unique_key": True, "fresh": False}) == {
        "passed": False, "failed_rules": ["fresh"]
    }


def test_invalid_inputs():
    with pytest.raises(ValueError):
        missing_rate([])
    with pytest.raises(ValueError):
        range_violations([1, 2])
    with pytest.raises(ValueError):
        chronological_violations([1], [1, 2])
    with pytest.raises(ValueError):
        quality_gate({})
