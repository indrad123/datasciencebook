"""Generate deterministic linear and logistic prediction examples for Chapter 36."""
import csv,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/"data/generated/ch36_sample.csv"
def build_rows():
 inputs=[(1,0,0,-1.2),(2,0,1,-.8),(3,1,0,-.3),(4,0,0,.1),(5,1,1,.45),(6,0,1,.8),(7,1,0,1.15),(8,1,1,1.5),(9,0,0,1.9),(10,1,1,2.3)];errors=[-1.1,.8,-.5,1.3,-.9,.4,1.1,-.6,.7,-1.2];rows=[]
 for i,((dist,cong,prio,eta),err) in enumerate(zip(inputs,errors),1):
  pred=18+.7*dist+5.2*cong-2.1*prio;prob=1/(1+math.exp(-eta))
  rows.append({"shipment_id":f"S{i:02d}","distance_100km":dist,"port_congestion":cong,"priority":prio,"observed_hours":f"{pred+err:.1f}","predicted_hours":f"{pred:.1f}","residual_hours":f"{err:.1f}","logit_score":f"{eta:.2f}","late_probability":f"{prob:.4f}","alert_at_0_60":1 if prob>=.60 else 0})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
if __name__=="__main__":main()
