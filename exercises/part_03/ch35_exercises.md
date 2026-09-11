# Chapter 35 Exercises

## Concept checks

1. A fraud event occurs in 0.5 per cent of transactions. Explain why 99.5 per cent accuracy may describe a useless classifier.
2. Define the four cells of a confusion matrix for NRG's late-shipment case.
3. Explain the difference between precision and recall using operational language.
4. Why can precision change when prevalence changes even if recall and specificity remain similar?
5. What information does a majority baseline provide?
6. Why is F1 not automatically a business-value metric?
7. Distinguish ranking quality from probability calibration.
8. Explain why threshold choice must not use the final test set.

## Calculations

9. A model produces TP = 60, FP = 90, FN = 20, TN = 830. Calculate accuracy, precision, recall, specificity, F1, and balanced accuracy.
10. Compare the model in Exercise 9 with an all-negative baseline using accuracy and recall.
11. For FP cost 40 and FN cost 500, calculate the total error cost in Exercise 9.
12. Threshold A gives FP = 160 and FN = 8. Threshold B gives FP = 50 and FN = 25. Calculate cost using Exercise 11's costs and select the lower-cost threshold.
13. NRG can review 100 alerts. Thresholds produce 180, 105, 92, and 55 alerts with expected costs 7,000, 7,400, 8,100, and 12,000. Which feasible threshold has the lowest stated cost?

## Applied reasoning

14. Design three baselines for an employee-attrition model. State one limitation of each.
15. Propose an evaluation card for a rare product-contamination alert. Include safety and capacity constraints.
16. A classifier has strong ROC AUC but only 8 per cent precision at the operating threshold. Give four investigations before deployment.
