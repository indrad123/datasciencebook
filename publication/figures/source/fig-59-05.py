"""Figure 59.5: understock, overstock, and service-cost sensitivity."""
import csv, sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT)); sys.path.insert(0,str(ROOT/'src'))
from datasciencebook.inventory_planning import lead_time_target, newsvendor_cost
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    rows=list(csv.DictReader((ROOT/'data/generated/ch59_sample.csv').open())); p=[r for r in rows if r['product_id']=='SAMBAL_250']; d=np.array([float(r['latent_demand_cases']) for r in p]); train=d[:-13]; forecast=train[-13:][:2]
    errors=np.array([np.sum(train[e:e+2]-np.resize(train[e-13:e],2)) for e in range(39,len(train)-2,2)]); scenarios=forecast.sum()+errors
    levels=np.arange(.50,.99,.05); targets=np.array([lead_time_target(forecast,errors,x)['target'] for x in levels]); hold=[]; shortage=[]
    for target in targets:
        hold.append(np.mean(np.maximum(target-scenarios,0))); shortage.append(4*np.mean(np.maximum(scenarios-target,0)))
    hold=np.array(hold); shortage=np.array(shortage); total=hold+shortage; best=int(np.argmin(total))
    apply_style(); fig,axes=plt.subplots(1,2,figsize=(8,4.35))
    axes[0].plot(targets,hold,color=BLUE,marker='o',label='overstock cost (1×)'); axes[0].plot(targets,shortage,color=RED,marker='o',label='shortage cost (4×)'); axes[0].plot(targets,total,color=TEAL,marker='s',lw=2,label='total expected cost')
    axes[0].scatter(targets[best],total[best],s=90,color=GOLD,edgecolor=NAVY,zorder=5,label='minimum in scenarios'); axes[0].set(title='Asymmetric consequences shift the target',xlabel='Order-up-to target (cases)',ylabel='Mean scenario cost (kIDR)'); axes[0].legend(frameon=False,fontsize=6.2); axes[0].grid(alpha=.15)
    service=[np.mean(scenarios<=t) for t in targets]; axes[1].plot(100*levels,total,color=TEAL,marker='o',label='expected cost'); ax2=axes[1].twinx(); ax2.plot(100*levels,100*np.array(service),color=GOLD,marker='s',label='empirical service')
    axes[1].axvline(90,color=NAVY,ls='--',lw=1); axes[1].set(title='Policy needs cost and service evidence',xlabel='Planning quantile (%)',ylabel='Mean scenario cost (kIDR)'); ax2.set(ylabel='Scenarios fully covered (%)',ylim=(40,105)); axes[1].grid(alpha=.15)
    lines=axes[1].lines[:1]+ax2.lines; axes[1].legend(lines,[x.get_label() for x in lines],frameon=False,fontsize=6.3,loc='center left')
    fig.suptitle('The lowest estimated cost does not erase service commitments',color=NAVY,weight='bold',fontsize=11.5); fig.tight_layout(rect=(0,.01,1,.92)); save_figure(fig,'fig-59-05',ROOT); plt.close(fig)


if __name__=='__main__': main()
