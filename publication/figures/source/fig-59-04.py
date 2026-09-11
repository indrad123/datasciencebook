"""Figure 59.4: empirical horizon-specific demand uncertainty."""
import csv, sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE, LIGHT_BLUE, NAVY, RED, TEAL, apply_style, save_figure


def main():
    rows=list(csv.DictReader((ROOT/'data/generated/ch59_sample.csv').open())); p=[r for r in rows if r['product_id']=='SAMBAL_250']
    demand=np.array([float(r['latent_demand_cases']) for r in p]); train=demand[:-13]; test=demand[-13:]; point=train[-13:]
    errors=[]
    for origin in range(39,len(train)-13): errors.append(demand[origin+1:origin+14]-demand[origin-12:origin+1])
    errors=np.array(errors); lower=np.maximum(0,point+np.quantile(errors,.10,axis=0)); upper=point+np.quantile(errors,.90,axis=0)
    h=np.arange(1,14); apply_style(); fig,axes=plt.subplots(1,2,figsize=(8,4.35))
    axes[0].fill_between(h,lower,upper,color=LIGHT_BLUE,label='empirical 10–90% band'); axes[0].plot(h,point,color=TEAL,marker='o',label='seasonal point forecast'); axes[0].plot(h,test,color=NAVY,marker='s',label='realized demand')
    axes[0].set(title='Uncertainty changes with horizon',xlabel='Forecast horizon (weeks)',ylabel='Cases',xticks=[1,3,5,7,9,11,13]); axes[0].legend(frameon=False,fontsize=6.3); axes[0].grid(alpha=.15)
    cumulative_errors=np.cumsum(errors,axis=1); q10=np.quantile(cumulative_errors,.10,axis=0); q50=np.quantile(cumulative_errors,.50,axis=0); q90=np.quantile(cumulative_errors,.90,axis=0)
    axes[1].fill_between(h,q10,q90,color=LIGHT_BLUE,label='10–90% cumulative error'); axes[1].plot(h,q50,color=BLUE,label='median cumulative error'); axes[1].axhline(0,color=NAVY,lw=.8)
    axes[1].axvline(2,color=RED,ls='--',lw=1,label='2-week lead time'); axes[1].set(title='Lead-time risk is cumulative',xlabel='Forecast horizon (weeks)',ylabel='Cumulative error (cases)',xticks=[1,2,3,5,7,9,11,13]); axes[1].legend(frameon=False,fontsize=6.3); axes[1].grid(alpha=.15)
    fig.suptitle('A point forecast alone cannot define safety stock',color=NAVY,weight='bold',fontsize=11.5); fig.tight_layout(rect=(0,.01,1,.92)); save_figure(fig,'fig-59-04',ROOT); plt.close(fig)


if __name__=='__main__': main()
