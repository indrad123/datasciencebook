"""Experimental-design and A/B-testing helpers for Chapter 25."""

import hashlib
import math
import random


def deterministic_assignment(unit_id, salt="nrg-ch25", treatment_share=0.5):
    """Assign a stable unit identifier to control (0) or treatment (1)."""
    if not 0 < treatment_share < 1:
        raise ValueError("treatment_share must be between zero and one")
    digest = hashlib.sha256(f"{salt}:{unit_id}".encode("utf-8")).digest()
    score = int.from_bytes(digest[:8], "big") / 2**64
    return int(score < treatment_share)


def difference_in_means(control, treatment):
    control = _finite(control, "control")
    treatment = _finite(treatment, "treatment")
    estimate = sum(treatment) / len(treatment) - sum(control) / len(control)
    return {"control_mean": sum(control) / len(control),
            "treatment_mean": sum(treatment) / len(treatment),
            "effect": estimate}


def conversion_effect(control_successes, control_total,
                      treatment_successes, treatment_total):
    for successes, total in ((control_successes, control_total),
                             (treatment_successes, treatment_total)):
        if not isinstance(successes, int) or not isinstance(total, int):
            raise ValueError("counts must be integers")
        if total <= 0 or successes < 0 or successes > total:
            raise ValueError("successes must be between zero and total")
    control_rate = control_successes / control_total
    treatment_rate = treatment_successes / treatment_total
    return {"control_rate": control_rate,
            "treatment_rate": treatment_rate,
            "risk_difference": treatment_rate - control_rate,
            "relative_lift": (treatment_rate / control_rate - 1)
            if control_rate else None}


def sample_ratio_mismatch(observed_treatment, total, expected_share=0.5):
    """Return a two-sided normal approximation for an assignment imbalance."""
    if not isinstance(observed_treatment, int) or not isinstance(total, int):
        raise ValueError("counts must be integers")
    if total <= 0 or observed_treatment < 0 or observed_treatment > total:
        raise ValueError("observed_treatment must be between zero and total")
    if not 0 < expected_share < 1:
        raise ValueError("expected_share must be between zero and one")
    expected = total * expected_share
    z = (observed_treatment - expected) / math.sqrt(total * expected_share * (1 - expected_share))
    p_value = math.erfc(abs(z) / math.sqrt(2))
    return {"z_score": z, "p_value": p_value,
            "observed_share": observed_treatment / total}


def permutation_difference(control, treatment, permutations=999, seed=0):
    control = _finite(control, "control")
    treatment = _finite(treatment, "treatment")
    if not isinstance(permutations, int) or permutations < 1:
        raise ValueError("permutations must be a positive integer")
    observed = difference_in_means(control, treatment)["effect"]
    pooled = control + treatment
    n_control = len(control)
    rng = random.Random(seed)
    extreme = 0
    for _ in range(permutations):
        shuffled = pooled[:]
        rng.shuffle(shuffled)
        candidate = difference_in_means(shuffled[:n_control], shuffled[n_control:])["effect"]
        extreme += abs(candidate) >= abs(observed)
    return {"effect": observed,
            "p_value": (extreme + 1) / (permutations + 1),
            "permutations": permutations}


def _finite(values, name):
    data = [float(value) for value in values]
    if not data or not all(math.isfinite(value) for value in data):
        raise ValueError(f"{name} must contain finite values")
    return data
