# Chapter 38 Solutions

1. Euclidean distance is $\sqrt{3^2+4^2}=5$. Manhattan distance is $3+4=7$.
2. Large-range features otherwise dominate a distance, changing which rows are closest and how margins are oriented.
3. Full-data scaling uses information from validation or test distributions. Learn parameters in each training fold and apply unchanged.
4. $k=1$ is flexible and noise-sensitive. Larger $k$ smooths predictions but can mix distinct regions and underfit.
5. Distance weighting, fixed class priority, and stable row ordering are valid if documented.
6. In many dimensions, observations become sparse and nearest and distant points can look less distinguishable, especially with irrelevant features.
7. A training point at or within the fitted margin that helps determine the SVM boundary.
8. Hard margin requires perfect separation. Soft margin permits violations and balances them against margin width.
9. Larger $C$ penalises violations more strongly; smaller $C$ allows more violations and stronger regularisation.
10. The losses are 0, 0.6, and 1.5.
11. A valid kernel directly calculates inner products corresponding to a feature space, allowing a linear separator there without explicitly materialising every transformed coordinate.
12. Small $\gamma$ gives broad smooth influence. Large $\gamma$ gives narrow local influence and a more flexible boundary.
13. The optimisation produces a margin-related score. Fit and validate a separate calibration mapping when probability is required.
14. Within chronological training folds, compare several $k$ values, distance metrics, and weights; compare logarithmic grids of $C$ and $\gamma$ for RBF SVM. Fit scaling inside every fold. Select with decision-relevant measures, then calibrate and set a threshold without using the final test.
15. Assess whether a linear model is adequate, reduce redundant rows or features, tune $C$ and $\gamma$, benchmark approximate or alternative algorithms, measure actual latency, and compare the performance gain with simpler baselines.
16. Flag the row using a training-distance threshold, prevent high-impact automatic action, route it to human review or a conservative rule, log the case, and collect mature outcomes before expanding coverage.
