import json
import pytest
from datasciencebook.environment import package_version,readiness,save_report

def test_readiness_and_save(tmp_path):
    report={"virtual_environment":"/tmp/venv","commands":{"git":"/usr/bin/git"},"packages":{"numpy":"2.0"}}
    assert readiness(report)=={"ready":True,"issues":[]}
    path=save_report(report,tmp_path/'report.json');assert json.loads(path.read_text())==report

def test_missing_and_invalid():
    result=readiness({"virtual_environment":None,"commands":{},"packages":{"pytest":None}})
    assert not result['ready'] and len(result['issues'])==3
    with pytest.raises(ValueError):package_version('')
