# Appendix A Solutions

1. Code is the instruction supplied to Python. Output is the value, text, figure, or error produced when it runs.
2. Restarting removes hidden state and confirms that dependencies are created in the visible execution order.
3. Suitable names are `product_id`, `weekly_cases`, and `is_promotion`.
4. They are `int`, `float`, `str`, `bool`, and `NoneType`.
5. `29 // 6` gives four full packs, and `29 % 6` gives five remaining cases.
6. `=` assigns a value to a name. `==` compares two values and produces a Boolean result.
7. `print(f"Demand: {84.25:.1f} cases")` reports `Demand: 84.2 cases`.
8. It returns `[20, 30]` because the ending position is excluded.
9. One answer is `{"product_id":"KOPI_200", "cases":48, "stockout":False}`.
10. `order = target - position if position < target else 0` is one valid solution.
11. Initialise `total=0`, loop over the values, and update `total=total+value`.
12. `[value * 2 for value in [2,3,4]]` returns `[4,6,8]`.
13. `def revenue(cases, price_per_case): return cases * price_per_case`.
14. A parameter is a name in the function definition. An argument is a value passed during a call.
15. Explicit imports show where each name comes from and reduce accidental name collisions.
16. Check row count, columns, types, missingness, unique keys, units, ranges, categories, and dates. Any six earn credit.
17. Its shape is `(3, 2)`: three observations along the first axis and two values along the second.
18. Read the final line first because it identifies the exception type and immediate message.
19. Compare the active virtual environment and `sys.executable`; the failing terminal may use a different interpreter.
20. Move logic when it is reused, needs focused validation or tests, or makes the notebook's reasoning difficult to follow.
