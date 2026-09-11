"""Figure 22.1: power rises with effect size and sample size."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch22_sample.csv').open()));fig,ax=plt.subplots(figsize=(5.2,3.15));cols=[GREY,BLUE,TEAL,GOLD,RED]
    for d,c in zip((.1,.2,.4,.6,.8),cols):
        z=[x for x in r if float(x['standardized_effect_d'])==d];ax.plot([int(x['sample_size_per_group']) for x in z],[float(x['planned_power']) for x in z],color=c,lw=2,label=f'd={d}')
    ax.axhline(.8,color=NAVY,ls='--',lw=1.4,label='80% planning target');ax.set_ylim(0,1.03);ax.set_xlabel('Sample size per group');ax.set_ylabel('Planned power');ax.set_title('Power depends jointly on effect size and sample size',color=NAVY,weight='bold');ax.grid(color=GREY,alpha=.16);ax.legend(frameon=False,fontsize=6.5,ncol=2);fig.tight_layout();save_figure(fig,'fig-22-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
