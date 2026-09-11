# Chapter 30 Exercises

## Concept and interpretation

1. Explain why a valid-looking value can still be unsuitable for analysis.
2. Distinguish data provenance from data quality.
3. Give two reasons why an analyst should retain an immutable raw snapshot.
4. Explain why an overall missing rate can conceal an operational failure.
5. Distinguish validity, consistency, and accuracy using shipment examples.
6. Why is freshness relative to a use rather than an absolute property?
7. Explain how a one-to-many join can unintentionally change the unit of analysis.
8. Why should duplicate records be investigated before removal?

## Applied NRG tasks

9. NRG predicts delay before dispatch. A field records the final customer complaint category. Assess its eligibility as a predictor.
10. Write a testable rule for shipment-weight completeness. Include a denominator and scope.
11. A table has 5,000 rows and 4,910 unique shipment IDs. What should the analyst investigate before deduplication?
12. Temperature is 96 percent complete overall but 62 percent complete in one warehouse during July. Recommend the next action.
13. List four items that should be recorded for an extraction from the transport system.
14. Define a reconciliation report for joining shipments to route records.

## Code-supported tasks

15. Use `join_reconciliation` for left keys `["A", "B", "B", "C"]` and right keys `["B", "C", "D"]`. Interpret every output field.
16. Create at least four Boolean rules for an NRG shipment snapshot and pass them to `quality_gate`. Explain whether the pipeline should proceed and what should happen after a failed rule.
