import pytest

from datasciencebook.cleaning_pipeline import (
    category_counts,
    latest_revisions,
    map_category,
    normalize_text,
    numeric_profile,
    parse_quantity,
    transformation_record,
)


def test_text_quantity_and_mapping():
    assert normalize_text("  Instant   Noodle ") == "instant noodle"
    assert normalize_text(" ab-12 ", case="upper") == "AB-12"
    assert parse_quantity("1,200 units") == pytest.approx(1200)
    assert parse_quantity("-") is None
    assert map_category(" JAKRTA ", {"jakrta": "Jakarta"}) == "Jakarta"


def test_revision_selection_and_profiles():
    rows = [
        {"order_id": "A", "revision_number": 1, "quantity": 10},
        {"order_id": "A", "revision_number": 2, "quantity": 12},
        {"order_id": "B", "revision_number": 1, "quantity": 5},
    ]
    selected = latest_revisions(rows)
    assert [row["quantity"] for row in selected] == [12, 5]
    assert numeric_profile([12, 5, None])["mean"] == pytest.approx(8.5)
    assert category_counts(["Jakarta", "Dubai", "Jakarta"]) == {"Dubai": 1, "Jakarta": 2}


def test_transformation_record():
    assert transformation_record("deduplicate", 100, 96, 4)["output_rows"] == 96


def test_invalid_inputs():
    with pytest.raises(ValueError):
        parse_quantity("about 500")
    with pytest.raises(ValueError):
        normalize_text("x", case="title")
    with pytest.raises(ValueError):
        latest_revisions([
            {"order_id": "A", "revision_number": 1, "quantity": 2},
            {"order_id": "A", "revision_number": 1, "quantity": 3},
        ])
    with pytest.raises(ValueError):
        transformation_record("bad", 2, -1, 0)
