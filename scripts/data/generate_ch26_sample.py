"""Generate deterministic missingness and feature-timing data for Chapter 26."""
import csv
from datetime import datetime,timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'data/generated/ch26_sample.csv'
def build_rows():
 rows=[];start=datetime(2025,1,1,8)
 for facility,missing in [('Company',7),('Third-party',38)]:
  for i in range(100):
   dispatch=start+timedelta(hours=len(rows)*3);urgent=i%5==0;premium=urgent or i%7==0;late=(i*3+(facility=='Third-party'))%10 < (4 if urgent else 2);temp='' if i<missing else round(4.2+(i%9)*.25,2)
   rows.append({'shipment_id':f'SHP-{len(rows)+1:03d}','facility_type':facility,'temperature_c':temp,'temperature_missing':'Yes' if temp=='' else 'No','urgent_shipment':'Yes' if urgent else 'No','premium_freight':'Yes' if premium else 'No','late_delivery':'Yes' if late else 'No','dispatch_time':dispatch.isoformat(),'final_exception_code':'LATE' if late else 'NONE','exception_available_time':(dispatch+timedelta(hours=18+i%8)).isoformat()})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f'Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}')
if __name__=='__main__':main()
