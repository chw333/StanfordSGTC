import matplotlib 
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import pylab as plt

cmap = sns.light_palette("blue", as_cmap=True)

SIG = 0.0001
df = pd.read_table('MHCII_low_Tspan8_PositiveNegative_sig.Feature.Annot.matrix')
mat = df.ix[df.padj<SIG,[0]+range(7,len(df.ix[0,]))]
mat.index=[x.split('_')[0] for x in mat.ix[:,0]]
mat = mat.ix[:,1:]

### remove empty columns
X = []
for i in range(len(mat.ix[0,])):
    if 1 in list(mat.ix[:,i]):
        X.append(True)
    else:
        X.append(False)
mat = mat.ix[:,X]



cm = sns.clustermap(mat, cmap=cmap)

hm = cm.ax_heatmap.get_position()
rd = cm.ax_row_dendrogram.get_position()
cd = cm.ax_col_dendrogram.get_position()
ca = cm.cax.get_position()


msy = 0
msx = -0.07
cm.ax_heatmap.set_position([hm.x0+msx, hm.y0+msy, hm.width, hm.height])
cm.ax_row_dendrogram.set_position([rd.x0+msx, rd.y0+msy, rd.width, rd.height])
cm.ax_col_dendrogram.set_position([cd.x0+msx, cd.y0+msy, cd.width, cd.height])
cm.cax.set_position([ca.x0+msx, ca.y0, ca.width, ca.height])

cm.cax.yaxis.set_ticklabels([0,'','','','',1])
cm.cax.yaxis.set_label_position('left')
cm.cax.yaxis.set_label_text('TF binding')


plt.setp(cm.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)

plt.savefig('test.pdf')
