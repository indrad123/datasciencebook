"""Generate deterministic delivery-time data for Chapter 16."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch16_sample.csv';SEED=1616
def build_rows():
    rng=np.random.default_rng(SEED);regions=['Jakarta','West Java','Central Java','East Java'];rows=[]
    values=np.clip(np.round(rng.gamma(3.0,.95,77),1),.8,8.5);values=np.concatenate([values,[10.5,13.0,18.0]])
    for i,x in enumerate(values,1):
        rows.append({'shipment_id':f'SHP-{i:03d}','region':regions[(i-1)%4],'delivery_days':float(x),'units':int(rng.integers(4,31)),'within_four_days':'Yes' if x<=4 else 'No','delay_band':'0-2 days' if x<=2 else ('2.1-4 days' if x<=4 else ('4.1-7 days' if x<=7 else 'Over 7 days'))})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
