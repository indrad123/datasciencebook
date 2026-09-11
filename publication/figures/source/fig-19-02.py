"""Figure 19.2: sampling means narrow and become more regular as n grows."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch19_sample.csv').open()));fig,axes=plt.subplots(1,3,figsize=(5.2,3.15),sharey=True);cols=[BLUE,TEAL,GOLD]
    for ax,n,c in zip(axes,(1,5,30),cols):
        x=np.array([float(z['sample_mean_weekly_units']) for z in r if int(z['sample_size'])==n]);se=float(next(z['theoretical_se_units'] for z in r if int(z['sample_size'])==n));ax.hist(x,bins=28,color=c,edgecolor='white');ax.set_title(f'n={n}\nSE={se:.1f}',color=NAVY,weight='bold',fontsize=8.5);ax.set_xlabel('Sample mean');ax.grid(color=GREY,alpha=.15)
    axes[0].set_ylabel('Replicates');fig.suptitle('Larger samples reduce standard error and smooth skew',color=NAVY,weight='bold',fontsize=10.5);fig.tight_layout();save_figure(fig,'fig-19-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
