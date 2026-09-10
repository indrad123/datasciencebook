"""Generate deterministic measurement-error teaching data for Chapter 14."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch14_sample.csv';SEED=1414
def build_rows():
    rng=np.random.default_rng(SEED);refs=np.linspace(10,100,40);rows=[]
    for i,ref in enumerate(refs,1):
        biased=ref+.4+rng.normal(0,.25);unbiased=ref+rng.normal(0,.25)
        rows.append({'reading_id':f'M-{i:03d}','warehouse_code':['JKT','SBY','MDN','MKS'][(i-1)%4],'satisfaction_level':1+(i-1)%5,'ambient_temperature_c':round(22+5*np.sin(i/6),2),'reference_weight_kg':round(ref,3),'biased_scale_weight_kg':round(biased,3),'biased_signed_error_kg':round(biased-ref,3),'unbiased_scale_weight_kg':round(unbiased,3),'unbiased_signed_error_kg':round(unbiased-ref,3),'biased_absolute_error_kg':round(abs(biased-ref),3)})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
