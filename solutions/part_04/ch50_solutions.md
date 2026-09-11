# Chapter 50 Solutions

1. Inputs, weights, bias, preactivation, and activation/output.
2. $z=2(0.5)+3(-1)+1=-1$.
3. It shifts the boundary and permits a nonzero output when all inputs are zero.
4. $\sigma(0)=0.5$.
5. Identity returns any real preactivation; step returns a hard class; sigmoid returns a smooth value in `(0,1)`.
6. The model estimates risk; the threshold maps that estimate to an action under costs and capacity.
7. Holding the represented inputs fixed, greater moisture raises predicted log odds of damage.
8. The coefficient describes an associational prediction and can reflect confounding, selection, or proxy structure.
9. $-\log(0.8)\approx0.223$.
10. It prevents taking the logarithm of zero and avoids an infinite numerical result.
11. It scales each gradient update.
12. An epoch is a complete pass through training examples; mini-batch training makes several updates per epoch.
13. $z=Xw+b$, with the scalar bias broadcast across rows.
14. One unit's features generally receive different gradients. Identically initialized units in the same layer receive identical gradients and remain redundant.
15. XOR's positive points occupy opposite corners, so any line that isolates one positive corner misclassifies another corner.
16. Compare against baselines on a future-like test set; report log loss, calibration, ranking, cost at the operating threshold, capacity, subgroups, latency, drift, and reproducibility.
