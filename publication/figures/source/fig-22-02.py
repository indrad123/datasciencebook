"""Figure 22.2: detectability and practical importance at a fixed sample size."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=[x for x in csv.DictReader((ROOT/'data/generated/ch22_sample.csv').open()) if x['sample_size_per_group']=='80'];x=[float(z['effect_delivery_days']) for z in r];y=[float(z['planned_power']) for z in r];fig,ax=plt.subplots(figsize=(5.2,3.15));ax.plot(x,y,color=BLUE,lw=2,marker='o');ax.axvline(1,color=GOLD,ls='--',lw=2,label='minimum worthwhile = 1 day');ax.axhline(.8,color=RED,ls=':',lw=2,label='power target = 80%');
    for a,b,z in zip(x,y,r):ax.annotate(f"d={z['standardized_effect_d']}",(a,b),xytext=(3,5),textcoords='offset points',fontsize=6.5,color=NAVY)
    ax.set_xlim(0,3.4);ax.set_ylim(0,1.03);ax.set_xlabel('Planned effect (delivery days)');ax.set_ylabel('Planned power');ax.set_title('Detectable does not automatically mean worthwhile',color=NAVY,weight='bold');ax.grid(color=GREY,alpha=.16);ax.legend(frameon=False,fontsize=7);fig.tight_layout();save_figure(fig,'fig-22-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
