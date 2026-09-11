"""Figure 19.1: one population concept and repeated sample means."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch19_sample.csv').open()));x=np.array([float(z['sample_mean_weekly_units']) for z in r if z['sample_size']=='30']);mu=float(r[0]['population_mean_weekly_units']);fig,(a,b)=plt.subplots(1,2,figsize=(5.2,3.15))
    a.scatter(range(1,31),x[:30],color=BLUE,s=20);a.axhline(mu,color=RED,lw=1.5,label=f'population mean {mu:.1f}');a.set_xlabel('First 30 replicates');a.set_ylabel('Sample mean (units/week)');a.set_title('Every sample mean differs',color=NAVY,weight='bold',fontsize=9);a.legend(frameon=False,fontsize=6.5)
    b.hist(x,bins=25,color=TEAL,edgecolor='white');b.axvline(mu,color=RED,lw=1.8,label='population mean');b.axvline(x.mean(),color=GOLD,ls='--',lw=1.8,label=f'mean of means {x.mean():.1f}');b.set_xlabel('Mean of 30 stores');b.set_ylabel('Replicates');b.set_title('The distribution stays centred',color=NAVY,weight='bold',fontsize=9);b.legend(frameon=False,fontsize=6.5)
    for ax in (a,b):ax.grid(color=GREY,alpha=.16)
    fig.suptitle('Repeated samples create a distribution of estimates',color=NAVY,weight='bold',fontsize=10.5);fig.tight_layout();save_figure(fig,'fig-19-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
