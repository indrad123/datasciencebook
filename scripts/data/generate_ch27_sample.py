"""Generate deterministic baseline and learned-model examples for Chapter 27."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'data/generated/ch27_sample.csv'
def build_rows():
 rows=[]
 for i,y in enumerate((100,110,90,120),1):rows.append({'task':'demand','observation_id':f'D-{i}','split':'train','feature_value':'','actual_value':y,'baseline_prediction':'','learned_prediction':'','absolute_error_baseline':'','absolute_error_learned':''})
 for i,(y,p) in enumerate(((108,107),(130,124)),5):rows.append({'task':'demand','observation_id':f'D-{i}','split':'test','feature_value':'','actual_value':y,'baseline_prediction':105,'learned_prediction':p,'absolute_error_baseline':abs(y-105),'absolute_error_learned':abs(y-p)})
 for i,x in enumerate(range(12,32,2),1):
  y=round(7+1.18*x+(-2,1,0,2,-1)[(i-1)%5],2);split='train' if i<=7 else 'test';base=round(sum(7+1.18*z+(-2,1,0,2,-1)[j%5] for j,z in enumerate(range(12,26,2)))/7,2);pred=round(7+1.18*x,2)
  rows.append({'task':'transit','observation_id':f'T-{i:02d}','split':split,'feature_value':x,'actual_value':y,'baseline_prediction':base if split=='test' else '','learned_prediction':pred if split=='test' else '','absolute_error_baseline':round(abs(y-base),2) if split=='test' else '','absolute_error_learned':round(abs(y-pred),2) if split=='test' else ''})
 return rows
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f'Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}')
if __name__=='__main__':main()
