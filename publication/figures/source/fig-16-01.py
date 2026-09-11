"""Figure 16.1: distribution with centre and quantile landmarks."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();x=np.array([float(r['delivery_days']) for r in csv.DictReader((ROOT/'data/generated/ch16_sample.csv').open())]);q1,med,q3=np.quantile(x,[.25,.5,.75],method='linear');mean=x.mean()
    fig,ax=plt.subplots(figsize=(5.2,3.15));bins=np.arange(0,20,1);ax.hist(x,bins=bins,color=BLUE,alpha=.82,edgecolor='white')
    for v,c,label,ls in [(q1,TEAL,f'Q1 {q1:.1f}',':'),(med,GOLD,f'Median {med:.1f}','--'),(q3,TEAL,f'Q3 {q3:.1f}',':'),(mean,RED,f'Mean {mean:.1f}','-')]:ax.axvline(v,color=c,lw=1.8,ls=ls,label=label)
    ax.set_xlabel('Delivery time (days)');ax.set_ylabel('Shipments');ax.set_title('A slow tail pulls the mean above the median',color=NAVY,weight='bold');ax.grid(color=GREY,alpha=.16);ax.legend(frameon=False,fontsize=7,ncol=2);fig.tight_layout();save_figure(fig,'fig-16-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
