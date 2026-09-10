"""Generate deterministic leakage-safe weekly features for Chapter 32."""
import csv,math
from datetime import date,timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/"data/generated/ch32_sample.csv"
def build_rows():
 demand=[920,970,945,1010,1040,990,1080,1120,1095,1170,1210,1160,1240,1300,1275,1360];rows=[]
 for i,y in enumerate(demand):
  week=i+1;promo=1 if week in (4,8,12,16) else 0;discount=10 if promo else 0
  rows.append({"forecast_week":(date(2026,1,5)+timedelta(weeks=i)).isoformat(),"product":"instant_noodles","warehouse":"Jakarta","demand_cartons":y,"promotion_planned":promo,"discount_pct":discount,"promotion_discount_interaction":promo*discount,"week_sin":f"{math.sin(2*math.pi*week/52):.6f}","demand_lag_1w":demand[i-1] if i>=1 else "","demand_mean_4w":f"{sum(demand[i-4:i])/4:.2f}" if i>=4 else ""})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
if __name__=="__main__":main()
