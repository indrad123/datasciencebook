# Chapter 32 Solutions

1. A raw variable is recorded by a source process. A feature is a value supplied to analysis and may be raw, transformed, aggregated, or combined.
2. A production decision can use only information available reliably before that time. Later information would cause leakage or make deployment impossible.
3. The same ratio can arise from very different scales. Numerator and denominator can preserve volume and help the model distinguish those cases.
4. It is suitable when positions wrap around, such as December and January, and the model should recognise their circular proximity.
5. A stateless transformation uses a fixed rule. A stateful transformation learns parameters or vocabulary from data and must preserve fitted state.
6. Fitting on validation or test data lets their distribution influence development and may change the production schema.
7. A category average can contain the current row's target or targets from the future. Out-of-fold and time-respecting estimation is required.
8. Feature engineering creates representations. Feature selection chooses which candidate features to retain.
9. Eligible examples are prior-week demand, planned discount, and days to a known holiday. Ineligible examples are final shipped quantity, end-of-week stockout reason, and actual completed-week returns.
10. For each product-warehouse-week, calculate the arithmetic mean of demand in the four completed weeks strictly before the forecast origin. Require four observed weeks, return missing otherwise, use cartons per week, and monitor history coverage.
11. Keep the lag features missing and add an indicator such as `is_new_product`. A separate product-family or launch baseline can be evaluated using information available at launch.
12. It represents the joint exposure. The promotion indicator identifies whether a promotion exists, discount gives magnitude, and their product activates magnitude only under promotion.
13. Check availability time, coverage, latency, stability, cost, legal use, subgroup quality, and out-of-sample contribution. Any five justified checks earn credit.
14. Complaint access and reporting behaviour may differ by region, so the rate can proxy infrastructure or socioeconomic conditions. Acting on it can reduce service to regions already underrepresented in complaints.
15. Example:

```python
values = [100, 120, 90, 140, 150]
lag(values, 1)
trailing_mean(values, 3)
```

The lag is `[None, 100, 120, 90, 140]`. With the default minimum history, the trailing mean is `[None, None, None, 103.333..., 116.666...]`. The final value uses 120, 90, and 140. It excludes the current value 150.

16. Example:

```python
categories = fit_categories(['Jakarta', 'Dubai', 'Jakarta'])
known = one_hot('Jakarta', categories)
unseen = one_hot('Surabaya', categories)
record = feature_record(
    'warehouse_one_hot',
    'one-hot encoding using training vocabulary and OTHER',
    'forecast origin',
    unit='indicator',
)
```

The fitted vocabulary is `('Dubai', 'Jakarta', 'OTHER')`. Jakarta activates its own column, while Surabaya activates `category_OTHER`.
