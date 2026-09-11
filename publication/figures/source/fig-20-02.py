"""Figure 20.2: repeated confidence intervals and long-run coverage."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch20_sample.csv').open()));shown=r[:40];fig,ax=plt.subplots(figsize=(5.2,3.6))
    for i,z in enumerate(shown,1):
        cover=z['covers_population_mean']=='Yes';c=TEAL if cover else RED;ax.hlines(i,float(z['ci_lower_units']),float(z['ci_upper_units']),color=c,lw=1.8);ax.scatter(float(z['sample_mean_weekly_units']),i,color=c,s=10)
    ax.axvline(1000,color=NAVY,ls='--',lw=1.5,label='fixed population mean');coverage=sum(z['covers_population_mean']=='Yes' for z in r)/len(r);ax.set_xlabel('Weekly units');ax.set_ylabel('Replicate');ax.set_title(f'Repeated intervals vary; observed coverage = {coverage:.1%}',color=NAVY,weight='bold');ax.grid(axis='x',color=GREY,alpha=.16);ax.legend(frameon=False,fontsize=7);fig.tight_layout();save_figure(fig,'fig-20-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
