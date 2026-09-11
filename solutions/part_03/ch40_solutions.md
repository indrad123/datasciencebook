# Chapter 40 Solutions

1. Selection keeps original columns; extraction constructs new coordinates from them.
2. Compression, visualization, denoising, and downstream modelling.
3. Variance depends on numerical scale, so a large-unit feature can dominate component directions.
4. It maximizes projected input variance among unit-length directions.
5. Scores locate rows in component space; loadings describe feature contributions to each direction.
6. Reversing both a direction and its scores produces the same reconstruction and geometry.
7. It does not prove that 82 percent of target signal, decision value, or subgroup information is retained.
8. A global fit lets validation observations influence centring, scaling, and component directions.
9. It measures discrepancy between original and inverse-transformed values. It can monitor approximation quality or drift.
10. It may encode a rare failure signal or information strongly related to the target despite low marginal variance.
11. The optimizer, seed, hyperparameters, density, and local-neighbour objective shape the displayed gaps and sizes.
12. Repeat seeds, vary key hyperparameters, and refit on resampled observations.
13. Explicit centring makes a sparse matrix dense; truncated SVD can operate on the sparse representation.
14. Put preprocessing and PCA inside every training fold, tune component count, compare a no-reduction baseline, and evaluate the final choice once on untouched test data.
15. Purpose, input schema, fit population and dates, preprocessing parameters, algorithm version, component count, loadings, and validation results are valid examples.
16. Compare reconstruction error by product family, then compare demand-model error with and without PCA on chronological validation data.
