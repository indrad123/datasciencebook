"""Figure 23.1: association, fitted line, and residuals."""
from pathlib import Path
import csv,sys,numpy as np,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,apply_style,save_figure
def main():
    apply_style();r=[x for x in csv.DictReader((ROOT/'data/generated/ch23_sample.csv').open()) if x['scenario']=='linear'];x=np.array([float(z['distance_km']) for z in r]);y=np.array([float(z['delivery_time_minutes']) for z in r]);b=np.polyfit(x,y,1);fit=np.polyval(b,x)
    fig,ax=plt.subplots(figsize=(5.2,3.15));ax.scatter(x,y,s=18,color=BLUE,label='Observed route');ax.plot(x,fit,color=GOLD,lw=2,label=f'Fitted: {b[1]:.1f} + {b[0]:.2f} × distance')
    for xi,yi,fi in zip(x,y,fit):ax.plot([xi,xi],[fi,yi],color=RED,lw=.7,alpha=.6)
    ax.plot([],[],color=RED,lw=1,label='Residual');ax.set(xlabel='Route distance (km)',ylabel='Delivery time (minutes)');ax.set_title('A fitted line summarizes association; residuals retain misses',color=NAVY,weight='bold');ax.grid(color=GREY,alpha=.16);ax.legend(frameon=False,fontsize=6.7);fig.tight_layout();save_figure(fig,'fig-23-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
