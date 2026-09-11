"""Figure 33.2: expanding validation and untouched final test."""
import csv,sys
from datetime import date
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure

def d(s):return date.fromisoformat(s).toordinal()
def main():
 with (ROOT/"data/generated/ch33_sample.csv").open() as f:rows=list(csv.DictReader(f))
 apply_style();fig,ax=plt.subplots(figsize=(7.2,3.8));y=range(len(rows),0,-1)
 for yy,r in zip(y,rows):
  ax.barh(yy,d(r["train_end"])-d(r["train_start"]),left=d(r["train_start"]),height=.55,color=BLUE)
  ax.barh(yy,d(r["evaluation_start"])-d(r["train_end"]),left=d(r["train_end"]),height=.55,color="white",edgecolor=RED,hatch="///")
  c=RED if r["evaluation_role"]=="test" else GOLD
  ax.barh(yy,d(r["evaluation_end"])-d(r["evaluation_start"])+1,left=d(r["evaluation_start"]),height=.55,color=c)
 ax.set_yticks(list(y),["Fold 1","Fold 2","Fold 3","Fold 4","Final test"]);ticks=[date(2024,1,1),date(2024,7,1),date(2025,1,1),date(2025,7,1),date(2026,1,1)]
 ax.set_xticks([x.toordinal() for x in ticks],[x.strftime("%b\n%Y") for x in ticks]);ax.set_xlabel("Calendar time");ax.set_title("Selection happens before the untouched final test",color=NAVY,weight="bold")
 ax.text(.01,-.22,"Training",transform=ax.transAxes,color=BLUE,weight="bold");ax.text(.19,-.22,"30-day maturity gap",transform=ax.transAxes,color=RED,weight="bold");ax.text(.48,-.22,"Validation",transform=ax.transAxes,color=GOLD,weight="bold");ax.text(.67,-.22,"Final test",transform=ax.transAxes,color=RED,weight="bold")
 fig.tight_layout();save_figure(fig,"fig-33-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
