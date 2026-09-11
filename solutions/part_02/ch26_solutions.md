# Chapter 26 Solutions

1. The sensor could fail, the reading could be inapplicable, transmission could be delayed, or the facility could omit it.
2. $45/300=0.15$, or 15%.
3. The rate describes how often values are absent, not why absence occurred or how it relates to unseen values.
4. Under MCAR, absence is unrelated to relevant values. Under MAR, it may depend on observed variables. Under MNAR, dependence on unobserved information remains after conditioning on recorded variables.
5. It can reduce precision and can change the represented population when excluded rows differ systematically.
6. A single inserted mean treats uncertain values as known and adds no natural variation, often narrowing variability and weakening relationships.
7. Selection bias, because portal adoption determines inclusion and may relate to distributor characteristics and outcomes.
8. Measurement bias caused by a changed recording process.
9. Urgent difficult shipments are more likely to receive premium freight and more likely to be late, so urgency can create or distort the observed association.
10. A confounder is a pre-exposure common cause. A mediator is caused by the exposure and lies on a causal pathway. A collider is caused by two variables and can create bias when conditioned on.
11. Approval occurs after dispatch and contains information about the eventual damage outcome that is unavailable at prediction time.
12. Test-set values influence the fitted centre and scale, so evaluation is no longer independent of training.
13. Rows from the same order may share customers, products, routes, or duplicated information; separating them can make the test set too familiar.
14. Train on records available through May, tune using June if required, and reserve July or a later untouched period for final evaluation. All features must use information available at each simulated prediction time.
15. Example: the feature indicates an official alert for the route; event time is agency issuance; availability time is successful ingestion into NRG; use only alerts ingested before dispatch confirmation and retain the ingestion timestamp.
16. Define the decision and cutoff time; map sources; profile missingness and selection; group related shipments; split chronologically; fit transformations on training data; audit feature availability; compare sensitivity results; and report limitations. Any six well-justified steps earn full credit.
