"""Generate a deterministic synthetic NRG store population and sample."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/'data/generated/ch13_sample.csv'; SEED=1313

def build_rows():
    rng=np.random.default_rng(SEED)
    regions=[('Java','JAV',180),('Sumatra','SUM',90),('Kalimantan','KAL',50),('Sulawesi','SUL',50),('Eastern Indonesia','EAS',30)]
    formats=['Neighbourhood','Supermarket','Kiosk']; rows=[]; index=0
    region_effect={'Java':180,'Sumatra':80,'Kalimantan':30,'Sulawesi':50,'Eastern Indonesia':-20}
    format_effect={'Neighbourhood':0,'Supermarket':330,'Kiosk':-240}
    for region,code,count in regions:
        for local in range(1,count+1):
            index+=1; fmt=rng.choice(formats,p=[.48,.34,.18]); area=int(round({'Neighbourhood':115,'Supermarket':230,'Kiosk':42}[fmt]+rng.normal(0,18)))
            sales=int(round(780+2.25*area+region_effect[region]+format_effect[fmt]+rng.normal(0,115)))
            rows.append({'store_id':f'ID-{code}-{local:03d}','region':region,'store_format':fmt,'floor_area_m2':max(area,20),'weekly_sales_units':max(sales,100),'in_sampling_frame':'yes','selected_sample':'no'})
    # Simulate a master-store frame that misses 16 recently opened stores.
    omitted=rng.choice(len(rows),size=16,replace=False)
    for i in omitted: rows[int(i)]['in_sampling_frame']='no'
    eligible=[i for i,r in enumerate(rows) if r['in_sampling_frame']=='yes']
    selected=rng.choice(eligible,size=50,replace=False)
    for i in selected: rows[int(i)]['selected_sample']='yes'
    return rows
def main():
    rows=build_rows(); OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
