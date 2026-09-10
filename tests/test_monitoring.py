import pytest
from datasciencebook.monitoring import population_stability_index,latency_summary,missing_rate,breach
def test_stable_and_service_metrics():
 assert population_stability_index([1,2,3,4],[1,2,3,4],2)==0
 assert latency_summary([10,20,30])["p50"]==20
 assert missing_rate([1,float('nan')])==.5
 assert breach(.3,.2,.4)=="warning"
def test_invalid():
 with pytest.raises(ValueError): latency_summary([-1])
