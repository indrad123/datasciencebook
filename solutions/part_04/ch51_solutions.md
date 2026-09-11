# Chapter 51 Solutions

1. A matrix transformation, bias addition, and activation applied to a batch.
2. `(4,6)`.
3. The same length-six bias vector is added to every observation row.
4. Without nonlinearity, $(XW_1)W_2=X(W_1W_2)$ and offsets also combine.
5. ReLU clips negatives; sigmoid maps to `(0,1)`; tanh maps to `(-1,1)`; softmax normalizes class logits.
6. One identity output.
7. One sigmoid output.
8. Multiclass selects one exclusive class with softmax; multi-label uses independent sigmoids.
9. `(32,4) @ (4,6) -> (32,6) @ (6,3) -> (32,3)`.
10. It prevents overflow without changing normalized probabilities.
11. `4*6+6+6*3+3=51`.
12. It is the mean negative log probability assigned to the observed class.
13. It omits action costs, capacity, calibration needs, and stakeholder consequences.
14. Hidden ReLUs create features for the two ways inputs differ; their sum separates XOR.
15. Schema, compatible shapes, finite intermediates, softmax row sums, and batch consistency.
16. Record layer name, input/output shapes, activation, parameter count, range, mean, and nonfinite count.
