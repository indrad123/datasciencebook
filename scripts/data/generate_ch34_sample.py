"""Generate deterministic validation- and learning-curve data for Chapter 34."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/"data/generated/ch34_sample.csv"
def build_rows():
 rows=[]
 for degree,tr,va,label in [(1,520,560,"underfit"),(3,210,240,"stable candidate"),(6,90,230,"flexible candidate"),(12,5,480,"overfit")]:
  rows.append({"curve":"validation","scenario":"polynomial_degree","setting":degree,"training_rows":10240,"training_mse":tr,"validation_mse":va,"generalisation_gap":va-tr,"diagnosis":label})
 learning={"high_bias":[(500,610,650),(1000,590,625),(2000,575,605),(4000,565,590),(8000,560,578),(12000,558,572)],"high_variance":[(500,75,510),(1000,82,420),(2000,91,340),(4000,105,275),(8000,122,225),(12000,135,205)]}
 for scenario,values in learning.items():
  for n,tr,va in values:rows.append({"curve":"learning","scenario":scenario,"setting":"","training_rows":n,"training_mse":tr,"validation_mse":va,"generalisation_gap":va-tr,"diagnosis":"poor plateau" if scenario=="high_bias" else "gap narrows with data"})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
if __name__=="__main__":main()
