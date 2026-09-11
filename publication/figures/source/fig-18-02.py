"""Figure 18.2: parameters change location and spread."""
from pathlib import Path
import math,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def normal(x,mu,s):return np.exp(-.5*((x-mu)/s)**2)/(s*np.sqrt(2*np.pi))
def main():
    apply_style();fig,(a,b)=plt.subplots(1,2,figsize=(5.2,3.15));k=np.arange(0,13)
    for lam,c in [(1,BLUE),(4,TEAL),(8,GOLD)]:a.plot(k,[math.exp(-lam)*lam**int(v)/math.factorial(int(v)) for v in k],marker='o',ms=3,color=c,label=f'lambda={lam}')
    a.set_xlabel('Events per interval');a.set_ylabel('Probability mass');a.set_title('Poisson rate shifts the count',color=NAVY,weight='bold',fontsize=9);a.legend(frameon=False,fontsize=7)
    x=np.linspace(40,160,300)
    for s,c in [(8,RED),(15,BLUE),(25,GOLD)]:b.plot(x,normal(x,100,s),color=c,lw=2,label=f'sigma={s}')
    b.set_xlabel('Measurement');b.set_ylabel('Density');b.set_title('Normal sigma changes spread',color=NAVY,weight='bold',fontsize=9);b.legend(frameon=False,fontsize=7)
    for ax in (a,b):ax.grid(color=GREY,alpha=.16)
    fig.suptitle('Parameters select one member of a distribution family',color=NAVY,weight='bold',fontsize=10.5);fig.tight_layout();save_figure(fig,'fig-18-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
