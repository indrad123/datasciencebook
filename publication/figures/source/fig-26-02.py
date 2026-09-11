"""Figure 26.2: prediction time separates valid and leaked features."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(5.7,3.0));ax.set_xlim(0,24);ax.set_ylim(0,4);ax.axvline(6,color=NAVY,lw=2);ax.text(6,3.55,'Prediction: dispatch',ha='center',color=NAVY,weight='bold');ax.arrow(.8,2.8,21.5,0,head_width=.12,head_length=.5,color=NAVY,length_includes_head=True)
 events=[(1,'Urgency',TEAL),(3,'Facility',TEAL),(5,'Temperature',TEAL),(18,'Final exception',RED),(22,'Arrival status',RED)]
 for x,t,c in events:ax.scatter(x,2.8,s=55,color=c,zorder=3);ax.text(x,2.35,t,ha='center',fontsize=7,rotation=18)
 ax.text(2.8,.9,'VALID\navailable before decision',ha='center',color=TEAL,weight='bold');ax.text(17,.9,'LEAKED\nrecorded after decision',ha='center',color=RED,weight='bold');ax.set_xlabel('Hours along shipment journey');ax.set_yticks([]);ax.set_title('Feature availability—not table location—defines leakage',color=NAVY,weight='bold');fig.tight_layout();save_figure(fig,'fig-26-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
