# Chapter 37 Solutions

1. Internal nodes ask feature-threshold questions; paths define regions; leaves return a value or class proportion.
2. $2(0.3)(0.7)=0.42$.
3. It selects the best immediate gain without evaluating every possible future sequence of splits.
4. Maximum depth, minimum split size, minimum leaf size, maximum leaves, minimum impurity decrease, and pruning are valid.
5. A few observations determine the estimate, so small data changes can sharply change composition and probability.
6. Draw bootstrap training samples, fit one tree to each, and average predictions.
7. Each split considers a random subset of features, encouraging diversity and reducing tree correlation.
8. Strong individual trees reduce their errors, while low correlation makes averaging more effective.
9. Start from a constant, compute residuals, fit a small tree, multiply it by a learning rate, add it, and repeat.
10. Smaller contributions generally require more stages; both must be tuned together with tree complexity.
11. Impurity importance accumulates training split gains and can favour certain features. Permutation importance measures validation-score deterioration after shuffling but can create unrealistic data and is affected by correlation.
12. One feature can substitute for another, dividing or masking measured reliance. Direction and causality still do not follow.
13. Changed prevalence distorts precision, calibration, alert volume, and cost. Resampling belongs inside training folds.
14. Use earlier mature shipments for training, later periods for hyperparameter and threshold selection, and the latest untouched period for final comparison. Use identical features, availability rules, baselines, cost measures, calibration checks, and subgroup slices.
15. Do not select by ROC AUC alone. Recheck threshold and calibration on validation data, compare uncertainty and workload, and select the model with stable feasible decision value.
16. Monitor prevalence, mature confusion counts, precision, recall, cost, calibration, alert volume, latency, missingness, feature drift, out-of-range rows, subgroup performance, and fallback use with named owners.
