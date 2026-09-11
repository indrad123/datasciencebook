# Chapter 53 Solutions

1. Optimization failure leaves both losses poor; overfitting produces a favorable training loss and worse validation performance.
2. They receive identical gradients and remain redundant.
3. Xavier uses fan-in and fan-out for tanh-like units; He uses fan-in with larger variance for ReLU-like units.
4. Results may depend on a fortunate initialization or batch order.
5. Fit mean and scale on training data and reuse the stored values everywhere else.
6. One transforms model inputs using training state; the other is a network layer using activation statistics.
7. Training uses current batches and updates running state; inference uses stored state.
8. Means and variances become noisy or unrepresentative.
9. A squared-weight penalty added to the objective.
10. Adaptive optimizers can couple an L2 gradient to their rescaling, unlike decoupled decay.
11. Mask during training and divide survivors by the keep probability.
12. Otherwise predictions remain random and have the wrong evaluation behavior.
13. Stop according to a predefined validation rule and restore the best checkpoint.
14. Mirroring an image when label orientation is operationally meaningful.
15. Train/validation loss, gradient norms, activation ranges, calibration, and subgroup metrics.
16. Hold splits and budget fixed, vary one control, repeat seeds, and select on predefined validation and operating constraints.
