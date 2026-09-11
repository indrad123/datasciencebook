"""Figure 27.2: compare baselines and learned models on test data."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,apply_style,save_figure
def main():
 apply_style();r=[x for x in csv.DictReader((ROOT/'data/generated/ch27_sample.csv').open()) if x['split']=='test'];tasks=['demand','transit'];base=[];learn=[]
 for t in tasks:
  z=[x for x in r if x['task']==t];base.append(sum(float(x['absolute_error_baseline']) for x in z)/len(z));learn.append(sum(float(x['absolute_error_learned']) for x in z)/len(z))
 fig,ax=plt.subplots(figsize=(5.2,3));x=range(2);ax.bar([i-.18 for i in x],base,.36,label='Baseline',color=GOLD);ax.bar([i+.18 for i in x],learn,.36,label='Learned model',color=BLUE);ax.set_xticks(list(x),['Demand cases','Transit hours']);ax.set_ylabel('Test mean absolute error');ax.set_title('Complexity earns its place on unseen cases',color=NAVY,weight='bold');ax.legend(frameon=False);ax.grid(axis='y',alpha=.17);fig.tight_layout();save_figure(fig,'fig-27-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
