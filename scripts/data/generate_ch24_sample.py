"""Generate deterministic grouped shipment observations for Chapter 24."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'data/generated/ch24_sample.csv'
def build_rows():
    means={'Morning':18.4,'Evening':20.1,'Night':23.0};offsets=(-3.8,-2.9,-2.1,-1.5,-1.0,-.6,-.3,-.1,.2,.5,.8,1.1,1.4,1.8,2.3)*2
    rows=[]
    for s,(shift,mean) in enumerate(means.items()):
        centered=[x-sum(offsets)/len(offsets) for x in offsets]
        for i,o in enumerate(centered):
            picking=round(mean+o,2);warehouse=('Jakarta','Surabaya','Medan')[(i+s)%3]
            late='Yes' if (i*2+s*3)%10 < (2+s) else 'No';rating=max(1,min(5,5-int(round((picking-15)/3))+(i%3==0)))
            rows.append({'shipment_id':f'SHP-{s*30+i+1:03d}','shift':shift,'warehouse':warehouse,'late_delivery':late,'picking_minutes':picking,'distributor_rating':rating})
    return rows
def main():
    rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}')
if __name__=='__main__':main()
