"""Figure 20.1: estimate, margin of error, and interval anatomy."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch20_sample.csv').open()))[0];m=float(r['sample_mean_weekly_units']);lo=float(r['ci_lower_units']);hi=float(r['ci_upper_units']);mu=float(r['population_mean_weekly_units'])
    fig,ax=plt.subplots(figsize=(5.2,3.15));ax.hlines(1,lo,hi,color=BLUE,lw=5);ax.scatter([lo,hi],[1,1],color=BLUE,s=45);ax.scatter(m,1,color=GOLD,s=85,zorder=3,label=f'estimate {m:.1f}');ax.axvline(mu,color=RED,ls='--',lw=1.8,label='population mean 1000');ax.annotate(f'lower {lo:.1f}',(lo,1),xytext=(0,-38),textcoords='offset points',ha='center',fontsize=8,color=NAVY);ax.annotate(f'upper {hi:.1f}',(hi,1),xytext=(0,-38),textcoords='offset points',ha='center',fontsize=8,color=NAVY);ax.set_yticks([]);ax.set_ylim(.78,1.25);ax.set_xlabel('Weekly units');ax.set_title('Estimate plus or minus margin of error forms the interval',color=NAVY,weight='bold');ax.grid(axis='x',color=GREY,alpha=.18);ax.legend(frameon=False,fontsize=7);fig.tight_layout();save_figure(fig,'fig-20-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
