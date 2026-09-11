"""Figure 29.2: upper-bound value sensitivity."""
from pathlib import Path
import csv,sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,RED,TEAL,apply_style,save_figure
def main():
 apply_style();rows=list(csv.DictReader((ROOT/'data/generated/ch29_sample.csv').open()));fig,ax=plt.subplots(figsize=(5.8,3.6))
 for frac,col in zip((.10,.25,.40),(TEAL,BLUE,GOLD)):
  z=[r for r in rows if int(r['eligible_orders'])==20000 and float(r['preventable_fraction'])==frac]
  z.sort(key=lambda r:float(r['damage_return_rate']));ax.plot([100*float(r['damage_return_rate']) for r in z],[float(r['upper_bound_value_units']) for r in z],marker='o',lw=2,label=f'{frac:.0%} preventable',color=col)
 ex=next(r for r in rows if r['is_chapter_example']=='yes');ax.scatter([2],[float(ex['upper_bound_value_units'])],s=90,color=RED,zorder=4,edgecolor='white')
 ax.annotate('Chapter example: 3,000',xy=(2,3000),xytext=(2.25,4100),arrowprops=dict(arrowstyle='->',color=RED),color=RED,fontsize=8)
 ax.set(xlabel='Damage-return rate (%)',ylabel='Upper-bound monthly value (illustrative units)',title='Test value before adding model complexity');ax.set_title(ax.get_title(),color=NAVY,weight='bold');ax.legend(frameon=False);ax.grid(alpha=.17);fig.tight_layout();save_figure(fig,'fig-29-02',ROOT);plt.close(fig)
if __name__=='__main__':main()
