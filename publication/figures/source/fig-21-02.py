"""Figure 21.2: statistical evidence and practical importance are separate axes."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();rows=list(csv.DictReader((ROOT/'data/generated/ch21_sample.csv').open()));summary={r['scenario']:r for r in rows};fig,ax=plt.subplots(figsize=(5.2,3.4));ax.set_xlim(-.5,1.5);ax.set_ylim(-.5,1.5);ax.axvline(.5,color='white',lw=3);ax.axhline(.5,color='white',lw=3);ax.add_patch(plt.Rectangle((-.5,-.5),1,1,color=GREY,alpha=.18));ax.add_patch(plt.Rectangle((.5,-.5),1,1,color=GOLD,alpha=.24));ax.add_patch(plt.Rectangle((-.5,.5),1,1,color=BLUE,alpha=.18));ax.add_patch(plt.Rectangle((.5,.5),1,1,color=TEAL,alpha=.24))
    places={'Uncertain small effect':(0,0),'Uncertain meaningful effect':(1,0),'Precise small effect':(0,1),'Precise meaningful effect':(1,1)}
    for name,(x,y) in places.items():r=summary[name];ax.text(x,y,f"{name}\neffect={float(r['observed_effect_units']):.1f}, p={float(r['simulated_two_sided_p_value']):.3f}",ha='center',va='center',fontsize=7.5,color=NAVY,weight='bold')
    ax.set_xticks([0,1],['Below practical\nthreshold','Meets practical\nthreshold']);ax.set_yticks([0,1],['Weak statistical\nevidence','Strong statistical\nevidence']);ax.set_title('Statistical evidence and practical importance answer different questions',color=NAVY,weight='bold',fontsize=10);fig.tight_layout();save_figure(fig,'fig-21-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
