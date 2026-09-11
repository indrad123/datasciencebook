"""Figure 30.1: provenance from source event to analytical decision."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure


def main():
    apply_style();fig,ax=plt.subplots(figsize=(6.4,3.5));ax.axis("off")
    labels=[("CREATE","Gate scan\n+ device/timezone"),("STORE","TMS table\n+ key/definition"),("EXTRACT","Versioned query\n+ filters/time"),("TRANSFORM","UTC + route map\n+ code versions"),("INTEGRATE","Join keys\n+ unmatched counts"),("FREEZE & USE","Hash + schema\n+ model/report")]
    colours=[TEAL,BLUE,GOLD,RED,BLUE,TEAL]
    for i,((head,body),colour) in enumerate(zip(labels,colours)):
        row,col=divmod(i,3);x=.04+col*.32;y=.56-row*.42
        ax.text(x+.125,y+.15,head,ha="center",weight="bold",color=colour,fontsize=8)
        ax.text(x+.125,y+.06,body,ha="center",va="center",color=NAVY,fontsize=7,
                bbox=dict(boxstyle="round,pad=.5",facecolor="white",edgecolor=colour,lw=1.7))
        if col<2: ax.annotate("",xy=(x+.30,y+.07),xytext=(x+.27,y+.07),arrowprops=dict(arrowstyle="->",color=NAVY,lw=1.3))
    ax.text(.5,.96,"Provenance records meaning as well as movement",ha="center",color=NAVY,weight="bold",fontsize=12)
    ax.text(.5,.03,"Every transformation retains evidence needed to reproduce and judge the dataset",ha="center",color=NAVY,fontsize=8)
    fig.tight_layout();save_figure(fig,"fig-30-01",ROOT);plt.close(fig)


if __name__=="__main__":main()
