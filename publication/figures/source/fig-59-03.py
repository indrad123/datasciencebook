"""Figure 59.3: consistent holdout comparison of three baselines."""
import csv, sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT)); sys.path.insert(0,str(ROOT/'src'))
from datasciencebook.inventory_planning import wape
from publication.figure_style import BLUE, GOLD, NAVY, TEAL, apply_style, save_figure


def main():
    rows=list(csv.DictReader((ROOT/'data/generated/ch59_sample.csv').open())); products=['SAMBAL_250','KOPI_200','TEH_20']; metrics=[]
    for product in products:
        p=[r for r in rows if r['product_id']==product and r['data_split']=='holdout']; a=[float(r['latent_demand_cases']) for r in p]
        metrics.append([wape(a,[float(r[k]) for r in p]) for k in ['last_observation_forecast_cases','seasonal_naive_forecast_cases','drift_forecast_cases']])
    metrics=np.array(metrics); apply_style(); fig,axes=plt.subplots(1,2,figsize=(8,4.4),gridspec_kw={'width_ratios':[1.05,1.45]})
    x=np.arange(3); width=.23; colors=[BLUE,TEAL,GOLD]
    for i,(name,color) in enumerate(zip(['Last observation','Seasonal naive','Drift'],colors)):
        axes[0].bar(x+(i-1)*width,100*metrics[:,i],width,label=name,color=color)
    axes[0].set(xticks=x,xticklabels=['Sambal','Kopi','Teh'],ylabel='Holdout WAPE (%)',title='One protocol for every model'); axes[0].legend(frameon=False,fontsize=6.5); axes[0].grid(axis='y',alpha=.15)
    p=[r for r in rows if r['product_id']=='SAMBAL_250' and r['data_split']=='holdout']; h=np.arange(1,14); actual=[float(r['latent_demand_cases']) for r in p]
    axes[1].plot(h,actual,color=NAVY,marker='o',label='actual demand')
    for key,name,color,style in [('last_observation_forecast_cases','last',BLUE,':'),('seasonal_naive_forecast_cases','seasonal naive',TEAL,'-'),('drift_forecast_cases','drift',GOLD,'--')]: axes[1].plot(h,[float(r[key]) for r in p],color=color,ls=style,marker='.',label=name)
    axes[1].set(xlabel='Forecast horizon (weeks)',ylabel='Cases',title='Sambal final 13-week holdout',xticks=[1,3,5,7,9,11,13]); axes[1].legend(frameon=False,fontsize=6.4); axes[1].grid(alpha=.15)
    fig.suptitle('Seasonal naive is selected only after an honest chronological comparison',color=NAVY,weight='bold',fontsize=11.5)
    fig.tight_layout(rect=(0,.01,1,.92)); save_figure(fig,'fig-59-03',ROOT); plt.close(fig)


if __name__=='__main__': main()
