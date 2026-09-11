"""Figure 24.2: mean and rank-oriented group comparisons."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch24_sample.csv').open()));shifts=['Morning','Evening','Night'];colors=[TEAL,GOLD,RED];fig,axs=plt.subplots(1,2,figsize=(6.2,2.85))
 vals=[[float(x['picking_minutes']) for x in r if x['shift']==s] for s in shifts];bp=axs[0].boxplot(vals,tick_labels=shifts,patch_artist=True,medianprops={'color':NAVY,'lw':1.5})
 for p,c in zip(bp['boxes'],colors):p.set_facecolor(c);p.set_alpha(.55)
 axs[0].scatter(range(1,4),[sum(v)/len(v) for v in vals],marker='D',color=NAVY,s=22,label='Mean');axs[0].set(title='Continuous outcome: compare means',ylabel='Picking minutes');axs[0].legend(frameon=False,fontsize=6)
 cats=range(1,6);bottom=[0,0,0]
 for rating in cats:
  pct=[sum(int(x['distributor_rating'])==rating for x in r if x['shift']==s)/30 for s in shifts];axs[1].bar(shifts,pct,bottom=bottom,label=str(rating),alpha=.85);bottom=[a+b for a,b in zip(bottom,pct)]
 axs[1].set(title='Ordinal outcome: retain categories',ylabel='Share of shipments',ylim=(0,1));axs[1].legend(title='Rating',frameon=False,fontsize=5.5,title_fontsize=6,ncol=5,loc='upper center')
 fig.suptitle('The outcome scale changes the comparison',color=NAVY,weight='bold');fig.tight_layout();save_figure(fig,'fig-24-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
