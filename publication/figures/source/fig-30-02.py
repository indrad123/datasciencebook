"""Figure 30.2: quality results must be examined by scope."""
from pathlib import Path
import csv,sys
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure


def main():
    apply_style();rows=list(csv.DictReader((ROOT/"data/generated/ch30_sample.csv").open()))
    selected=[rows[0],rows[1],rows[2],rows[3]]
    labels=["Duplicate IDs\nall shipments","Missing temperature\nall shipments","Missing temperature\naffected warehouse","Timestamp order\nall shipments"]
    values=[100*float(r["violation_rate"]) for r in selected]
    colours=[RED,TEAL,RED,GOLD]
    fig,ax=plt.subplots(figsize=(6,3.7));bars=ax.bar(labels,values,color=colours,width=.65)
    for bar,v,r in zip(bars,values,selected):
        label = f"{v:.2f}" if 0 < v < 1 else f"{v:g}"
        ax.text(bar.get_x()+bar.get_width()/2,v+.7,f"{label}%\n{r['status'].upper()}",ha="center",fontsize=8,weight="bold",color=NAVY)
    ax.axhline(5,color=BLUE,ls="--",lw=1.4,label="5% missingness threshold")
    ax.set(ylabel="Violation rate (%)",ylim=(0,36),title="Overall quality can hide a concentrated failure")
    ax.set_title(ax.get_title(),color=NAVY,weight="bold");ax.legend(frameon=False,loc="upper left");ax.grid(axis="y",alpha=.17)
    fig.tight_layout();save_figure(fig,"fig-30-02",ROOT);plt.close(fig)


if __name__=="__main__":main()
