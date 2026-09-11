# Chapter 27 Solutions

1. Both fields use data, probability, models, optimisation, and empirical checks.
2. Statistical inference often emphasizes uncertainty about populations or parameters; predictive machine learning often emphasizes performance on unseen cases.
3. Descriptive.
4. Predictive.
5. Decision.
6. One row should represent one shipment as known at dispatch confirmation.
7. A feature is an available input such as route distance; the target is the later outcome such as whether delivery was over 24 hours late.
8. It determines which information is legitimately available when the prediction is required.
9. Training examples $(\mathbf{x}_i,y_i)$ are used to estimate $\hat{f}$ so that $\hat{y}=\hat{f}(\mathbf{x})$.
10. $(12+18+15+15)/4=15$.
11. $(|10-15|+|20-15|)/2=5$.
12. Training error measures fit to examples used in learning; suitably independent test error better represents performance on unseen cases.
13. It may learn noise, and deployment data may differ from the training population or period.
14. Prediction can exploit association without identifying what would happen under an intervention.
15. Train and validate on records before July, preserve temporal order, and use July or the latest available pre-deployment period as the untouched test set.
16. A complete answer states the decision owner, observation unit, target, prediction time, population, baseline, metric, split, error costs, subgroup checks, and failure or retirement conditions. Any eight well-defined items earn full credit.
