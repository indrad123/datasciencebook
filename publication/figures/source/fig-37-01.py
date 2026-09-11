"""Figure 37.1: constrained shipment-risk decision tree."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(7,4));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
 nodes=[(.5,.84,"WAITING > 9 HOURS?",NAVY),(.27,.55,"DISTANCE > 1,500 KM?",BLUE),(.73,.55,"REFRIGERATED?",RED),(.12,.22,"LOW\n12% late",TEAL),(.38,.22,"MEDIUM\n31% late",GOLD),(.62,.22,"HIGH\n58% late",RED),(.88,.22,"VERY HIGH\n76% late",RED)]
 for x,y,t,c in nodes:ax.text(x,y,t,ha="center",va="center",fontsize=8,weight="bold",color=c,bbox=dict(boxstyle="round,pad=.45",fc="white",ec=c,lw=2))
 for a,b in [((.5,.78),(.27,.61)),((.5,.78),(.73,.61)),((.27,.49),(.12,.29)),((.27,.49),(.38,.29)),((.73,.49),(.62,.29)),((.73,.49),(.88,.29))]:ax.annotate("",b,a,arrowprops=dict(arrowstyle="->",color=NAVY,lw=1.5))
 for x,y,t in [(.36,.68,"NO"),(.64,.68,"YES"),(.17,.39,"NO"),(.35,.39,"YES"),(.65,.39,"NO"),(.83,.39,"YES")]:ax.text(x,y,t,color=NAVY,fontsize=7,weight="bold")
 ax.set_title("A constrained tree turns interactions into explicit paths",color=NAVY,weight="bold");fig.tight_layout();save_figure(fig,"fig-37-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
