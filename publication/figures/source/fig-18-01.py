"""Figure 18.1: probability mass versus probability density."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,TEAL,apply_style,save_figure
def main():
    apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch18_sample.csv').open()));fig,(a,b)=plt.subplots(1,2,figsize=(5.2,3.15))
    d=[z for z in r if z['distribution']=='Binomial'];a.bar([float(z['x']) for z in d],[float(z['mass_or_density']) for z in d],color=BLUE);a.set_xlabel('Late shipments out of 10');a.set_ylabel('Probability mass');a.set_title('Discrete: mass at outcomes',color=NAVY,weight='bold',fontsize=9)
    d=[z for z in r if z['distribution']=='Normal'];x=[float(z['x']) for z in d];y=[float(z['mass_or_density']) for z in d];b.plot(x,y,color=TEAL,lw=2);b.fill_between(x,y,color=GOLD,alpha=.3);b.set_xlabel('Fill weight (g)');b.set_ylabel('Probability density');b.set_title('Continuous: area over intervals',color=NAVY,weight='bold',fontsize=9)
    for ax in (a,b):ax.grid(color=GREY,alpha=.16)
    fig.suptitle('Discrete mass and continuous density are not interchangeable',color=NAVY,weight='bold',fontsize=10.5);fig.tight_layout();save_figure(fig,'fig-18-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
