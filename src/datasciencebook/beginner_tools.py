"""Small validated helpers used by Appendix A."""
from numbers import Real

def describe_value(name, value):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be nonempty text")
    return {"name": name.strip(), "type": type(value).__name__, "value": value}

def safe_mean(values):
    items = list(values)
    if not items or any(isinstance(x, bool) or not isinstance(x, Real) for x in items):
        raise ValueError("values must contain only numeric observations")
    return float(sum(items) / len(items))

def filter_records(records, key, minimum):
    if not isinstance(key, str) or not key or isinstance(minimum, bool) or not isinstance(minimum, Real):
        raise ValueError("key and numeric minimum are required")
    output = []
    for record in records:
        if not isinstance(record, dict) or key not in record:
            raise ValueError("every record must be a dictionary containing key")
        value = record[key]
        if isinstance(value, bool) or not isinstance(value, Real):
            raise ValueError("filtered values must be numeric")
        if value >= minimum:
            output.append(record.copy())
    return output

def case_summary(records):
    if not records:
        raise ValueError("records must not be empty")
    values = []
    for record in records:
        if not isinstance(record, dict) or "cases" not in record:
            raise ValueError("each record requires cases")
        value = record["cases"]
        if isinstance(value, bool) or not isinstance(value, Real) or value < 0:
            raise ValueError("cases must be nonnegative numbers")
        values.append(value)
    return {"rows": len(values), "total_cases": float(sum(values)), "mean_cases": safe_mean(values)}
