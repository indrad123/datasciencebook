"""Generate the deterministic blocked A/B experiment for Chapter 25."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'data/generated/ch25_sample.csv'
def build_rows():
 rows=[];regions=('Java','Sumatra','Kalimantan','Sulawesi');tiers=('Standard','Key')
 for b,(region,tier) in enumerate((r,t) for r in regions for t in tiers):
  for arm in ('Control','Treatment'):
   completed=78 if arm=='Control' and b<4 else 77 if arm=='Control' else 85
   corrections=5 if arm=='Control' else 8;support=6 if arm=='Control' else 7
   for i in range(250):
    rows.append({'account_id':f'ACC-{len(rows)+1:04d}','region':region,'account_tier':tier,'randomization_block':f'{region}-{tier}','assignment':arm,'block_arm_index':i+1,'completed_order_7d':'Yes' if i<completed else 'No','correction_request':'Yes' if i<corrections else 'No','support_contact':'Yes' if corrections<=i<corrections+support else 'No'})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f'Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}')
if __name__=='__main__':main()
