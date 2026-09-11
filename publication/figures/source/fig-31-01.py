"""Figure 31.1: reproducible cleaning pipeline."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(6.3,3.3));ax.axis("off")
 stages=[("RAW","Read-only\nhashed snapshot",NAVY),("VALIDATE","Schema +\nrequired fields",RED),("STANDARDISE","Keys + controlled\ncategories",BLUE),("PARSE","Quantity + dates\nwith status",GOLD),("RESOLVE","Latest valid\nrevision",TEAL),("PUBLISH","Quality-gated\nversion + hash",NAVY)]
 for i,(h,b,c) in enumerate(stages):
  x=.03+i*.16;ax.text(x+.065,.58,h,ha="center",weight="bold",color=c,fontsize=7.5);ax.text(x+.065,.43,b,ha="center",va="center",fontsize=6.8,color=NAVY,bbox=dict(boxstyle="round,pad=.45",fc="white",ec=c,lw=1.7))
  if i<5:ax.annotate("",xy=(x+.155,.43),xytext=(x+.135,.43),arrowprops=dict(arrowstyle="->",color=NAVY,lw=1.2))
 ax.text(.5,.91,"Raw evidence becomes a reproducible analysis table",ha="center",color=NAVY,weight="bold",fontsize=12)
 ax.text(.5,.12,"Each stage is ordered, deterministic, tested, observable, and regenerable",ha="center",color=NAVY,fontsize=8)
 fig.tight_layout();save_figure(fig,"fig-31-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
