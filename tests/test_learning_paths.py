from pathlib import Path
import pytest
from datasciencebook.learning_paths import load_paths, available_paths, path_plan, plan_summary, check_progress

DATA = Path(__file__).parents[1] / "project" / "learning_paths.csv"

def test_paths_and_summary():
    rows = load_paths(DATA)
    assert len(available_paths(rows)) == 6
    assert plan_summary(rows, "analyst")["hours"] == 92
    assert [r["sequence"] for r in path_plan(rows, "deep")] == [1, 2, 3, 4]

def test_progress_and_unknown_path():
    plan = path_plan(load_paths(DATA), "leader")
    result = check_progress(plan, ["Chapters 1-6"])
    assert result["completed"] == 1
    assert result["next_resource"] == "Chapters 20-26"
    with pytest.raises(ValueError):
        path_plan(load_paths(DATA), "missing")
