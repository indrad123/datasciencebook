"""Figure 32.1: prediction-time feature boundary."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(6.2,3.3));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off");ax.plot([.08,.92],[.5,.5],color=NAVY,lw=2);ax.axvline(.52,.18,.82,color=RED,ls="--",lw=2)
 ax.text(.52,.87,"MONDAY 06:00\nFORECAST ORIGIN",ha="center",color=RED,weight="bold",fontsize=9)
 for x,t in [(.13,"Prior demand"),(.28,"Planned promotion"),(.42,"Stock available")]:ax.text(x,.59,t,ha="center",fontsize=7,color=NAVY,bbox=dict(boxstyle="round,pad=.35",fc="white",ec=TEAL))
 for x,t in [(.66,"Final shipped quantity"),(.81,"Return quantity"),(.91,"Revised promotion")]:ax.text(x,.39,t,ha="center",fontsize=7,color=RED,bbox=dict(boxstyle="round,pad=.35",fc="white",ec=RED))
 ax.text(.28,.25,"ELIGIBLE: reliably available before scoring",ha="center",color=TEAL,weight="bold",fontsize=8);ax.text(.76,.25,"LEAKAGE: created after the boundary",ha="center",color=RED,weight="bold",fontsize=8)
 ax.set_title("Feature eligibility depends on availability time",color=NAVY,weight="bold");fig.tight_layout();save_figure(fig,"fig-32-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
