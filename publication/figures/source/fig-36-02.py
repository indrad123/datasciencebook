"""Figure 36.2: logistic score to probability and decision."""
import csv,math,sys
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 with (ROOT/"data/generated/ch36_sample.csv").open() as f:r=list(csv.DictReader(f))
 x=[-4+i*.04 for i in range(201)];p=[1/(1+math.exp(-v)) for v in x];cut=math.log(.6/.4)
 apply_style();fig,ax=plt.subplots(figsize=(6.3,3.7));ax.plot(x,p,color=BLUE,lw=2.5);ax.scatter([float(z["logit_score"]) for z in r],[float(z["late_probability"]) for z in r],color=TEAL,s=42,zorder=3);ax.axhline(.6,color=RED,ls="--");ax.axvline(cut,color=RED,ls="--")
 ax.fill_between(x,p,.6,where=[v>=cut for v in x],color=GOLD,alpha=.18);ax.text(1.45,.67,"ALERT REGION",color=RED,weight="bold",fontsize=8);ax.annotate("p = 0.60\nscore ≈ 0.41",(cut,.6),xytext=(-1.5,.76),arrowprops=dict(arrowstyle="->",color=NAVY),fontsize=8,color=NAVY)
 ax.set(xlabel="Linear predictor / log odds",ylabel="Late-shipment probability",ylim=(0,1),title="The logistic link maps every score into 0 to 1");fig.tight_layout();save_figure(fig,"fig-36-02",ROOT);plt.close(fig)
if __name__=="__main__":main()
