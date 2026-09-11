"""Figure 23.2: patterns a correlation coefficient can conceal."""
from pathlib import Path
import csv,sys,numpy as np,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,apply_style,save_figure
def main():
    apply_style();rows=list(csv.DictReader((ROOT/'data/generated/ch23_sample.csv').open()));fig,axs=plt.subplots(1,3,figsize=(6.2,2.55));cases=[('curvature','Curvature'),('unequal_spread','Unequal spread'),('linear','High leverage')]
    for ax,(case,title) in zip(axs,cases):
        z=[q for q in rows if q['scenario']==case];x=np.array([float(q['distance_km']) for q in z]);y=np.array([float(q['delivery_time_minutes']) for q in z])
        if title=='High leverage':
            base=np.polyfit(x,y,1);q=next(q for q in rows if q['scenario']=='influence');xa=float(q['distance_km']);ya=float(q['delivery_time_minutes']);aug=np.polyfit(np.r_[x,xa],np.r_[y,ya],1);xx=np.array([x.min(),xa]);ax.plot(xx,np.polyval(base,xx),color=GOLD,lw=1.5,label='Before');ax.plot(xx,np.polyval(aug,xx),color=RED,lw=1.5,label='After');ax.scatter([xa],[ya],marker='D',s=28,color=RED);ax.legend(frameon=False,fontsize=5.8)
        else:
            b=np.polyfit(x,y,1);ax.plot(x,np.polyval(b,x),color=GOLD,lw=1.5)
        ax.scatter(x,y,s=8,color=BLUE,alpha=.8);ax.set_title(title,color=NAVY,weight='bold',fontsize=9);ax.grid(color=GREY,alpha=.14);ax.set_xlabel('Distance (km)',fontsize=7);ax.tick_params(labelsize=6)
    axs[0].set_ylabel('Delivery time (minutes)',fontsize=7);fig.suptitle('The scatterplot reveals what one fitted line can hide',color=NAVY,weight='bold',fontsize=12);fig.tight_layout();save_figure(fig,'fig-23-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
