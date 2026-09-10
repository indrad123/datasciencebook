"""Generate deterministic confidence-interval coverage data for Chapter 20."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch20_sample.csv';SEED=2020
def build_rows():
    rng=np.random.default_rng(SEED);mu=1000.;sigma=180.;n=40;z=1.96;se=sigma/np.sqrt(n);means=rng.normal(mu,se,200);rows=[]
    for i,m in enumerate(means,1):
        margin=z*se;lo=m-margin;hi=m+margin
        rows.append({'replicate_id':i,'sample_size':n,'sample_mean_weekly_units':round(float(m),3),'standard_error_units':round(float(se),3),'margin_of_error_units':round(float(margin),3),'ci_lower_units':round(float(lo),3),'ci_upper_units':round(float(hi),3),'covers_population_mean':'Yes' if lo<=mu<=hi else 'No','population_mean_weekly_units':mu})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
