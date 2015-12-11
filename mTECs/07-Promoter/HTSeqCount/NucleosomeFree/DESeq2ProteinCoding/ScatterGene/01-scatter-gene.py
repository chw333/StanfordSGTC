# coding: utf-8
import matplotlib
matplotlib.use('Agg')
import pylab as plt
import pandas as pd

Gene = 'Tspan8'
df = pd.read_table('Tspan8_Negative_MHCII_Low_vs_Other_sig_exp',header=0)
g=df.ix[df.Gene.str.contains(Gene),range(7,df.shape[1])]

df = pd.DataFrame([[1,2,3,4,5,6,7,8],[g.iloc[0][0], g.iloc[0][1], g.iloc[0][4], g.iloc[0][5], g.iloc[0][2], g.iloc[0][3], g.iloc[0][6], g.iloc[0][7]]])
df = df.T
df.columns=['Sample','Expression']

fig = plt.figure()
ax = fig.add_axes([0.1,0.2,0.8,0.7])
df.plot(kind='scatter',x='Sample',y='Expression',grid=True,color='b',edgecolor='b',s=60, ax=ax)
ax.set_xlabel('')
ax.set_xticklabels(['','TpMh1','TpMh2','TpMl1','TpMl2','TnMh1','TnMh2','TnMl1','TnMl2',''])
ax.set_ylabel('Normalized read counts')
ax.set_title('Tspan8')
plt.savefig(Gene+'.exp.pdf')
