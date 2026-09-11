"""Figure 34.1: training and validation loss across complexity."""
import csv,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch34_sample.csv").open() as f:rows=[r for r in csv.DictReader(f) if r["curve"]=="validation"]
 x=[int(r["setting"]) for r in rows];tr=[int(r["training_mse"]) for r in rows];va=[int(r["validation_mse"]) for r in rows]
 apply_style();fig,ax=plt.subplots(figsize=(6.3,3.7));ax.plot(x,tr,"o-",color=BLUE,lw=2,label="Training MSE");ax.plot(x,va,"o-",color=GOLD,lw=2,label="Validation MSE")
 ax.axvspan(.5,1.8,color=RED,alpha=.08);ax.axvspan(9,12.5,color=RED,alpha=.08);ax.annotate("Both losses high:\nunderfitting",(1,560),xytext=(2.2,500),arrowprops=dict(arrowstyle="->",color=NAVY),fontsize=8,color=NAVY);ax.annotate("Large gap:\noverfitting",(12,480),xytext=(8.2,525),arrowprops=dict(arrowstyle="->",color=NAVY),fontsize=8,color=NAVY)
 ax.set(xticks=x,xlabel="Polynomial degree (complexity)",ylabel="Mean squared error",title="Training fit alone cannot select complexity");ax.legend(frameon=False,ncol=2);fig.tight_layout();save_figure(fig,"fig-34-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
