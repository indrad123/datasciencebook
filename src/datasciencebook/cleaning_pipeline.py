"""Dependency-light cleaning and reproducible-pipeline helpers."""

import re
from collections import Counter


def normalize_text(value, case="lower"):
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("value must be text or None")
    cleaned = " ".join(value.split())
    if case == "lower":
        return cleaned.lower()
    if case == "upper":
        return cleaned.upper()
    if case == "preserve":
        return cleaned
    raise ValueError("case must be lower, upper, or preserve")


def parse_quantity(value):
    if value is None:
        return None
    if isinstance(value, bool):
        raise ValueError("boolean is not a quantity")
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str):
        raise TypeError("quantity must be numeric, text, or None")
    text = value.strip().lower()
    if text in {"", "-", "na", "n/a"}:
        return None
    text = re.sub(r"\s*units?$", "", text).replace(",", "")
    if not re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)", text):
        raise ValueError(f"unsupported quantity: {value}")
    return float(text)


def map_category(value, mapping):
    normalized = normalize_text(value)
    normalized_mapping = {normalize_text(key): result for key, result in mapping.items()}
    return normalized_mapping.get(normalized, normalized)


def latest_revisions(records, key="order_id", revision="revision_number"):
    selected = {}
    for record in records:
        if key not in record or revision not in record:
            raise KeyError(f"records require {key} and {revision}")
        item_key = record[key]
        if item_key not in selected or record[revision] > selected[item_key][revision]:
            selected[item_key] = dict(record)
        elif record[revision] == selected[item_key][revision] and record != selected[item_key]:
            raise ValueError(f"conflicting final revision for {item_key}")
    return [selected[item_key] for item_key in sorted(selected, key=str)]


def numeric_profile(values):
    numbers = sorted(float(value) for value in values if value is not None)
    if not numbers:
        raise ValueError("at least one numeric value is required")
    return {
        "count": len(numbers),
        "minimum": numbers[0],
        "mean": sum(numbers) / len(numbers),
        "maximum": numbers[-1],
    }


def category_counts(values):
    return dict(sorted(Counter(values).items(), key=lambda pair: str(pair[0])))


def transformation_record(step, input_rows, output_rows, affected_values, status="passed"):
    if min(input_rows, output_rows, affected_values) < 0:
        raise ValueError("counts must be non-negative")
    if status not in {"passed", "warning", "failed"}:
        raise ValueError("unsupported status")
    return {
        "step": str(step), "input_rows": int(input_rows),
        "output_rows": int(output_rows), "affected_values": int(affected_values),
        "status": status,
    }
