"""Categorical association and group-comparison helpers for Chapter 24."""

import math
import random


def _groups(groups):
    data = [[float(v) for v in group] for group in groups]
    if len(data) < 2 or any(not group for group in data):
        raise ValueError("at least two non-empty groups are required")
    if not all(math.isfinite(v) for group in data for v in group):
        raise ValueError("values must be finite")
    return data


def chi_square_independence(table):
    rows = [[float(v) for v in row] for row in table]
    if len(rows) < 2 or any(len(row) != len(rows[0]) for row in rows) or len(rows[0]) < 2:
        raise ValueError("table must be rectangular with at least two rows and columns")
    if any(v < 0 or not math.isfinite(v) for row in rows for v in row):
        raise ValueError("counts must be finite and non-negative")
    row_totals = [sum(row) for row in rows]
    col_totals = [sum(rows[i][j] for i in range(len(rows))) for j in range(len(rows[0]))]
    total = sum(row_totals)
    if total == 0 or any(v == 0 for v in row_totals + col_totals):
        raise ValueError("all margins must be positive")
    expected = [[r * c / total for c in col_totals] for r in row_totals]
    statistic = sum((rows[i][j] - expected[i][j]) ** 2 / expected[i][j] for i in range(len(rows)) for j in range(len(rows[0])))
    return {"statistic": statistic, "df": (len(rows) - 1) * (len(rows[0]) - 1), "expected": expected}


def one_way_anova(groups):
    data = _groups(groups)
    n, k = sum(map(len, data)), len(data)
    if n <= k:
        raise ValueError("within-group degrees of freedom must be positive")
    grand = sum(sum(g) for g in data) / n
    means = [sum(g) / len(g) for g in data]
    ss_between = sum(len(g) * (m - grand) ** 2 for g, m in zip(data, means))
    ss_within = sum(sum((v - m) ** 2 for v in g) for g, m in zip(data, means))
    ss_total = ss_between + ss_within
    if ss_within == 0:
        raise ValueError("within-group variation must be positive")
    f_statistic = (ss_between / (k - 1)) / (ss_within / (n - k))
    return {"f_statistic": f_statistic, "df_between": k - 1, "df_within": n - k, "eta_squared": ss_between / ss_total if ss_total else 0.0, "means": means}


def _average_ranks(values):
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and ordered[end][1] == ordered[start][1]:
            end += 1
        rank = (start + 1 + end) / 2
        for position in range(start, end):
            ranks[ordered[position][0]] = rank
        start = end
    return ranks


def kruskal_wallis(groups):
    data = _groups(groups)
    values = [v for group in data for v in group]
    ranks = _average_ranks(values)
    n = len(values)
    offset, rank_sums = 0, []
    for group in data:
        rank_sums.append(sum(ranks[offset:offset + len(group)]))
        offset += len(group)
    h = 12 / (n * (n + 1)) * sum(r ** 2 / len(g) for r, g in zip(rank_sums, data)) - 3 * (n + 1)
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    correction = 1 - sum(c ** 3 - c for c in counts.values()) / (n ** 3 - n)
    if correction == 0:
        raise ValueError("ranks must vary")
    return {"h_statistic": h / correction, "df": len(data) - 1, "rank_sums": rank_sums}


def permutation_anova(groups, permutations=999, seed=0):
    data = _groups(groups)
    if permutations < 1:
        raise ValueError("permutations must be positive")
    observed = one_way_anova(data)["f_statistic"]
    sizes = [len(g) for g in data]
    pooled = [v for g in data for v in g]
    rng, extreme = random.Random(seed), 0
    for _ in range(permutations):
        shuffled = pooled[:]
        rng.shuffle(shuffled)
        split, offset = [], 0
        for size in sizes:
            split.append(shuffled[offset:offset + size])
            offset += size
        if one_way_anova(split)["f_statistic"] >= observed:
            extreme += 1
    return {"f_statistic": observed, "p_value": (extreme + 1) / (permutations + 1), "permutations": permutations}
