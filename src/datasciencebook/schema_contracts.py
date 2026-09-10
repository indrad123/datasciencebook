"""Load and validate the machine-readable NRG data dictionary."""
from __future__ import annotations
import csv, json
from pathlib import Path


REQUIRED_FIELDS={"table","column","type","nullable","key","unit","description","allowed_or_rule"}


def load_dictionary(path):
    with Path(path).open(encoding="utf-8",newline="") as handle:
        rows=list(csv.DictReader(handle))
    if not rows or set(rows[0]) != REQUIRED_FIELDS:
        raise ValueError("dictionary fields do not match the required contract")
    return rows


def table_contract(rows, table):
    selected=[row for row in rows if row["table"]==table]
    if not selected:
        raise ValueError(f"unknown table: {table}")
    return {"table":table,"columns":[row["column"] for row in selected],"required":[row["column"] for row in selected if row["nullable"]=="false"],"keys":[row["column"] for row in selected if row["key"]]}


def validate_dictionary(rows):
    identities=[(row["table"],row["column"]) for row in rows]
    errors=[]
    if len(identities)!=len(set(identities)): errors.append("duplicate table-column entries")
    table_sequence=[row["table"] for row in rows]
    for table in set(table_sequence):
        positions=[i for i,value in enumerate(table_sequence) if value==table]
        if positions != list(range(min(positions),max(positions)+1)): errors.append(f"table {table} is not contiguous")
    for i,row in enumerate(rows,2):
        if not all(row[field].strip() for field in ("table","column","type","nullable","description")): errors.append(f"row {i} has blank required metadata")
        if row["nullable"] not in {"true","false"}: errors.append(f"row {i} has invalid nullable value")
    return {"rows":len(rows),"tables":sorted({row["table"] for row in rows}),"errors":errors,"valid":not errors}


def load_schema(path):
    value=json.loads(Path(path).read_text(encoding="utf-8"))
    required={"schema_version","dataset","fictional","timezone","grain","relationships"}
    if not required.issubset(value): raise ValueError("schema is missing required fields")
    return value
