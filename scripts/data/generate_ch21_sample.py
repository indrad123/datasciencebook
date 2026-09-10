"""Generate deterministic null-model simulations for Chapter 21."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch21_sample.csv';SEED=2121
SCENARIOS=[('Precise small effect',.8,.20),('Precise meaningful effect',3.0,.70),('Uncertain small effect',.8,1.0),('Uncertain meaningful effect',3.0,2.0)]
def build_rows():
    rng=np.random.default_rng(SEED);rows=[];threshold=2.0
    for name,observed,se in SCENARIOS:
        null=rng.normal(0,se,2000);extreme=np.abs(null)>=abs(observed);p=(extreme.sum()+1)/(len(null)+1)
        for i,(v,e) in enumerate(zip(null,extreme),1):rows.append({'scenario':name,'permutation_id':i,'null_effect_units':round(float(v),4),'observed_effect_units':observed,'standard_error_units':se,'practical_threshold_units':threshold,'as_or_more_extreme':'Yes' if e else 'No','simulated_two_sided_p_value':round(float(p),6),'practically_meaningful':'Yes' if abs(observed)>=threshold else 'No'})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
