import matplotlib 
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import pylab as plt
import numpy as np

cmap = sns.light_palette("blue", as_cmap=True)

df = pd.read_table('Tspan8_Negative_MHCII_Low_vs_Other_sig_exp')
mat = df.ix[:, [7,8,11,12,9,10,13,14]]
mat.index = [x.split('_')[0] for x in list(df.ix[:, 0])]
mat.columns= ['TpMh1','TpMh2','TpMl1','TpMl2','TnMh1','TnMh2','TnMl1','TnMl2']


mat2 = np.log2(mat)
#mat2 = mat2.ix[0:50,]
cm = sns.clustermap(mat2, cmap=cmap, col_cluster=False, z_score=0, yticklabels=False)

hm = cm.ax_heatmap.get_position()
rd = cm.ax_row_dendrogram.get_position()
cd = cm.ax_col_dendrogram.get_position()
ca = cm.cax.get_position()

msy = 0.3
msx = -0.07
cm.ax_heatmap.set_position([hm.x0+msx, hm.y0, hm.width*msy, hm.height])
cm.ax_row_dendrogram.set_position([rd.x0+msx, rd.y0, rd.width, rd.height])
#cm.ax_col_dendrogram.set_position([cd.x0+msx, cd.y0, cd.width*msy, cd.height])
cm.cax.set_position([ca.x0-0.04, ca.y0-0.3, ca.width, ca.height])

#cm.cax.yaxis.set_ticklabels([0,'','','','',1])
cm.cax.yaxis.set_label_position('left')
cm.cax.yaxis.set_label_text('z-score')


plt.setp(cm.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)

plt.savefig('Tspan8_Negative_MHCII_Low_vs_Other_sig_exp_total.pdf')
