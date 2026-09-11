# Appendix E Solutions: Data Dictionary and Schema

1. One row per week, product, and market.
2. `week_start`, `product_id`, and `market_id`.
3. Names can change, differ in spelling, or be duplicated; the stable identifier preserves identity.
4. Demand estimates desired unconstrained quantity; sales record fulfilled quantity and can be suppressed by unavailable stock.
5. Zero through seven days inclusive.
6. It records state at one time and lacks the transactions needed to explain changes between times.
7. `on_hand_cases * unit_cost_usd`.
8. It identifies the information boundary and forecast vintage needed for leakage-safe evaluation and decision traceability.
9. Both are non-negative and `p90_cases >= p50_cases`.
10. Changing code or training data under one label prevents exact identification and reproduction of the forecast.
11. Example: key uniqueness, required columns, non-null keys, and foreign-key match rate.
12. Blank can mean unknown, unavailable, inapplicable, or failed collection; zero asserts a known quantity.
13. Rename `market_id`; add an optional description; correct a spelling error in prose without changing rules.
14. Multiple matching rows on both sides create repeated combinations, multiplying quantities after the join.
15. Proportion, US dollars per case, and days.
16. A later revised demand value or feature may contain information unavailable at the historical forecast origin.
17. Example: transaction timestamp, movement type, quantity, source location, destination location, and document ID.
18. They share an entity class and identifier scheme, but one represents a demand-planning market and the other a physical stock-holding facility.
19. `forecast_origin`, `target_week`, `product_id`, `market_id`, `model_version`, `p50_cases`, and `p90_cases`.
20. Example: verify schema version, required fields, unique keys, foreign-key matches, value ranges, chronology, units, row reconciliation, and synthetic-data labelling. Any five well-specified checks earn credit.
