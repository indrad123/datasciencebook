"""Figure 13.1: population, frame, sample, and observation."""
from pathlib import Path
import csv,sys
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style(); rows=list(csv.DictReader((ROOT/'data/generated/ch13_sample.csv').open(encoding='utf-8'))); frame=sum(r['in_sampling_frame']=='yes' for r in rows); sample=sum(r['selected_sample']=='yes' for r in rows)
    fig,ax=plt.subplots(figsize=(5.2,3.15));ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis('off')
    for xy,r,c,label in [((3.8,3),2.65,BLUE,'Target population\n400 stores'),((3.8,3),2.18,TEAL,f'Sampling frame\n{frame} stores'),((3.8,3),1.12,GOLD,f'Sample\n{sample} stores')]:
        ax.add_patch(Circle(xy,r,facecolor=c,alpha=.18,edgecolor=c,lw=2));ax.text(3.8,3+r-.3,label,ha='center',va='top',color=NAVY,weight='bold',fontsize=8)
    ax.scatter([3.8],[3],s=90,color=RED,zorder=5);ax.annotate('One observation\n= one store row',(3.8,3),xytext=(7.2,3.5),arrowprops=dict(arrowstyle='->',color=NAVY),color=NAVY,fontsize=8,weight='bold')
    ax.annotate('16 target stores absent\nfrom the operational frame',(1.5,1.2),xytext=(6.4,.8),arrowprops=dict(arrowstyle='->',color=RED),color=RED,fontsize=7)
    ax.set_title('Population, frame, sample, and observation are different sets',color=NAVY,weight='bold')
    fig.tight_layout();save_figure(fig,'fig-13-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
