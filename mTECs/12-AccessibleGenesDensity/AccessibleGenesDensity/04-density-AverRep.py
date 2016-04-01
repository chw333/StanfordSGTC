### legend thin line
import matplotlib
matplotlib.use('Agg')
import pylab as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches

def LineColor(n):
    COLORS= ['r','b','g','m']
    return(COLORS[n])

#### another method to remove some labels. Start with _
def GetLabel(n,Sample2):
    return(Sample2[n])

LibSize = pd.read_table('mTECs-Sample-LibrarySize-NF-AverRep', header=None)
LibSizeFactor =  20000000


def density(ouF, bandwidth):
    AX = []
    df = pd.read_table('mTECs_Gene_Promoter_Cov_ProteinCoding-AverRep', header=0)
    
    Sample = df.columns[4:]
    Sample2 = Sample
    #Sample2 = [' '.join(x.split('_')[0:-1]) for x in df.columns[4:]]
    
    fig = plt.figure()
    ax = fig.add_axes([0.15,0.15,0.8,0.8])
    
    for i in range(4,df.shape[1]):
        AX.append(sns.kdeplot(np.log2(df.ix[:,i]/LibSize.ix[i-4,1]*LibSizeFactor), shade=False, color=LineColor(i-4), legend=True, label=GetLabel(i-4, Sample2), bw=bandwidth))
    '''
    patch1 = mpatches.Patch(color='r', label='Tspan8 negative MHCII low')
    patch2 = mpatches.Patch(color='b', label='Tspan8 negative MHCII high')
    patch3 = mpatches.Patch(color='g', label='Tspan8 positive MHCII low')
    patch4 = mpatches.Patch(color='m', label='Tspan8 positive MHCII high')
    plt.legend(handles=[patch1, patch2, patch3, patch4])
    '''
    ax.set_xlabel('Normalized number of reads (log2)')
    ax.set_ylabel('Density of gene numbers')
    ax.set_xlim(0, ax.get_xlim()[1])
    
    plt.savefig(ouF +'-bw_'+ str(bandwidth) + '.pdf')

density('mTECs-Promoter-Density-AverRep', 0.1)
density('mTECs-Promoter-Density-AverRep', 0.3)
density('mTECs-Promoter-Density-AverRep', 0.5)
density('mTECs-Promoter-Density-AverRep', 1)
density('mTECs-Promoter-Density-AverRep', 2)
density('mTECs-Promoter-Density-AverRep', 3)
density('mTECs-Promoter-Density-AverRep', 4)
density('mTECs-Promoter-Density-AverRep', 5)
density('mTECs-Promoter-Density-AverRep', 6)
density('mTECs-Promoter-Density-AverRep', 7)
density('mTECs-Promoter-Density-AverRep', 8)
density('mTECs-Promoter-Density-AverRep', 9)
density('mTECs-Promoter-Density-AverRep', 10)
