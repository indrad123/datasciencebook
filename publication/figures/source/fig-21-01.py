"""Figure 21.1: null model, observed statistic, and simulated p-value."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt,numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();r=[z for z in csv.DictReader((ROOT/'data/generated/ch21_sample.csv').open()) if z['scenario']=='Precise meaningful effect'];x=np.array([float(z['null_effect_units']) for z in r]);obs=float(r[0]['observed_effect_units']);p=float(r[0]['simulated_two_sided_p_value']);fig,ax=plt.subplots(figsize=(5.2,3.15));bins=np.linspace(x.min(),x.max(),35);ax.hist(x,bins=bins,color=BLUE,edgecolor='white');ax.axvline(obs,color=RED,lw=2,label=f'observed effect {obs:.1f}');ax.axvline(-obs,color=RED,lw=1.5,ls=':');ax.set_xlabel('Effect under zero-effect null model');ax.set_ylabel('Simulations');ax.set_title(f'Tail area answers compatibility with the null (p={p:.4f})',color=NAVY,weight='bold');ax.grid(color=GREY,alpha=.16);ax.legend(frameon=False,fontsize=7);fig.tight_layout();save_figure(fig,'fig-21-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
