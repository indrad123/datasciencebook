# Chapter 59 Solutions

1. Each Monday after close, forecast cases demanded for each product-centre pair over the next 13 weeks, using only origin-time information, to support replenishment orders.
2. Stockouts censor transactions: customers may have wanted units that were unavailable, so recorded sales can be below latent demand.
3. Examples are unique grain keys, complete weekly timestamps, nonnegative cases, valid master-data identifiers, known-at-origin promotions, reconciled inventory, freshness, and schema checks.
4. It lets later observations influence training for earlier predictions and does not reproduce operational forecasting.
5. Train through an origin, forecast the next 13 weeks, record errors, advance the origin, and repeat while preserving chronology.
6. WAPE is undefined when the sum of absolute actuals is zero. Report product and horizon errors, distributions, baseline-relative measures, and decision costs too.
7. Otherwise differences may come from splits, horizons, features, or tuning access rather than the model.
8. Forecasts are coherent when lower-level product forecasts sum exactly to their centre, region, and company forecasts.
9. The point forecast estimates expected demand. The target adds uncertainty and policy choices such as a service quantile.
10. \(120+24-8=136\) cases.
11. The raw need is 87. Rounding upward to packs of 12 gives 96 cases.
12. Examples are uncertain lead time, expiry, minimum orders, shared storage, purchase budgets, transfers, and supplier capacity.
13. Store origin, versioned inputs, forecast, uncertainty, starting inventory, order, arrivals, actual demand, sales, shortage, leftover, service, and cost.
14. Examples are shadow evaluation, a limited pilot, baseline fallback, manual exception review, frozen recommendations, tested rollback, and capacity validation.
15. Leading monitors include data freshness, missing series, forecast ranges, constraint violations, and overrides. Delayed monitors include forecast error, coverage, service, shortages, waste, and cost.
16. A strong memo defines scope and owner, compares the policy with a baseline on rolling origins, states cost and capacity assumptions, limits the first release, specifies overrides and rollback, and sets monitoring and expansion criteria.
