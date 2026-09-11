"""Figure 25.1: randomized assignment preserves the analysis path."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(5.6,3.15));ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis('off');boxes=[(3.2,5,'4,000 eligible accounts',NAVY),(1.2,3.2,'Control\n2,000 assigned',BLUE),(5.2,3.2,'Treatment\n2,000 assigned',TEAL),(1.2,1.25,'620 completed\n+ guardrails',GOLD),(5.2,1.25,'680 completed\n+ guardrails',RED)]
 for x,y,t,c in boxes:ax.add_patch(FancyBboxPatch((x,y-.48),2.8,.96,boxstyle='round,pad=.06',facecolor=c,edgecolor='none',alpha=.92));ax.text(x+1.4,y,t,ha='center',va='center',color='white',weight='bold',fontsize=8)
 for a,b in [((4.6,4.52),(2.6,3.68)),((4.6,4.52),(6.6,3.68)),((2.6,2.72),(2.6,1.73)),((6.6,2.72),(6.6,1.73))]:ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color=NAVY,lw=1.3))
 ax.text(5,4.15,'blocked random assignment',ha='center',color=NAVY,fontsize=7);ax.set_title('Assignment, measurement, and analysis use the same unit',color=NAVY,weight='bold');fig.tight_layout();save_figure(fig,'fig-25-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
