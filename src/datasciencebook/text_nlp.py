"""Small NLP workflow helpers for Chapter 44."""
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,f1_score

def normalize_text(text):
    if not isinstance(text,str):raise ValueError("text must be a string")
    return " ".join(text.lower().strip().split())

def tokenize(text):return re.findall(r"(?u)\b\w\w+\b",normalize_text(text))

def fit_text_classifier(texts,labels,min_df=1):
    docs=list(texts);y=np.asarray(labels)
    if len(docs)<4 or len(y)!=len(docs) or len(set(y))<2:raise ValueError("aligned texts with at least two classes are required")
    vectorizer=TfidfVectorizer(ngram_range=(1,2),min_df=min_df,sublinear_tf=True)
    x=vectorizer.fit_transform(docs);model=LogisticRegression(max_iter=1000,random_state=44).fit(x,y);return vectorizer,model

def predict_text(vectorizer,model,texts):return model.predict(vectorizer.transform(list(texts)))

def classification_summary(actual,predicted):
    a=np.asarray(actual);p=np.asarray(predicted)
    if a.ndim!=1 or p.shape!=a.shape or len(a)==0:raise ValueError("labels must align")
    return {"accuracy":float(accuracy_score(a,p)),"macro_f1":float(f1_score(a,p,average="macro"))}

def top_coefficients(vectorizer,model,n=5):
    if model.coef_.shape[0]!=1 or n<1:raise ValueError("binary classifier and positive n required")
    names=np.asarray(vectorizer.get_feature_names_out());coef=model.coef_[0]
    return names[np.argsort(coef)[-n:][::-1]].tolist(),names[np.argsort(coef)[:n]].tolist()
