import pytest
from datasciencebook.text_nlp import classification_summary,fit_text_classifier,normalize_text,predict_text,tokenize,top_coefficients

def test_pipeline():
    texts=["late delivery again","shipment delayed","thanks delivered","order arrived","very late shipment","delivery received"]
    y=[1,1,0,0,1,0];v,m=fit_text_classifier(texts,y);p=predict_text(v,m,texts);s=classification_summary(y,p)
    assert s["accuracy"]>=.8 and len(top_coefficients(v,m,2))==2
    assert normalize_text("  TERIMA   Kasih ")=="terima kasih" and tokenize("Order #42 late")==["order","42","late"]

def test_invalid():
    with pytest.raises(ValueError):normalize_text(None)
    with pytest.raises(ValueError):fit_text_classifier(["a","b"],[0,1])
