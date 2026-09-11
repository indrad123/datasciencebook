"""Figure 17.2: an IQR flag starts review rather than deleting data."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();rows=[r for r in csv.DictReader((ROOT/'data/generated/ch17_sample.csv').open()) if r['scenario']=='Routine plus disruption'];x=np.array([float(r['delivery_days']) for r in rows]);q1,q3=np.quantile(x,[.25,.75],method='linear');fence=q3+1.5*(q3-q1)
    fig,ax=plt.subplots(figsize=(5.2,3.15));y=np.ones(len(x));ax.scatter(x,y,color=BLUE,s=22,alpha=.65);flags=x>fence;ax.scatter(x[flags],y[flags],color=RED,s=55,label='IQR-screened for review',zorder=3);ax.axvline(fence,color=GOLD,ls='--',lw=2,label=f'upper fence {fence:.1f} days');ax.annotate('18-day verified disruption\nretained with context',(18,1),xytext=(12.2,1.16),fontsize=7,color=NAVY,arrowprops=dict(arrowstyle='->',color=RED));ax.set_yticks([]);ax.set_ylim(.82,1.28);ax.set_xlim(0,19);ax.set_xlabel('Delivery time (days)');ax.set_title('A statistical flag is a question, not a deletion rule',color=NAVY,weight='bold');ax.grid(axis='x',color=GREY,alpha=.18);ax.legend(frameon=False,fontsize=7,loc='lower right');fig.tight_layout();save_figure(fig,'fig-17-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
