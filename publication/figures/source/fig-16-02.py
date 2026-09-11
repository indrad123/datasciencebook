"""Figure 16.2: annotated five-number summary and box plot."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();x=np.array([float(r['delivery_days']) for r in csv.DictReader((ROOT/'data/generated/ch16_sample.csv').open())]);vals=np.quantile(x,[0,.25,.5,.75,1],method='linear');names=['Minimum','Q1','Median','Q3','Maximum']
    fig,ax=plt.subplots(figsize=(5.2,3.15));ax.boxplot(x,vert=False,widths=.36,whis=(0,100),showfliers=False,patch_artist=True,boxprops=dict(facecolor=BLUE,alpha=.55),medianprops=dict(color=GOLD,lw=2),whiskerprops=dict(color=NAVY),capprops=dict(color=NAVY))
    for i,(v,n) in enumerate(zip(vals,names)):ax.scatter(v,1,color=RED if n in ('Minimum','Maximum') else TEAL,zorder=3,s=24);ax.annotate(f'{n}\n{v:.1f}',(v,1),xytext=(0,28 if i%2==0 else -36),textcoords='offset points',ha='center',fontsize=7,color=NAVY,arrowprops=dict(arrowstyle='-',color=GREY))
    ax.set_yticks([]);ax.set_xlabel('Delivery time (days)');ax.set_xlim(0,19);ax.set_title('Five landmarks retain centre, middle spread, and full range',color=NAVY,weight='bold');ax.grid(axis='x',color=GREY,alpha=.18);fig.tight_layout();save_figure(fig,'fig-16-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
