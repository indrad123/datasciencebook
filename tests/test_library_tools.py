import numpy as np
import pandas as pd
import pytest
from datasciencebook.library_tools import *

def test_array_report():
    result=array_report([[1,2],[3,4]])
    assert result["shape"]==(2,2) and result["ndim"]==2 and result["mean"]==2.5

def test_frame_contract():
    frame=pd.DataFrame({"id":[1,2],"value":[3.,4.]})
    assert frame_contract(frame,["id","value"],["id"])["valid"]
    assert frame_contract(frame,["other"])["missing_columns"]==["other"]

def test_versions_and_invalid():
    assert "numpy" in installed_versions(["numpy"])
    with pytest.raises(ValueError):array_report([])
    with pytest.raises(ValueError):array_report([1,np.nan])
    with pytest.raises(ValueError):installed_versions([""])
