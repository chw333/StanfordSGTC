# coding: utf-8
import matplotlib
matplotlib.use('Agg')
import pylab as plt
import pandas as pd

def scatter(Gene):
    df = pd.read_table('Tspan8_Negative_MHCII_Low_vs_Other_sig.raw.exp',header=0)
    g=df.ix[df.Gene.str.contains(Gene),range(7,df.shape[1])]
    
    df = pd.DataFrame([[1,1,2,2,3,3,4,4],[g.iloc[0][0], g.iloc[0][1], g.iloc[0][4], g.iloc[0][5], g.iloc[0][2], g.iloc[0][3], g.iloc[0][6], g.iloc[0][7]]])
    df = df.T
    df.columns=['Sample','Expression']
    
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.2,0.8,0.7])
    df.plot(kind='scatter',x='Sample',y='Expression',grid=True,color='b',edgecolor='b',s=60, ax=ax)
    ax.set_xlabel('')
    ax.set_ylabel('Raw read counts')
    ax.set_title(Gene)
    ax.set_xlim(0,5)
    ax.set_xticks([0,1,2,3,4,5])
    ax.set_xticklabels(['','Tspan8 positive\nMHCII high','Tspan8 positive\nMHCII low','Tspan8 negative\nMHCII high','Tspan8 negative\nMHCII low',''], fontsize=10)
    plt.savefig(Gene+'.raw.exp.pdf')

scatter('Tspan8')
scatter('Aire')
