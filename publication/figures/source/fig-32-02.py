"""Figure 32.2: raw inputs become purposeful feature groups."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(6.1,3.6));ax.axis("off")
 groups=[("NUMERIC","price per carton\nratios • logs",BLUE),("CATEGORICAL","warehouse indicators\nunseen → OTHER",TEAL),("TEMPORAL","week sine/cosine\nholiday distance",GOLD),("HISTORICAL","lag 1 • lag 52\ntrailing means",RED)]
 for i,(h,b,c) in enumerate(groups):
  x=.06+i*.235;ax.text(x+.095,.63,h,ha="center",weight="bold",color=c,fontsize=8);ax.text(x+.095,.45,b,ha="center",va="center",color=NAVY,fontsize=7.5,bbox=dict(boxstyle="round,pad=.65",fc="white",ec=c,lw=2))
 ax.text(.5,.9,"Engineer representations with a business mechanism",ha="center",color=NAVY,weight="bold",fontsize=12);ax.text(.5,.18,"Fit learned state on training data • apply unchanged later • monitor availability and stability",ha="center",color=NAVY,fontsize=7.5)
 fig.tight_layout();save_figure(fig,"fig-32-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
