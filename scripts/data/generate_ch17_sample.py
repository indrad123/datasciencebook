"""Generate deterministic distribution-shape data for Chapter 17."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch17_sample.csv';SEED=1717
def build_rows():
    rng=np.random.default_rng(SEED)
    series={
        'Symmetric routine':np.clip(rng.normal(5,1.15,60),1,9),
        'Right-skewed waiting':np.clip(rng.gamma(2.6,1.45,60),.3,14),
        'Routine plus disruption':np.r_[np.clip(rng.normal(4.7,.9,59),1.5,8),18.0],
    };rows=[]
    for scenario,values in series.items():
        for i,v in enumerate(values,1):
            outcome='Verified disruption' if scenario=='Routine plus disruption' and i==60 else 'Routine observation'
            rows.append({'observation_id':f"{scenario[:3].upper()}-{i:03d}",'scenario':scenario,'delivery_days':round(float(v),2),'review_outcome':outcome,'retained_in_analysis':'Yes'})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
