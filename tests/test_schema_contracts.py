import pytest
from datasciencebook.schema_contracts import load_dictionary,load_schema,table_contract,validate_dictionary

DICTIONARY="data/dictionaries/nrg_data_dictionary.csv"
SCHEMA="data/dictionaries/nrg_schema.json"

def test_dictionary_and_schema():
    rows=load_dictionary(DICTIONARY);report=validate_dictionary(rows)
    assert report["valid"] and report["rows"]>=35 and len(report["tables"])==6
    assert table_contract(rows,"products")["keys"]==["product_id"]
    schema=load_schema(SCHEMA);assert schema["fictional"] is True and len(schema["relationships"])==8

def test_unknown_table():
    with pytest.raises(ValueError): table_contract(load_dictionary(DICTIONARY),"missing")
