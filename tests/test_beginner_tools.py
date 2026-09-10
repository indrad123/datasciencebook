import pytest
from datasciencebook.beginner_tools import *

def test_description_and_mean():
    assert describe_value(" cases ", 12) == {"name":"cases","type":"int","value":12}
    assert safe_mean([2,4,6]) == 4

def test_filter_and_summary():
    rows=[{"product":"tea","cases":8},{"product":"coffee","cases":12}]
    assert filter_records(rows,"cases",10)==[rows[1]]
    assert case_summary(rows)=={"rows":2,"total_cases":20.0,"mean_cases":10.0}

def test_invalid_inputs():
    with pytest.raises(ValueError): describe_value("",1)
    with pytest.raises(ValueError): safe_mean([])
    with pytest.raises(ValueError): safe_mean([True])
    with pytest.raises(ValueError): filter_records([{}],"cases",1)
    with pytest.raises(ValueError): case_summary([{"cases":-1}])
