"""Generate deterministic feasibility scenarios for Chapter 29."""
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data/generated/ch29_sample.csv'

def build_rows():
 rows=[];i=0
 for orders in (10000,20000,30000):
  for rate in (.01,.02,.04):
   for preventable in (.10,.25,.40):
    i+=1;events=orders*rate;addressable=events*preventable;value=addressable*30
    rows.append({'scenario_id':f'V-{i:02d}','eligible_orders':orders,'damage_return_rate':f'{rate:.2f}','preventable_fraction':f'{preventable:.2f}','net_avoidable_loss_units':'30.00','expected_damage_returns':f'{events:.2f}','addressable_returns':f'{addressable:.2f}','upper_bound_value_units':f'{value:.2f}','is_chapter_example':'yes' if (orders,rate,preventable)==(20000,.02,.25) else 'no'})
 return rows

def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f'Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}')
if __name__=='__main__':main()
