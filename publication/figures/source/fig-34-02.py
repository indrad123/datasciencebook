"""Figure 34.2: learning curves distinguish high bias from high variance."""
import csv,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch34_sample.csv").open() as f:rows=list(csv.DictReader(f))
 apply_style();fig,axs=plt.subplots(1,2,figsize=(7.2,3.45),sharey=True)
 for ax,scenario,title,note in zip(axs,["high_bias","high_variance"],["HIGH BIAS","HIGH VARIANCE"],["Poor levels converge\nMore rows alone help little","Gap narrows as data grow\nMore representative data may help"]):
  rr=[r for r in rows if r["scenario"]==scenario];x=[int(r["training_rows"]) for r in rr]
  ax.plot(x,[int(r["training_mse"]) for r in rr],"o-",color=BLUE,label="Training");ax.plot(x,[int(r["validation_mse"]) for r in rr],"o-",color=GOLD,label="Validation");ax.set_title(title,color=NAVY,weight="bold");ax.set_xlabel("Training observations");ax.text(.5,.84,note,transform=ax.transAxes,ha="center",fontsize=8,color=NAVY,bbox=dict(boxstyle="round,pad=.35",fc="white",ec=NAVY,alpha=.9));ax.grid(alpha=.2)
 axs[0].set_ylabel("Mean squared error");axs[0].legend(frameon=False);fig.suptitle("Learning curves diagnose different remedies",color=NAVY,weight="bold",fontsize=13);fig.tight_layout(rect=(0,0,1,.91));save_figure(fig,"fig-34-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
