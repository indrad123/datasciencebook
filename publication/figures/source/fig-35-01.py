"""Figure 35.1: confusion counts connect metrics to consequences."""
import csv,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch35_sample.csv").open() as f:r=next(x for x in csv.DictReader(f) if x["threshold"]=="0.5")
 vals=[[int(r["tp"]),int(r["fn"])],[int(r["fp"]),int(r["tn"])]];labs=[["TRUE POSITIVE\nLate + alert","FALSE NEGATIVE\nLate + no alert"],["FALSE POSITIVE\nOn time + alert","TRUE NEGATIVE\nOn time + no alert"]];cols=[[TEAL,RED],[GOLD,BLUE]]
 apply_style();fig,ax=plt.subplots(figsize=(6.2,4));ax.set_xlim(0,2);ax.set_ylim(0,2);ax.axis("off")
 for i in range(2):
  for j in range(2):
   y=1-i;ax.add_patch(plt.Rectangle((j,y),.96,.92,facecolor=cols[i][j],alpha=.9));ax.text(j+.48,y+.57,str(vals[i][j]),ha="center",va="center",fontsize=23,weight="bold",color="white");ax.text(j+.48,y+.22,labs[i][j],ha="center",va="center",fontsize=8,color="white",weight="bold")
 ax.text(1,-.18,"PREDICTED: ALERT                         PREDICTED: NO ALERT",ha="center",fontsize=8,color=NAVY,weight="bold");ax.text(-.16,1.5,"ACTUAL\nLATE",ha="center",va="center",fontsize=8,color=NAVY,weight="bold");ax.text(-.16,.5,"ACTUAL\nON TIME",ha="center",va="center",fontsize=8,color=NAVY,weight="bold");ax.set_title("Counts reveal the errors hidden by accuracy",color=NAVY,weight="bold");fig.tight_layout();save_figure(fig,"fig-35-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
