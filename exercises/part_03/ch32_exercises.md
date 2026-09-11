# Chapter 32 Exercises

## Concept and interpretation

1. Distinguish a raw variable from an engineered feature.
2. Why does prediction time constrain feature eligibility?
3. Explain why a ratio may need its numerator and denominator retained.
4. When is cyclic encoding more appropriate than using an ordinary month number?
5. Distinguish stateless and stateful transformations.
6. Explain why a category vocabulary must be fitted on training data.
7. Why can target encoding leak information?
8. Distinguish feature engineering from feature selection.

## Applied NRG tasks

9. Define three eligible features for a Monday demand forecast and three ineligible historical columns.
10. Write a complete definition for a four-week trailing demand mean.
11. A product has no prior sales because it is new. Propose a missing-history policy without pretending that demand was zero.
12. Explain how a promotion-by-discount interaction differs from the two original features.
13. List five checks for deciding whether an external competitor-price feature should be retained.
14. Identify two fairness or governance risks from using regional complaint rate as a feature.

## Code-supported tasks

15. Use `lag` and `trailing_mean` on weekly demand `[100, 120, 90, 140, 150]`. Explain exactly which observations contribute to the last feature value.
16. Fit categories on `['Jakarta', 'Dubai', 'Jakarta']`, encode `Jakarta` and unseen `Surabaya`, and create a registry record for the encoded feature.
