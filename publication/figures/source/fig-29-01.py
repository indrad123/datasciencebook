"""Figure 29.1: analytical problem canvas."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(6.3,3.6));ax.axis('off')
 items=[('DECISION','Allocate up to 200\npre-dispatch inspections'),('UNIT','One eligible\nretail order'),('OUTCOME','Damage-coded return\nwithin 30 days'),('USE TIME','Two hours\nbefore dispatch'),('ACTION','Inspect, repack,\nor leave unchanged'),('SUCCESS','Prevented returns and net value\nwithout unacceptable delay')]
 cols=[RED,BLUE,TEAL,GOLD,RED,BLUE]
 for i,((h,t),c) in enumerate(zip(items,cols)):
  row,col=divmod(i,3);x=.03+col*.325;y=.53-row*.43
  ax.add_patch(plt.Rectangle((x,y),.29,.32,facecolor='white',edgecolor=c,lw=2))
  ax.text(x+.02,y+.24,h,color=c,weight='bold',fontsize=8);ax.text(x+.02,y+.08,t,color=NAVY,fontsize=7.2)
 ax.text(.5,.95,'Turn a broad concern into an analytical problem',ha='center',color=NAVY,weight='bold',fontsize=12)
 ax.text(.5,.04,'Population, constraints, baseline, stakeholders, and harms complete the specification',ha='center',color=NAVY,fontsize=7.5)
 fig.tight_layout();save_figure(fig,'fig-29-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
