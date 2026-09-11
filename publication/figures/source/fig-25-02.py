"""Figure 25.2: A/B effect and guardrails in natural units."""
from pathlib import Path
import csv,math,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def rate(rows,arm,field):
 z=[r for r in rows if r['assignment']==arm];return sum(r[field]=='Yes' for r in z)/len(z)
def main():
 apply_style();r=list(csv.DictReader((ROOT/'data/generated/ch25_sample.csv').open()));metrics=[('Completion','completed_order_7d'),('Corrections','correction_request'),('Support','support_contact')];effects=[];errs=[]
 for _,f in metrics:
  a=rate(r,'Control',f);b=rate(r,'Treatment',f);effects.append((b-a)*100);errs.append(1.96*math.sqrt(a*(1-a)/2000+b*(1-b)/2000)*100)
 fig,ax=plt.subplots(figsize=(5.3,3.15));y=range(3);ax.errorbar(effects,y,xerr=errs,fmt='o',color=BLUE,ecolor=NAVY,capsize=4,ms=7);ax.axvline(0,color=NAVY,lw=1);ax.axvline(2,color=GOLD,ls='--',lw=1.5,label='+2 pp minimum worthwhile completion effect');ax.set_yticks(list(y),[m[0] for m in metrics]);ax.set_xlabel('Treatment minus control (percentage points)');ax.set_title('Primary effect and guardrails belong in one decision',color=NAVY,weight='bold');ax.grid(axis='x',alpha=.18);ax.legend(frameon=False,fontsize=6.5,loc='upper right');fig.tight_layout();save_figure(fig,'fig-25-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
