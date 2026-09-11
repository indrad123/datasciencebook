"""Figure 26.1: four distinct threats to valid analysis."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,axs=plt.subplots(2,2,figsize=(5.8,3.7));items=[('Missingness','Facility → temperature observed\nFacility → lateness'),('Selection bias','Portal use → inclusion\nPortal use → outcome'),('Confounding','Urgency → premium freight\nUrgency → lateness'),('Leakage','Future exception code\n→ reveals lateness')]
 for ax,(title,text),c in zip(axs.flat,items,[BLUE,GOLD,TEAL,RED]):ax.axis('off');ax.text(.5,.68,title,ha='center',weight='bold',color=NAVY,fontsize=10);ax.text(.5,.35,text,ha='center',va='center',fontsize=8,bbox=dict(boxstyle='round,pad=.6',facecolor=c,alpha=.2,edgecolor=c))
 fig.suptitle('Similar-looking tables can fail for different reasons',color=NAVY,weight='bold');fig.tight_layout();save_figure(fig,'fig-26-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
