"""Figure 12.1: conditional probability as a natural-frequency tree."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure

def main():
    apply_style(); fig,ax=plt.subplots(figsize=(5.2,3.15)); ax.axis("off")
    nodes={"all":(0.08,.5,"1,000 cartons"),"d":(.38,.75,"20 defective\n2% prior"),"s":(.38,.25,"980 sound\n98%"),"da":(.78,.88,"18 alerts\n90% sensitivity"),"dn":(.78,.64,"2 no alerts"),"sa":(.78,.36,"49 alerts\n5% false-positive rate"),"sn":(.78,.12,"931 no alerts")}
    for a,b in [("all","d"),("all","s"),("d","da"),("d","dn"),("s","sa"),("s","sn")]:
        ax.annotate("",nodes[b][:2],nodes[a][:2],arrowprops=dict(arrowstyle="->",color=NAVY,lw=1.3))
    for key,(x,y,label) in nodes.items():
        colour=RED if key in ("d","da") else TEAL if key in ("s","sa") else BLUE
        ax.text(x,y,label,ha="center",va="center",fontsize=8,color="white",weight="bold",bbox=dict(boxstyle="round,pad=.45",fc=colour,ec="white"))
    ax.text(.78,.49,"67 alerts total",ha="center",color=GOLD,weight="bold",fontsize=9)
    ax.set_title("Natural frequencies keep the conditioning groups visible",color=NAVY,weight="bold")
    fig.tight_layout(); save_figure(fig,"fig-12-01",ROOT); plt.close(fig)
if __name__=="__main__": main()
