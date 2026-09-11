# Chapter 55 Exercise Solutions

1. Order expresses syntax, timing, and relationships, so the same tokens in another order can make a different claim.
2. Near-duplicate messages or replies from one thread can enter both training and test data.
3. A query expresses what a position seeks, a key represents what each source offers for matching, and a value carries the information to mix.
4. Scaling controls the magnitude of dot products as key dimension grows and helps keep softmax from saturating.
5. Each row becomes non-negative and sums to one.
6. Self-attention draws all three matrices from one sequence; cross-attention uses queries from one representation and keys and values from another.
7. It prevents artificial padding positions from contributing information.
8. It prevents a position from using later positions, preserving the prediction-time boundary.
9. Without position features, the operation does not itself encode sequence order.
10. Multiple heads can learn different mixtures, but extra heads add cost and their patterns can be overinterpreted.
11. Attention, a position-wise feedforward network, residual connections, and normalization.
12. It reveals whether transformer complexity produces enough incremental operational value.
13. $500^2=250{,}000$ entries per head and example.
14. Compare fragmentation rates by language and inspect important product names, abbreviations, and informal spellings.
15. They are internal mixture coefficients and need not be faithful causal accounts of a prediction.
16. Record route and cost-weighted error, calibration or abstention, latency, message length, fragmentation, route proportions, language slices, delayed outcomes, ownership, thresholds, and response actions.
