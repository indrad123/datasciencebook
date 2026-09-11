# Appendix B Solutions

1. NumPy handles arrays, pandas labelled tables, Matplotlib plots, SciPy scientific algorithms, statsmodels estimation and inference, scikit-learn predictive pipelines, and PyTorch differentiable tensor models.
2. A list suits a small sequence, heterogeneous values, or simple control flow where vectorised numerical operations are unnecessary.
3. `shape` gives axis lengths, `ndim` gives the number of axes, and `dtype` describes stored element type.
4. `axis=0` aggregates across products for each week. `axis=1` aggregates across weeks for each product.
5. Broadcasting virtually aligns compatible shapes. An unintended compatible shape can produce a plausible but wrong result.
6. Basic slicing can return a view sharing the original array's memory. Use `.copy()` when independence is required.
7. Check key uniqueness, relationship type, match rate, row counts, unmatched keys, duplicate expansion, and effective dates. Any five earn credit.
8. `.loc[]` selects by labels; `.iloc[]` selects by integer positions.
9. A copy makes ownership clear and prevents ambiguous or unintended changes to a parent object.
10. Include a title or caption, axis labels, units, interpretable legend, appropriate scale, and accessible encoding.
11. SciPy supplies general scientific algorithms. statsmodels supplies fitted statistical models with inference and diagnostics.
12. Inference APIs emphasise parameters, uncertainty, and assumptions; predictive APIs emphasise out-of-sample performance and reusable transformations.
13. It means learning parameters from the supplied data, such as scaling constants, categories, or model coefficients.
14. It refits preprocessing inside each training fold and applies learned transformations to held-out data without fitting on it.
15. Load a batch, run forward calculation, calculate loss, clear gradients, backpropagate, and update parameters.
16. Hardware, parallel execution, library kernels, and nondeterministic algorithms can still differ.
17. JupyterLab is an interface, the kernel executes code, `nbformat` reads and validates notebook structure, and `nbclient` executes notebooks programmatically.
18. Direct assertions may cover calculations, but framework discovery, fixtures, parametrisation, complete collection, and standard reporting are not demonstrated.
19. Risks include lost labels, changed dtypes, reordered columns, memory copies, device transfers, missing-value changes, and shape errors.
20. One answer uses pandas for loading and validation, NumPy for calculations, Matplotlib or seaborn for reporting, scikit-learn for a leakage-safe pipeline, Jupyter for explanation, and pytest for reusable-code tests. PyTorch is added only if justified.
