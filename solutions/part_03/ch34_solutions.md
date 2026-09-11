# Chapter 34 Solutions

1. Training fit measures performance on observations used to estimate the model. Generalisation concerns relevant unseen observations.
2. Training and validation losses can both be high and similar. The procedure then underfits without a large gap.
3. Signs include high loss on both sets, systematic residuals, compressed predictions, and failure to respond to known mechanisms. Any three earn credit.
4. Signs include very low training loss with worse validation loss, unstable folds or seeds, extreme rules, and reliance on identifiers. Any three earn credit.
5. Bias is the difference between the average prediction across fitted training samples and the true expected outcome. Variance is the spread of those fitted predictions around their average.
6. It is the conditional outcome variation not predictable from the available information under the decomposition assumptions. Better measurement or features can change what is available.
7. Increasing classical model complexity often reduces bias and increases variance, creating a possible intermediate minimum in generalisation error.
8. Over-parameterised models can show different variance and risk shapes, including double descent. Evaluation must rely on unseen-data evidence.
9. Both losses are high and close, suggesting underfitting. Check residual structure, baseline comparison, feature adequacy, optimisation, target quality, and validation alignment.
10. Reduce effective complexity or strengthen regularisation, collect more representative data, remove unstable features, constrain the search, or use an ensemble. Any three justified responses earn credit.
11. Training loss stays relatively low, validation loss is higher, and the gap may narrow as representative training data increase.
12. Near duplicates add little independent information and can make the sample appear larger without increasing coverage. They may reinforce existing errors or entities.
13. Validation loss selects the best checkpoint and therefore influences development. An untouched test set is still needed to evaluate the selected stopping procedure.
14. Suitable checks include folds, forecast origins, seeds, nearby hyperparameters, subgroups, data perturbations, prediction changes, feature stability, and workload. Any five earn credit.
15. The mean prediction is 10. Squared bias is $(10-11)^2=1$. Variance is $[(8-10)^2+(10-10)^2+(12-10)^2]/3=8/3$. Adding noise 2 gives expected error $1+8/3+2=17/3$.
16. Example:

```python
candidates = [
    {"name": "d1", "training_loss": 0.50, "validation_loss": 0.55},
    {"name": "d3", "training_loss": 0.22, "validation_loss": 0.25},
    {"name": "d6", "training_loss": 0.10, "validation_loss": 0.27},
    {"name": "d12", "training_loss": 0.01, "validation_loss": 0.60},
]
selected = select_by_validation(candidates)
gaps = {c["name"]: generalization_gap(c["training_loss"], c["validation_loss"]) for c in candidates}
```

`d3` wins on validation loss. `d12` has the best training loss but the largest gap and worst validation loss.
