"""Validation and planning helpers for Appendix G learning paths."""
import csv
from collections import defaultdict

REQUIRED = {"path_id", "path_name", "stage", "sequence", "resource", "deliverable", "hours", "gate"}

def load_paths(path):
    with open(path, encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or not REQUIRED.issubset(rows[0]):
        raise ValueError("learning-path table is empty or missing required columns")
    for row in rows:
        row["sequence"] = int(row["sequence"])
        row["hours"] = float(row["hours"])
        if row["sequence"] < 1 or row["hours"] <= 0:
            raise ValueError("sequence and hours must be positive")
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["path_id"]].append(row["sequence"])
    for path_id, values in grouped.items():
        if sorted(values) != list(range(1, len(values) + 1)):
            raise ValueError(f"non-contiguous sequence for {path_id}")
    return rows

def available_paths(rows):
    return {row["path_id"]: row["path_name"] for row in rows}

def path_plan(rows, path_id):
    plan = sorted((r for r in rows if r["path_id"] == path_id), key=lambda r: r["sequence"])
    if not plan:
        raise ValueError(f"unknown path_id: {path_id}")
    return plan

def plan_summary(rows, path_id):
    plan = path_plan(rows, path_id)
    return {"path_id": path_id, "stages": len(plan), "hours": sum(r["hours"] for r in plan),
            "final_deliverable": plan[-1]["deliverable"]}

def check_progress(plan, completed_resources):
    completed = set(completed_resources)
    done = [row for row in plan if row["resource"] in completed]
    next_item = next((row for row in plan if row["resource"] not in completed), None)
    return {"completed": len(done), "total": len(plan), "hours_completed": sum(r["hours"] for r in done),
            "next_resource": None if next_item is None else next_item["resource"]}
