from pathlib import Path
import pytest
from datasciencebook.reporting import load_checklist,item_ids,evaluate_report
DATA=Path(__file__).parents[1]/"project/statistical_reporting_checklist.json"
def test_complete_and_partial():
    c=load_checklist(DATA); ids=item_ids(c); assert len(ids)==20
    assert evaluate_report(c,{i:True for i in ids})["ready"]
    r=evaluate_report(c,{ids[0]:True}); assert r["complete"]==1 and len(r["missing"])==19
def test_unknown():
    with pytest.raises(ValueError): evaluate_report(load_checklist(DATA),{"invented":True})
