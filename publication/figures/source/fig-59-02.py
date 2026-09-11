"""Figure 59.2: weekly demand history and final forecast origin."""
import csv, sys
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

ROOT = Path(__file__).resolve().parents[3]; sys.path.insert(0, str(ROOT))
from publication.figure_style import BLUE, GOLD, NAVY, RED, TEAL, apply_style, save_figure


def main():
    rows=list(csv.DictReader((ROOT/'data/generated/ch59_sample.csv').open()))
    apply_style(); fig, axes=plt.subplots(3,1,figsize=(8,6),sharex=True)
    for ax, product in zip(axes, ['SAMBAL_250','KOPI_200','TEH_20']):
        p=[r for r in rows if r['product_id']==product]; dates=np.array([np.datetime64(r['week_start']) for r in p])
        demand=np.array([float(r['latent_demand_cases']) for r in p]); sales=np.array([float(r['observed_sales_cases']) for r in p])
        promo=np.array([r['promotion']=='1' for r in p]); stock=np.array([r['stockout']=='1' for r in p])
        ax.plot(dates,demand,color=BLUE,lw=1.2,label='latent demand'); ax.plot(dates,sales,color=TEAL,lw=.8,alpha=.7,label='observed sales')
        ax.scatter(dates[promo],demand[promo],marker='^',s=24,color=GOLD,label='promotion')
        ax.scatter(dates[stock],sales[stock],marker='x',s=28,color=RED,label='stockout')
        ax.axvline(dates[-13],color=NAVY,ls='--',lw=1); ax.axvspan(dates[-13],dates[-1],color=GOLD,alpha=.10)
        ax.set(ylabel='Cases',title=product.replace('_',' ')); ax.grid(alpha=.15)
    axes[0].legend(ncol=4,frameon=False,fontsize=6.2,loc='upper left')
    axes[-1].set(xlabel='Week starting Monday'); axes[-1].xaxis.set_major_locator(mdates.MonthLocator(interval=4)); axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    fig.suptitle('History remains visible at the product–distribution-centre decision grain',color=NAVY,weight='bold',fontsize=11.5)
    fig.text(.84,.93,'13-week holdout →',color=NAVY,fontsize=7)
    fig.tight_layout(rect=(0,.01,1,.93)); save_figure(fig,'fig-59-02',ROOT); plt.close(fig)


if __name__=='__main__': main()
