# Chapter 42 Solutions

1. The origin is the latest information time; the horizon is how far beyond it the prediction extends.
2. Trend is sustained direction, seasonality repeats on a known calendar, and cycles can vary in length.
3. Future regimes, revisions, or neighbouring episodes can influence training and validation.
4. The forecast equals the latest observed value.
5. When a stable pattern repeats at a known calendar period.
6. Stockouts and supply constraints can suppress recorded sales below latent demand.
7. It exposes performance across seasons, regimes, origins, and horizons.
8. MAE weights absolute errors linearly; RMSE gives large errors more influence.
9. Division by zero is undefined and near-zero actuals create extreme percentages.
10. The forecast’s MAE is lower than the naive error used for scaling on the stated evaluation.
11. Otherwise backtesting uses information unavailable in production.
12. It adjusts forecasts so lower and higher hierarchy levels add up coherently.
13. An interval quantifies predictive uncertainty under assumptions; a scenario describes a conditional future path.
14. Origin, horizon, model version, inputs, forecast value, and later outcome are valid fields.
15. Use several historical origins, forecast 13 weeks each time, compare seasonal-naive and candidate models, and report horizon, product, and cost metrics before one untouched final period.
16. Compare original and overridden error, bias, service impact, frequency, and performance by stated reason.
