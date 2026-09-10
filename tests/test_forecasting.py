import numpy as np
import pytest
from datasciencebook.forecasting import drift_forecast,mae,mase,naive_forecast,rmse,rolling_origins,seasonal_naive_forecast

def test_forecasts_metrics_and_origins():
    x=np.array([1,2,3,4,5,6],float)
    assert np.allclose(naive_forecast(x,2),[6,6])
    assert np.allclose(seasonal_naive_forecast(x,3,2),[5,6,5])
    assert np.allclose(drift_forecast(x,2),[7,8])
    assert mae([1,3],[2,3])==.5 and np.isclose(rmse([1,3],[2,3]),np.sqrt(.5))
    assert mase([7,8],[6,6],x)==1.5
    assert rolling_origins(10,5,2,2)==[(0,5,5,7),(0,7,7,9)]

def test_invalid_inputs():
    with pytest.raises(ValueError): seasonal_naive_forecast([1,2],1,3)
    with pytest.raises(ValueError): rolling_origins(5,4,2)
