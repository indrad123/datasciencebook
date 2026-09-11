"""Figure 33.1: split strategy must match deployment structure."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure

def main():
 apply_style();fig,axs=plt.subplots(1,3,figsize=(7.2,3.25));titles=["RANDOM ROWS","GROUPED","TEMPORAL"]
 for ax,title in zip(axs,titles):ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis("off");ax.set_title(title,color=NAVY,weight="bold",fontsize=10)
 # random: related rows can cross the boundary
 for i in range(5):
  for j in range(3):axs[0].scatter(i*1.8+1,j+1.5,s=70,color=[BLUE,TEAL,GOLD][(i+j)%3],marker="s")
 axs[0].text(5,.45,"Useful only when rows\nare exchangeable",ha="center",fontsize=7,color=NAVY)
 # grouped: each order stays in one fold
 for i,(name,c) in enumerate([("ORDER A",BLUE),("ORDER B",TEAL),("ORDER C",GOLD)]):
  axs[1].text(5,4.7-i*1.35,name,ha="center",fontsize=8,color=NAVY,bbox=dict(boxstyle="round,pad=.45",fc="white",ec=c,lw=2))
 axs[1].text(5,.45,"Keeps dependent rows\ntogether",ha="center",fontsize=7,color=NAVY)
 # time: train always precedes evaluation
 axs[2].arrow(.8,3,8,0,width=.04,head_width=.25,head_length=.35,color=NAVY,length_includes_head=True)
 axs[2].barh(3,5,left=1,height=.8,color=BLUE);axs[2].barh(3,2,left=6.5,height=.8,color=GOLD)
 axs[2].text(3.5,3,"TRAIN",ha="center",va="center",color="white",weight="bold",fontsize=8);axs[2].text(7.5,3,"VALIDATE",ha="center",va="center",color=NAVY,weight="bold",fontsize=6)
 axs[2].text(5,.45,"Mirrors prediction of\nfuture shipments",ha="center",fontsize=7,color=NAVY)
 fig.suptitle("Choose a split that represents the unseen case",color=NAVY,weight="bold",fontsize=13);fig.tight_layout(rect=(0,0,1,.9));save_figure(fig,"fig-33-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
