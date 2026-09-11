"""Figure 12.2: prior, likelihood, evidence, and posterior."""
from pathlib import Path
import sys
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,GREY,NAVY,RED,TEAL,apply_style,save_figure

def main():
    apply_style(); fig,(ax1,ax2)=plt.subplots(1,2,figsize=(5.2,3.15))
    labels=["Defective\nand alert","Sound\nand alert"]; counts=[18,49]
    ax1.bar(labels,counts,color=[RED,TEAL],width=.62)
    for i,v in enumerate(counts): ax1.text(i,v+1,str(v),ha="center",color=NAVY,weight="bold")
    ax1.set_ylim(0,58); ax1.set_ylabel("Cartons among 1,000"); ax1.set_title("Evidence: 67 alerts",color=NAVY,weight="bold",fontsize=9); ax1.grid(axis="y",color=GREY,alpha=.18)
    ax2.axis("off")
    stages=[("Prior P(D)","2.0%",BLUE,.80),("Likelihood P(A|D)","90.0%",GOLD,.57),("Joint P(D and A)","1.8%",RED,.34),("Posterior P(D|A)","26.9%",NAVY,.11)]
    for label,value,colour,y in stages:
        ax2.text(.52,y,f"{label}\n{value}",transform=ax2.transAxes,ha="center",va="center",fontsize=8,color="white",weight="bold",bbox=dict(boxstyle="round,pad=.42",fc=colour,ec="white"))
    for y1,y2 in ((.72,.65),(.49,.42),(.26,.19)):
        ax2.annotate("",(.52,y2),(.52,y1),xycoords="axes fraction",arrowprops=dict(arrowstyle="->",color=NAVY,lw=1.2))
    ax2.set_title("Bayes update after an alert",color=NAVY,weight="bold",fontsize=9)
    fig.suptitle("A strong detector can still have a modest posterior",color=NAVY,weight="bold",fontsize=11)
    fig.tight_layout(); save_figure(fig,"fig-12-02",ROOT); plt.close(fig)
if __name__=="__main__": main()
