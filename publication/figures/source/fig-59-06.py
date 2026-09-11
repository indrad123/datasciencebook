"""Figure 59.6: forecast, inventory action, ownership, and approval dashboard."""
import csv, sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE, GOLD, LIGHT_BLUE, LIGHT_GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    rows=list(csv.DictReader((ROOT/'data/generated/ch59_sample.csv').open())); products=['SAMBAL_250','KOPI_200','TEH_20']; labels=['Sambal 250','Kopi 200','Teh 20']; first=[]
    for product in products: first.append(next(r for r in rows if r['product_id']==product and r['data_split']=='holdout'))
    point=np.array([float(r['lead_time_point_demand_cases']) for r in first]); safety=np.array([float(r['safety_stock_cases']) for r in first]); position=np.array([float(r['inventory_position_cases']) for r in first]); order=np.array([float(r['recommended_order_cases']) for r in first])
    apply_style(); fig,axes=plt.subplots(2,2,figsize=(8,5.8),gridspec_kw={'height_ratios':[1.15,.85]}); x=np.arange(3)
    axes[0,0].bar(x,point,color=BLUE,label='2-week point demand'); axes[0,0].bar(x,safety,bottom=point,color=GOLD,label='90% error buffer'); axes[0,0].set(xticks=x,xticklabels=labels,ylabel='Cases',title='Order-up-to evidence'); axes[0,0].legend(frameon=False,fontsize=6.3); axes[0,0].grid(axis='y',alpha=.15)
    width=.35; axes[0,1].bar(x-width/2,position,width,color=TEAL,label='inventory position'); axes[0,1].bar(x+width/2,order,width,color=GOLD,label='recommended order'); axes[0,1].set(xticks=x,xticklabels=labels,ylabel='Cases',title='Position and case-pack action'); axes[0,1].legend(frameon=False,fontsize=6.3); axes[0,1].grid(axis='y',alpha=.15)
    axes[1,0].axis('off'); axes[1,0].text(.5,.95,'Decision record',ha='center',va='top',color=NAVY,fontsize=10,weight='bold')
    entries=[('Forecast vintage','2025-09-22'),('Selected model','seasonal naive'),('Lead time / service','2 weeks / 90%'),('Constraint','case-pack rounding'),('State','planner review required')]
    for i,(k,v) in enumerate(entries): axes[1,0].text(.05,.76-i*.145,k,color=NAVY,fontsize=7,weight='bold'); axes[1,0].text(.48,.76-i*.145,v,color=RED if k=='State' else TEAL,fontsize=7)
    axes[1,1].axis('off'); axes[1,1].text(.5,.95,'Named ownership and fallback',ha='center',va='top',color=NAVY,fontsize=10,weight='bold')
    entries=[('Demand planning','approve assumptions'),('Data engineering','freshness + lineage'),('Supply planning','capacity constraints'),('Model team','evaluation + monitoring'),('Fallback','seasonal naive + manual review')]
    for i,(k,v) in enumerate(entries):
        y=.78-i*.145; axes[1,1].add_patch(plt.Rectangle((.03,y-.045),.90,.105,facecolor=LIGHT_BLUE if i%2==0 else LIGHT_GOLD,edgecolor='none')); axes[1,1].text(.06,y,k,color=NAVY,fontsize=6.8,weight='bold',va='center'); axes[1,1].text(.46,y,v,color=NAVY,fontsize=6.5,va='center')
    fig.suptitle('A replenishment recommendation is evidence for an accountable decision',color=NAVY,weight='bold',fontsize=11.5); fig.tight_layout(rect=(0,.01,1,.93),h_pad=1.4,w_pad=1.4); save_figure(fig,'fig-59-06',ROOT); plt.close(fig)


if __name__=='__main__': main()
