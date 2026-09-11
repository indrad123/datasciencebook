# Chapter 31 Solutions

1. Cleaning changes values, rows, categories, units, or populations. Each decision can alter later estimates and therefore needs evidence and documentation.
2. Raw data preserve the received source. Intermediate data contain regenerable transformation stages. Analysis-ready data represent the declared unit and validated variables for a specific use.
3. Parsing converts an approved representation into a numeric type. Imputation estimates or assigns a value that was not observed.
4. The states have different meanings and mechanisms. Collapsing them loses evidence and can distort counts, averages, and missingness analysis.
5. The original supports audit and remapping. It also makes unknown or incorrectly merged categories detectable.
6. Deterministic means the same declared inputs and environment produce the same output. Idempotent means rerunning a completed step on its output does not continue to change it.
7. Comparison shows whether the intended changes occurred and reveals unexpected row loss, coverage shifts, or distribution changes.
8. Scaling parameters calculated from all rows use information from validation or test data. They must be learned on training data and then applied unchanged.
9. `1,200` becomes 1200; `900 units` becomes 900 under the approved suffix rule; `-` becomes missing with its status retained; `about 500` fails parsing and is flagged because it is not an exact observation.
10. Trim spaces, standardise case, and apply a versioned map of confirmed variants. Preserve `city_raw`, create `city_standard`, and flag unknown values without guessing.
11. Quarantine the conflict or stop the pipeline. Input order must not determine which disagreeing record wins.
12. Check unit, source, key, revision, customer type, product, related documents, and whether the order belongs to a distributor promotion rather than retail.
13. Suitable columns are step, input rows, output rows, affected values, and status. The entry should also be linked to the run and detailed log.
14. Examples include required schema, unique order ID after revision selection, successful parse rate above its threshold, valid date ordering, allowed currencies, and reconciliation of row counts. Any four justified checks earn credit.
15. Example:

```python
raw = {"product": "  Instant   Noodle ", "quantity": "1,200 units", "city": " JAKRTA "}
clean = {
    **raw,
    "product_clean": normalize_text(raw["product"]),
    "quantity_clean": parse_quantity(raw["quantity"]),
    "city_clean": map_category(raw["city"], {"jakrta": "Jakarta"}),
}
```

The raw fields remain available beside the cleaned fields.

16. Example:

```python
rows = [
    {"order_id": "A", "revision_number": 1, "quantity": 10},
    {"order_id": "A", "revision_number": 2, "quantity": 12},
    {"order_id": "B", "revision_number": 1, "quantity": 5},
]
final = latest_revisions(rows)
profile = numeric_profile([row["quantity"] for row in final])
log = transformation_record("select latest revision", 3, 2, 1)
```

The final quantities are 12 and 5, their mean is 8.5, and the ledger reports one affected row.
