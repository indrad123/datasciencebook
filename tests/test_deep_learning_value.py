import pytest
from datasciencebook.deep_learning_value import *
def test_value_case():
 v=annual_value(1000,.2,.15,10);c=annual_cost(2,100,1000,.01,100)
 assert v==pytest.approx(500) and c==pytest.approx(310) and net_value(v,c)==pytest.approx(190)
 assert readiness_score(.8,.7,.9,.6)==.6 and recommend(190,.6)=="pilot"
def test_invalid():
 with pytest.raises(ValueError):annual_value(1,.2,1.2,1)
