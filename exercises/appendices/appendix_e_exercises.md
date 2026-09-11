# Appendix E Exercises: Data Dictionary and Schema

1. Define the grain of `weekly_demand`.
2. Name its composite key.
3. Explain why `product_name` is not a suitable join key.
4. Distinguish `demand_cases` from `sales_cases` during a stockout.
5. State the valid range of `stockout_days`.
6. Explain why an inventory snapshot is not a movement table.
7. Write the formula for synthetic on-hand inventory value.
8. Explain why `forecast_origin` must be retained.
9. State the required relationship between p50 and p90.
10. Explain why `model_version` must be immutable.
11. Name four checks needed before joining demand to products.
12. Explain why a blank quantity must not automatically become zero.
13. Give one breaking, one backward-compatible, and one documentation-only schema change.
14. Explain how a many-to-many join can corrupt a demand total.
15. Identify the units of `service_target`, `case_cost_usd`, and `shelf_life_days`.
16. Explain how late data revision could create leakage in backtesting.
17. Propose two fields needed for a full inventory movement table.
18. Explain why a market and a distribution centre can both be locations but have different meanings.
19. Use the machine-readable dictionary to list the required forecast fields.
20. Write a five-check acceptance gate for a new NRG data extract.
