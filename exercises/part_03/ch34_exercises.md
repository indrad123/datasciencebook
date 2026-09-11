# Chapter 34 Exercises

## Concept and interpretation

1. Distinguish training fit from generalisation.
2. Why can a small generalisation gap still describe a poor model?
3. Give three signs of underfitting.
4. Give three signs of overfitting.
5. Define bias and variance using repeated training samples.
6. What does irreducible noise mean in the squared-error decomposition?
7. Explain the classical bias-variance trade-off.
8. Why should the classical U-shaped curve not be treated as a universal law?

## Applied NRG tasks

9. Training MSE is 500 and validation MSE is 530. Diagnose the likely simple pattern and name two further checks.
10. Training MSE is 5 and validation MSE is 480. Recommend three responses.
11. Explain what a high-variance learning curve may look like as training size increases.
12. NRG adds one million near-duplicate rows. Explain why this may not solve overfitting.
13. Describe how early stopping uses validation data and why final testing is still required.
14. List five stability checks for a shipment-risk model.

## Code-supported tasks

15. Use `bias_variance_at_point` for predictions `[8, 10, 12]`, truth 11, and noise variance 2. Verify every component and the total.
16. Create four candidate complexity settings with training and validation losses. Use `select_by_validation`, calculate each gap, and explain why the lowest training loss need not win.
