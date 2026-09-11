# Chapter 35 Solutions

1. Predicting every transaction as legitimate achieves 99.5 per cent accuracy while finding no fraud. Report positive-class recall, precision, confusion counts, workload, and costs.
2. TP: a late shipment alerted. FP: an on-time shipment alerted. FN: a late shipment not alerted. TN: an on-time shipment not alerted.
3. Recall is the share of actual late shipments found. Precision is the share of alerts that are truly late.
4. With a rarer event, negatives contribute more false positives relative to true positives at similar class-conditional rates, lowering precision.
5. It exposes what accuracy is available without finding the minority class and sets a minimum comparator.
6. F1 ignores true negatives and gives an implicit balance to precision and recall that may not match actual costs, harms, or capacity.
7. Ranking quality concerns ordering positives above negatives. Calibration concerns agreement between stated probabilities and observed frequencies.
8. Choosing a threshold adapts the system to those outcomes and biases the final estimate. Select on validation data and test the frozen choice once.
9. Total is 1,000. Accuracy = 0.89; precision = 0.40; recall = 0.75; specificity = 830/920 = 0.9022; F1 = 0.5217; balanced accuracy = 0.8261.
10. The all-negative baseline has 0.92 accuracy and zero recall. It has higher accuracy but fails the detection purpose.
11. $90(40)+20(500)=13,600$.
12. A costs $160(40)+8(500)=10,400$. B costs $50(40)+25(500)=14,500$. Select A under these assumptions.
13. Only 92 and 55 alerts are feasible. The 92-alert threshold has the lower cost, 8,100.
14. Examples: majority baseline, which finds no leavers; current manager rule, which may be inconsistently applied; regularised logistic model, which may miss nonlinear structure. All must share the same information boundary.
15. Record the contamination definition, batch unit, prediction time, quarantine action, current-rule baseline, minimum recall, maximum laboratory capacity, costs, safety harms, subgroup checks, escalation owner, and frozen threshold process. Safety constraints should not be reduced to money alone.
16. Check prevalence and confusion counts, inspect precision-recall performance near the operating point, verify that evaluation preserved deployment prevalence, examine calibration, recalculate workload, review leakage, and assess whether capacity or threshold assumptions are realistic. Any four well-supported investigations earn full credit.
