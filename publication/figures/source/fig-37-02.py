"""Figure 37.2: tree ensembles trade performance for complexity."""
import csv,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch37_sample.csv").open() as f:r=list(csv.DictReader(f))
 names=[x["model"].replace("_","\n").title() for x in r];cost=[int(x["validation_cost_idr"])/1e6 for x in r];lat=[int(x["latency_ms"]) for x in r];colors=[NAVY,BLUE,GOLD,TEAL,RED]
 apply_style();fig,axs=plt.subplots(1,2,figsize=(7.2,3.55));axs[0].bar(names,cost,color=colors);axs[0].set(ylabel="Expected cost (million IDR/day)",title="Chronological validation cost");axs[0].set_ylim(0,20);axs[0].tick_params(axis="x",labelsize=7)
 axs[1].scatter(lat,cost,s=[90,100,110,150,150],c=colors);[axs[1].annotate(n.replace("\n"," "),(x,y),xytext=(4,4),textcoords="offset points",fontsize=6.5) for n,x,y in zip(names,lat,cost)];axs[1].set(xlabel="Model inference latency (ms)",ylabel="Expected cost (million IDR/day)",title="Value must justify operating cost")
 fig.suptitle("Trees and ensembles solve different trade-offs",color=NAVY,weight="bold",fontsize=13);fig.tight_layout(rect=(0,0,1,.91));save_figure(fig,"fig-37-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
