"""Generate repeated-sampling data for Chapter 19."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch19_sample.csv';SEED=1919
def build_rows():
    rng=np.random.default_rng(SEED);population=np.round(rng.lognormal(np.log(900),.55,5000),1);mu=population.mean();sigma=population.std(ddof=0);rows=[]
    for n in (1,5,30):
        means=rng.choice(population,size=(1000,n),replace=True).mean(axis=1)
        for i,m in enumerate(means,1):rows.append({'sample_size':n,'replicate_id':i,'sample_mean_weekly_units':round(float(m),3),'population_mean_weekly_units':round(float(mu),3),'population_sd_weekly_units':round(float(sigma),3),'theoretical_se_units':round(float(sigma/np.sqrt(n)),3),'sampling_method':'Independent sampling with replacement'})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
