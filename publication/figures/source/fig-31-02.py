"""Figure 31.2: cleaning effects remain visible."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();r=list(csv.DictReader((ROOT/"data/generated/ch31_sample.csv").open()));fig,(a,b)=plt.subplots(1,2,figsize=(6.4,3.5))
 steps=["Raw","Final"];counts=[int(r[0]["input_rows"]),int(r[-1]["output_rows"])]
 a.bar(steps,counts,color=[GOLD,BLUE]);a.set_ylim(0,11500);a.set_ylabel("Rows");a.set_title("Row count is reconciled",color=NAVY,weight="bold",fontsize=10)
 for i,v in enumerate(counts):a.text(i,v+220,f"{v:,}",ha="center",weight="bold",color=NAVY)
 z=[x for x in r if int(x["affected_values"]) and x["step"]!="Preserve currency"];names=[x["step"] for x in z];vals=[int(x["affected_values"]) for x in z]
 b.barh(names,vals,color=[TEAL,BLUE,GOLD,RED]);b.set_xscale("log");b.set_xlabel("Affected values or rows (log scale)");b.set_title("Every change remains visible",color=NAVY,weight="bold",fontsize=10);b.tick_params(axis="y",labelsize=7)
 a.grid(axis="y",alpha=.17);b.grid(axis="x",alpha=.17)
 fig.suptitle("Cleaning changes evidence—record its effects",color=NAVY,weight="bold",fontsize=12);fig.tight_layout();save_figure(fig,"fig-31-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
