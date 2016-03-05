import matplotlib
matplotlib.use('Agg')
import pylab as plt

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.patches as patches


cmap = matplotlib.colors.ListedColormap(['b','lightgray','r'])
df = pd.read_table('Drug_cell_gene_connection_Formated_sorted', skiprows=2, header=None, index_col=0)
mat = df
mat.index.name=None
df = pd.read_table('Drug_cell_gene_connection_Formated_sorted', header=None)
drug = df.ix[0,2:df.shape[1]]
drug_set = list(set(drug))
cell_line = df.ix[1,2:df.shape[1]]
cell_line_set = list(set(cell_line))
mat.columns = ['Cardiac'] + list(cell_line)


#acmap = sns.color_palette("Set2", len(drug_set)+len(cell_line_set)+2)
acmap = sns.color_palette("Set2", 10)
bcmap = sns.color_palette("husl", 15)

col_colors1 = ['w']+[acmap[drug_set.index(x) + 2] for x in drug]
col_colors2 = ['w']+[bcmap[cell_line_set.index(x) + 1] for x in cell_line]
#col_colors2 = acmap[len(drug_set)+1:len(drug_set)+2]+[acmap[cell_line_set.index(x)+len(drug_set) + 2] for x in cell_line]


cm =sns.clustermap(mat, col_cluster=False,row_cluster=False, col_colors=[col_colors1,col_colors2],  linewidths=.5, cmap=cmap)
cm.cax.set_visible(False)
plt.savefig('Drug_cell_gene_connection.pdf')
