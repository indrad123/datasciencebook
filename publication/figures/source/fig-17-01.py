"""Figure 17.1: symmetry, right skew, and a distant tail event."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();rows=list(csv.DictReader((ROOT/'data/generated/ch17_sample.csv').open()));names=['Symmetric routine','Right-skewed waiting','Routine plus disruption'];cols=[BLUE,TEAL,GOLD]
    fig,axes=plt.subplots(1,3,figsize=(5.2,3.15),sharey=True)
    for ax,name,c in zip(axes,names,cols):
        x=np.array([float(r['delivery_days']) for r in rows if r['scenario']==name]);ax.hist(x,bins=np.arange(0,20,1),color=c,edgecolor='white');ax.axvline(np.median(x),color=NAVY,ls='--',lw=1.4,label=f'median {np.median(x):.1f}');ax.axvline(x.mean(),color=RED,lw=1.4,label=f'mean {x.mean():.1f}');ax.set_title(name.replace(' ','\n',1),fontsize=8,color=NAVY,weight='bold');ax.set_xlabel('Days');ax.grid(color=GREY,alpha=.15);ax.legend(frameon=False,fontsize=5.8)
    axes[0].set_ylabel('Observations');fig.suptitle('Similar centres can conceal different tails',color=NAVY,weight='bold',fontsize=11);fig.tight_layout();save_figure(fig,'fig-17-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
