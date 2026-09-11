# Chapter 33 Exercises

## Concept and interpretation

1. Distinguish training, validation, and test data.
2. Why does repeated test-set inspection invalidate its original role?
3. Explain why a familiar split percentage does not guarantee a credible evaluation.
4. Give an example where random row splitting violates independence.
5. Distinguish stratified, grouped, and time-aware cross-validation.
6. Why must imputation and scaling be fitted inside each fold?
7. Explain selection-induced optimism.
8. What separate roles do the inner and outer loops play in nested cross-validation?

## Applied NRG tasks

9. Design a split for predicting future shipments when several item rows belong to one order.
10. NRG predicts a 30-day outcome. Explain why a gap may be needed near a time boundary.
11. A team tries 100 configurations and reports the best five-fold score. Identify the problem and propose a correction.
12. State when leave-one-warehouse-out evaluation would be useful.
13. List six items that belong in an evaluation protocol record.
14. Explain what NRG should do after selecting a procedure but before a monitored production pilot.

## Code-supported tasks

15. Create five folds for 12 rows with a fixed seed. Verify that every row is used once for validation and no fold overlaps its training portion.
16. Create expanding-window splits for 20 weeks using 8 initial training weeks, 3 validation weeks, a step of 3, and a one-week gap. Interpret the first and final split.
