"""Figure 27.1: statistical reasoning continues into machine learning."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(5.8,2.8));ax.axis('off');labels=['Describe\nwhat happened','Infer\nwith uncertainty','Predict\nunseen cases','Decide\nunder costs'];cols=[BLUE,TEAL,GOLD,RED]
 for i,(t,c) in enumerate(zip(labels,cols)):
  x=.08+i*.24;ax.text(x,.52,t,ha='center',va='center',fontsize=8,weight='bold',color='white',bbox=dict(boxstyle='round,pad=.7',facecolor=c,edgecolor='none')); 
  if i<3:ax.annotate('',xy=(x+.17,.52),xytext=(x+.105,.52),arrowprops=dict(arrowstyle='->',color=NAVY,lw=1.5))
 ax.text(.5,.15,'Data meaning • uncertainty • validation • operational context',ha='center',color=NAVY,fontsize=8);ax.set_title('Machine learning extends—not replaces—statistical reasoning',color=NAVY,weight='bold');fig.tight_layout();save_figure(fig,'fig-27-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
