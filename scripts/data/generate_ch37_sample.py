"""Generate deterministic tree-model comparison data for Chapter 37."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/"data/generated/ch37_sample.csv"
def build_rows():
 models=[("current_rule","fixed business thresholds","rule",18400000,.65,.48,92,1,"no"),("logistic","weighted linear predictor","regularised",15100000,.71,.55,96,3,"no"),("decision_tree","recursive feature splits","depth 3",14800000,.73,.56,99,2,"no"),("random_forest","bootstrap trees plus feature sampling","300 trees",13200000,.76,.61,98,24,"yes"),("gradient_boosting","sequential residual correction","180 trees; rate 0.04",12900000,.77,.62,99,31,"candidate")]
 return [{"model":m,"construction":c,"complexity_control":k,"validation_cost_idr":cost,"recall":f"{r:.2f}","precision":f"{p:.2f}","alerts_per_day":a,"latency_ms":lat,"selection_status":s} for m,c,k,cost,r,p,a,lat,s in models]
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
if __name__=="__main__":main()
