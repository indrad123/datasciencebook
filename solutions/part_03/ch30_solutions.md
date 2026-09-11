# Chapter 30 Solutions

1. A value can satisfy its type and range but represent a different event, unit, time, or population from the analytical definition.
2. Provenance records origin, meaning, movement, and transformation. Quality evaluates fitness for a declared use through dimensions such as completeness, validity, consistency, uniqueness, timeliness, and coverage.
3. It preserves evidence of what was received and allows repairs to be reproduced, compared, or reversed.
4. Missingness may be concentrated in one source, period, subgroup, or outcome. The total averages over that structure.
5. A positive weight is valid. A delivery time after dispatch is consistent with event order. Agreement between recorded weight and a calibrated scale concerns accuracy.
6. A weekly update can be fresh for a monthly report but stale for an hourly dispatch decision.
7. Repeated child records create several rows per parent. Unless aggregation is deliberate, parents with more child records receive more influence.
8. Repetition may represent exact copies, revisions, split shipments, or legitimate events. Removal without a rule can delete information or bias frequency.
9. It is ineligible for pre-dispatch prediction because it is created after the decision and may reveal the outcome. Using it would introduce leakage.
10. Example: at least 99.5 percent of eligible dispatched shipments per warehouse-day have a non-null `weight_kg` value before the daily snapshot closes.
11. Investigate whether the intended unit is shipment, whether duplicates are exact, whether there are status histories or split shipments, which sources created them, and which record-selection rule is legitimate.
12. Trace the warehouse feed and the July process change. Flag the affected warehouse-period, assess representativeness, repair or recollect if possible, and restrict temperature-dependent use until the issue is understood.
13. Suitable items include query version, source table and fields, extraction timestamp, filters, parameters, timezone, row count, schema version, and responsible owner. Any four earn credit.
14. Report source row counts, matched unique keys, left-only and right-only keys, duplicate keys on both sides, expected join cardinality, output row count, and the rule for multiple matches.
15. The result is:

```python
{
    "left_rows": 4,
    "right_rows": 3,
    "matched_unique_keys": 2,
    "left_only_keys": ["A"],
    "right_only_keys": ["D"],
    "duplicate_left_keys": {"B": 2},
    "duplicate_right_keys": {},
}
```

`B` and `C` match. `A` lacks a route record, `D` has no shipment, and `B` is duplicated on the left.

16. One valid example is:

```python
rules = {
    "shipment_id_unique": True,
    "weight_complete": True,
    "timestamps_ordered": False,
    "extract_fresh": True,
}
quality_gate(rules)
```

The result fails with `timestamps_ordered` in `failed_rules`. The pipeline should follow the severity assigned to that rule, quarantine or stop the affected build, trace the source, document the response, and rerun the test.
