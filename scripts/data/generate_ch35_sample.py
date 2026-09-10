"""Generate deterministic threshold metrics for Chapter 35."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/"data/generated/ch35_sample.csv"
def build_rows():
 counts=[("all_negative","",0,0,80,920),("late_model",.30,72,180,8,740),("late_model",.40,68,110,12,810),("late_model",.50,60,90,20,830),("late_model",.60,58,40,22,880),("late_model",.70,50,25,30,895),("late_model",.80,38,10,42,910)]
 rows=[]
 for model,t,tp,fp,fn,tn in counts:
  n=tp+fp+fn+tn;p=tp/(tp+fp) if tp+fp else 0;r=tp/(tp+fn);s=tn/(tn+fp)
  rows.append({"model":model,"threshold":t,"tp":tp,"fp":fp,"fn":fn,"tn":tn,"alerts":tp+fp,"accuracy":f"{(tp+tn)/n:.3f}","precision":f"{p:.3f}","recall":f"{r:.3f}","specificity":f"{s:.3f}","f1":f"{2*p*r/(p+r):.3f}" if p+r else "0.000","balanced_accuracy":f"{(r+s)/2:.3f}","expected_cost_idr":40000*fp+500000*fn,"capacity_feasible":"yes" if tp+fp<=100 and r>=.70 else "no"})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
if __name__=="__main__":main()
