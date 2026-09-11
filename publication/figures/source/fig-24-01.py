"""Figure 24.1: outcome type guides group-comparison method."""
from pathlib import Path
import sys,matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from publication.figure_style import BLUE,GOLD,NAVY,TEAL,apply_style,save_figure
def main():
 apply_style();fig,ax=plt.subplots(figsize=(5.5,3.15));ax.axis('off');rows=[('Categorical','Late / on time','Counts and proportions','Chi-square'),('Continuous','Picking minutes','Means and spread','ANOVA / Welch'),('Ordinal','Rating 1–5','Ranks and categories','Kruskal–Wallis'),('Restricted design','Blocked assignments','Chosen statistic','Permutation')]
 table=ax.table(cellText=rows,colLabels=['Outcome structure','NRG example','Show first','Starting method'],cellLoc='left',colLoc='left',loc='center',colWidths=[.21,.23,.27,.24]);table.auto_set_font_size(False);table.set_fontsize(6.6);table.scale(1,1.75)
 for (r,c),cell in table.get_celld().items():cell.set_edgecolor('white');cell.set_facecolor(NAVY if r==0 else ('#E8F1F5' if r%2 else '#F7F3E8'));cell.get_text().set_color('white' if r==0 else NAVY);cell.get_text().set_weight('bold' if r==0 else 'normal')
 ax.set_title('Choose the method from the outcome and design',color=NAVY,weight='bold',pad=12);fig.tight_layout();save_figure(fig,'fig-24-01',ROOT);plt.close(fig)
if __name__=='__main__':main()
