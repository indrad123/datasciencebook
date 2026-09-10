"""Statistical reporting checklist helpers."""
import json

def load_checklist(path):
    with open(path,encoding="utf-8") as f: data=json.load(f)
    if not data.get("sections"): raise ValueError("checklist requires sections")
    ids=[]
    for section in data["sections"]:
        if not section.get("id") or not section.get("items"): raise ValueError("invalid section")
        ids.extend(section["items"])
    if len(ids)!=len(set(ids)): raise ValueError("duplicate checklist item")
    return data

def item_ids(checklist): return [item for section in checklist["sections"] for item in section["items"]]

def evaluate_report(checklist,responses):
    valid=set(item_ids(checklist)); unknown=set(responses)-valid
    if unknown: raise ValueError(f"unknown items: {sorted(unknown)}")
    sections=[]
    for section in checklist["sections"]:
        complete=sum(bool(responses.get(i,False)) for i in section["items"])
        sections.append({"id":section["id"],"complete":complete,"total":len(section["items"]),"score":complete/len(section["items"])})
    done=sum(s["complete"] for s in sections); total=sum(s["total"] for s in sections)
    return {"complete":done,"total":total,"score":done/total,"ready":done==total,"sections":sections,
            "missing":[i for i in item_ids(checklist) if not responses.get(i,False)]}
