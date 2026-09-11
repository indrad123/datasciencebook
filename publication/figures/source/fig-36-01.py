"""Figure 36.1: linear predictions and signed residuals."""
import csv,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch36_sample.csv").open() as f:r=list(csv.DictReader(f))
 x=[float(z["predicted_hours"]) for z in r];y=[float(z["observed_hours"]) for z in r]
 apply_style();fig,axs=plt.subplots(1,2,figsize=(7.2,3.5));lo=min(x+y)-1;hi=max(x+y)+1;axs[0].plot([lo,hi],[lo,hi],color=NAVY,ls="--");axs[0].scatter(x,y,s=55,color=BLUE)
 for a,b in zip(x,y):axs[0].plot([a,a],[a,b],color=RED,lw=1.4)
 axs[0].set(xlabel="Predicted delivery hours",ylabel="Observed delivery hours",title="Prediction and residual distance")
 axs[1].axhline(0,color=NAVY,lw=1);axs[1].scatter(x,[float(z["residual_hours"]) for z in r],s=55,color=GOLD);axs[1].set(xlabel="Fitted delivery hours",ylabel="Residual: observed - predicted",title="Residuals should be inspected")
 fig.suptitle("Linear regression predicts a numeric outcome",color=NAVY,weight="bold",fontsize=13);fig.tight_layout(rect=(0,0,1,.91));save_figure(fig,"fig-36-01",ROOT);plt.close(fig)
if __name__=="__main__":main()
