"""Figure 14.2: systematic offset and random measurement error."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();rows=list(csv.DictReader((ROOT/'data/generated/ch14_sample.csv').open(encoding='utf-8')));x=np.array([float(r['reference_weight_kg']) for r in rows]);eb=np.array([float(r['biased_signed_error_kg']) for r in rows]);eu=np.array([float(r['unbiased_signed_error_kg']) for r in rows])
    fig,(a,b)=plt.subplots(1,2,figsize=(5.2,3.15),sharey=True)
    for ax,e,c,title in [(a,eb,RED,'Offset + random noise'),(b,eu,TEAL,'Random noise only')]:
        ax.scatter(x,e,s=22,color=c,alpha=.78);ax.axhline(0,color=NAVY,lw=1);ax.axhline(e.mean(),color=GOLD,lw=1.7,ls='--',label=f'mean error {e.mean():+.3f} kg');ax.set_xlabel('Reference weight (kg)');ax.set_title(title,color=NAVY,weight='bold',fontsize=9);ax.grid(color=GREY,alpha=.18);ax.legend(frameon=False,fontsize=6.5)
    a.set_ylabel('Signed error (kg)');fig.suptitle('Bias shifts the centre; random error creates scatter',color=NAVY,weight='bold',fontsize=11);fig.tight_layout();save_figure(fig,'fig-14-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
