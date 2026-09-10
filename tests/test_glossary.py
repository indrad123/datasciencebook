from scripts.validate_glossary import glossary_report, parse_glossary


def test_parser():
    assert parse_glossary("**Alpha.** A useful definition here.\n") == [("Alpha", "A useful definition here.")]


def test_book_glossary_is_valid():
    report = glossary_report("book/appendices/appendix_d_glossary.md")
    assert report["valid"]
    assert report["entries"] >= 100
