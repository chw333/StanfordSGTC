# coding: utf-8
import matplotlib 
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import pylab as plt
df = pd.read_table('expression_atlas-retinoic_acid_AND_Homo_sapiens_median_sorted', header=None)
df2 = df[1]
fig = plt.figure()
ax = fig.add_axes([0.12,0.12,0.8,0.8])
df2.hist(ax=ax, color='m')
ax.set_xlim(-10,10)
ax.set_xticks(range(-10,12,2))
ax.set_xlabel('Fold change (log2)')
ax.set_ylabel('Number of genes')
ax.set_title('Differential expression given with retinoic acid (FDR=0.05)')
ax.annotate('RBM20', xy=[4.1,0], xytext=[4.1,100], arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('CNR1', xy=[8.2,0], xytext=[8.2,400], arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('HOXB3', xy=[8.0,0], xytext=[5,300], arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('HOXA3', xy=[7.3,0], xytext=[4,200], arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('LHX2', xy=[-6.9,0], xytext=[-9,100], arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('SIX3', xy=[-6.1,0], xytext=[-7,200], arrowprops=dict(facecolor='black', shrink=0.05))
plt.savefig('RetinoicAcidDEG.pdf')
