# Chapter 31 Exercises

## Concept and interpretation

1. Explain why cleaning is not a neutral operation.
2. Distinguish raw, intermediate, and analysis-ready data.
3. What is the difference between parsing a quantity and imputing a missing quantity?
4. Explain why unknown, missing, invalid, and zero should not automatically share one representation.
5. Give two reasons to retain an original text field after category standardisation.
6. Define deterministic and idempotent pipeline behaviour.
7. Why should a post-cleaning profile be compared with the source profile?
8. Explain why scaling the complete dataset before splitting can introduce leakage.

## Applied NRG tasks

9. NRG receives the values `1,200`, `900 units`, `-`, and `about 500`. Specify a defensible parsing result for each.
10. Draft a cleaning rule for city names that includes treatment of unknown categories.
11. Two rows share an order ID and revision number but contain different quantities. What should the pipeline do?
12. A 75,000-carton order is far above the retail distribution. List the investigations required before exclusion.
13. Design a five-column transformation ledger for selecting final order revisions.
14. Propose four validation checks that must pass before an analysis-ready order table is published.

## Code-supported tasks

15. Use `normalize_text`, `parse_quantity`, and `map_category` on three deliberately inconsistent NRG records. Show the result and preserve the raw values.
16. Create a small revision history, select the latest revisions, calculate a numeric profile, and create a `transformation_record` summarising the step.
