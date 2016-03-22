import matplotlib
matplotlib.use('Agg')
import pylab as plt

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches



cmap = matplotlib.colors.ListedColormap(['b','lightgray','r'])
df = pd.read_table('Drug_cell_gene_connection_Formated_sorted_removeDuplicate2.txt', skiprows=2, header=None, index_col=0)
mat = df
mat.index.name=None
df = pd.read_table('Drug_cell_gene_connection_Formated_sorted_removeDuplicate2.txt', header=None)
drug = df.ix[0,2:df.shape[1]]

drug_set = []
for x in drug:
    if x not in drug_set:
        drug_set.append(x)

cell_line = df.ix[1,2:df.shape[1]]
cell_line_set = list(set(cell_line))
mat.columns = ['Cardiac'] + list(cell_line)


#acmap = sns.color_palette("Set2", len(drug_set)+len(cell_line_set)+2)
acmap = sns.color_palette("Set2", 7)
bcmap = sns.color_palette("hls", 10)

col_colors1 = ['w']+[acmap[drug_set.index(x) + 2] for x in drug]
col_colors2 = ['w']+[bcmap[cell_line_set.index(x) + 1] for x in cell_line]
#col_colors2 = acmap[len(drug_set)+1:len(drug_set)+2]+[acmap[cell_line_set.index(x)+len(drug_set) + 2] for x in cell_line]

cm =sns.clustermap(mat, col_cluster=False,row_cluster=False, col_colors=[col_colors1,col_colors2],  linewidths=.5, cmap=cmap)
cm.cax.set_visible(True)
#cm.cax.set_ylim(0, 1)
cm.cax.yaxis.set_ticks([0.15, 0.85])
#cm.cax.set_yticklabels(['down regulation','up regulation'])
cm.cax.yaxis.set_ticklabels(['down regulation','up regulation'])
cm.ax_heatmap.text(4.5, 17.2, drug_set[0].title(), ha='center')
cm.ax_heatmap.text(11.5, 17.2, drug_set[1].title(), ha='center')
cm.ax_heatmap.text(18.5, 17.2, drug_set[2].title(), ha='center')
cm.ax_heatmap.text(25.5, 17.2, drug_set[3].title(), ha='center')
cm.ax_heatmap.text(31.5, 17.2, drug_set[4].title(), ha='center')
cm.ax_heatmap.text(0.5, 16.7, 'Drug', ha='right')
cm.ax_heatmap.text(0.5, 16.1, 'Cell Line', ha='right')


red_patch = mpatches.Patch(color='red', label='up regulation')
blue_patch = mpatches.Patch(color='blue', label='down regulation')
#ax.legend(handles=[red_patch, blue_patch])
plt.savefig('Drug_cell_gene_connection_removeDuplicate2.pdf')
