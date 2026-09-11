# Chapter 36 Solutions

1. Linear regression suits a numeric outcome; logistic regression suits a binary outcome probability.
2. One additional 100 km is associated with 0.7 additional predicted hours while represented features remain fixed.
3. The coefficient reflects conditional pattern under the fitted specification. Confounding, selection, measurement, and feature relationships can prevent causal interpretation.
4. Residual $=35-31=4$ hours.
5. Curvature, widening variance, time runs, group clusters, extreme influence, and systematic costly-direction errors are valid examples.
6. Odds $=0.8/0.2=4$. Log odds $=\log(4)\approx1.386$.
7. $e^{0.5}\approx1.649$.
8. The probability change depends on starting probability and all other inputs because the logistic mapping is nonlinear.
9. Full-data means and scales contain validation or test information. Fit on training data and apply unchanged elsewhere.
10. A feature combination perfectly separates observed classes and unregularised estimates may diverge. Causes include leakage, rare categories, deterministic rules, or small samples.
11. Ridge uses squared coefficients and usually shrinks all toward zero. Lasso uses absolute values and can set some exactly to zero. Both strengths require validation.
12. Thresholds convert probabilities into actions. The suitable value depends on error costs, capacity, prevalence, and required performance.
13. Train on earlier mature shipments, validate on a later period for transformations and regularisation, freeze the pipeline, and test on the latest untouched period. Report route and seasonal slices.
14. Report the slice failure, examine missing seasonal structure and drift, add defensible features or interactions within validation, and evaluate asymmetric operational cost before approval.
15. Flag the row as out of range, avoid automatic high-impact action, use a conservative fallback or human review, and collect representative data before extension.
16. Include outcome, horizon, population, features and availability, preprocessing, units, coefficients, regularisation, splits, baselines, metrics, residual or calibration checks, threshold and costs, ranges, slices, limitations, monitoring, and owners.
