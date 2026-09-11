# Chapter 11 Solutions

1. The decision variable is production quantity, the objective is the defined cost function, and capacity is a feasibility constraint.
2. \(18,6,2,6\), respectively.
3. \(w=4\) with loss 2.
4. \(L'(w)=2(w-4)\).
5. At zero the gradient is \(-8\), so \(w_1=0-0.1(-8)=0.8\).
6. \(w_1=0-0.5(-8)=4\), the exact minimum for this quadratic.
7. The gradient points towards locally increasing objective values; its negative points towards local decrease.
8. A parameter is fitted by the algorithm. A hyperparameter, such as learning rate, controls the fitting procedure and is set or tuned outside that update.
9. A zero gradient can occur at a maximum, saddle point, flat region, or local minimum.
10. \(\nabla f=[2(x-2),2(y+1)]^T\).
11. The gradient at \((0,0)\) is \((-4,2)\), so the new point is \((1,-0.5)\).
12. Examples are a small gradient norm, a small objective improvement, a small parameter change, or a validated iteration limit.
13. A full-batch gradient uses all observations; a stochastic gradient uses one or a subset and is cheaper but noisy.
14. Too large can overshoot or diverge; too small can make progress impractically slow.
15. Lower training loss can accompany overfitting. Selection must use validation performance and relevant constraints.
16. The update is \(w_1=w_0-0.5[2(w_0-4)]=4\).
