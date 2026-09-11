"""Figure 13.2: repeated samples produce varying sample means."""
from pathlib import Path
import csv,sys
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style(); rows=list(csv.DictReader((ROOT/'data/generated/ch13_sample.csv').open(encoding='utf-8'))); pop=np.array([float(r['weekly_sales_units']) for r in rows]); frame=np.array([float(r['weekly_sales_units']) for r in rows if r['in_sampling_frame']=='yes']); observed=np.mean([float(r['weekly_sales_units']) for r in rows if r['selected_sample']=='yes'])
    rng=np.random.default_rng(1314);means=np.array([rng.choice(frame,size=50,replace=False).mean() for _ in range(250)])
    bins=np.linspace(means.min()-1,means.max()+1,24);counts,edges=np.histogram(means,bins);xs=[];ys=[]
    for i,count in enumerate(counts):
        centre=(edges[i]+edges[i+1])/2
        xs.extend([centre]*count);ys.extend(range(1,count+1))
    fig,ax=plt.subplots(figsize=(5.2,3.15));ax.scatter(xs,ys,s=14,color=BLUE,alpha=.72,edgecolor='none');ax.axvline(pop.mean(),color=NAVY,lw=2,label=f'population mean {pop.mean():.1f}');ax.axvline(observed,color=RED,lw=1.7,ls='--',label=f'observed sample mean {observed:.1f}')
    ax.set_xlabel('Mean weekly sales from a sample of 50 stores');ax.set_ylabel('Stacked frequency');ax.set_title('Different random samples produce different statistics',color=NAVY,weight='bold');ax.grid(axis='x',color=GREY,alpha=.18);ax.legend(frameon=False,fontsize=7)
    fig.tight_layout();save_figure(fig,'fig-13-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
