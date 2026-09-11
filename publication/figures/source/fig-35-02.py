"""Figure 35.2: threshold selection balances recall, workload, and cost."""
import csv,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch35_sample.csv").open() as f:rows=[r for r in csv.DictReader(f) if r["model"]=="late_model"]
 x=[float(r["threshold"]) for r in rows];rec=[float(r["recall"]) for r in rows];pre=[float(r["precision"]) for r in rows];alerts=[int(r["alerts"]) for r in rows]
 apply_style();fig,axs=plt.subplots(1,2,figsize=(7.2,3.5));axs[0].plot(x,rec,"o-",color=BLUE,label="Recall");axs[0].plot(x,pre,"o-",color=TEAL,label="Precision");axs[0].axhline(.70,color=RED,ls="--",label="Minimum recall");axs[0].set(xlabel="Alert threshold",ylabel="Metric value",ylim=(0,1),title="Coverage and alert reliability");axs[0].legend(frameon=False,fontsize=7)
 axs[1].plot(x,alerts,"o-",color=GOLD);axs[1].axhline(100,color=RED,ls="--",label="Capacity: 100");axs[1].scatter([.6],[98],s=90,color=TEAL,zorder=4);axs[1].annotate("Feasible\nthreshold",(.6,98),xytext=(.66,155),arrowprops=dict(arrowstyle="->",color=NAVY),fontsize=8,color=NAVY);axs[1].set(xlabel="Alert threshold",ylabel="Alerts per 1,000 shipments",title="Operational workload");axs[1].legend(frameon=False,fontsize=7)
 fig.suptitle("A threshold is an operational decision",color=NAVY,weight="bold",fontsize=13);fig.tight_layout(rect=(0,0,1,.91));save_figure(fig,"fig-35-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
