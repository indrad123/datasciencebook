"""Figure 14.1: storage type does not determine measurement scale."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
    apply_style();fig,ax=plt.subplots(figsize=(5.2,3.15));ax.axis('off')
    items=[('Warehouse code','Text storage','Nominal','JKT is a label',BLUE),('Satisfaction level','Integer storage','Ordinal','5 is ordered above 4',TEAL),('Temperature °C','Float storage','Interval','differences are meaningful',GOLD),('Weight kg','Float storage','Ratio','zero and ratios are meaningful',RED)]
    for i,(name,storage,scale,note,c) in enumerate(items):
        y=.82-i*.21;ax.text(.29,y,name,transform=ax.transAxes,fontsize=8,weight='bold',color=NAVY,va='center',ha='right');ax.text(.42,y,storage,transform=ax.transAxes,fontsize=7,color='white',va='center',ha='center',bbox=dict(boxstyle='round,pad=.35',fc=c,ec='white'));ax.annotate('',(.61,y),(.52,y),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',color=NAVY));ax.text(.69,y,scale,transform=ax.transAxes,fontsize=8,weight='bold',color=NAVY,ha='center',va='center');ax.text(.80,y,note,transform=ax.transAxes,fontsize=6.2,color=NAVY,va='center')
    ax.set_title('Computer storage type and measurement scale answer different questions',color=NAVY,weight='bold');fig.tight_layout();save_figure(fig,'fig-14-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
