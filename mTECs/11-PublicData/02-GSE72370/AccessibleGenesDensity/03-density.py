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
    if n in [0,2,4,6]:
        return(COLORS[n/2])
    elif n in [1,3,5,7]:
        return(COLORS[(n-1)/2])

#### another method to remove some labels. Start with _
def GetLabel(n,Sample2):
    if n in [0,2,4,6]:
        return(Sample2[n])
    elif n in [1,3,5,7]:
        return('_' + Sample2[n])

def density(ouF, bandwidth):
    AX = []
    df = pd.read_table('Mouse_Gene_Promoter_Cov_ProteinCoding-Norm', header=0)
    
    Sample = df.columns[4:]
    #Sample2 = Sample
    Sample2 = [' '.join(x.split('_')[0:-1]) for x in df.columns[4:]]
    
    fig = plt.figure()
    ax = fig.add_axes([0.15,0.15,0.8,0.8])
    
    for i in range(4,df.shape[1]):
        AX.append(sns.kdeplot(np.log2(df.ix[:,i]), shade=True, color=LineColor(i-4), legend=True, label=GetLabel(i-4, Sample2), bw=bandwidth))
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

density('Mouse-Promoter-Density', 0.1)
density('Mouse-Promoter-Density', 0.3)
density('Mouse-Promoter-Density', 0.5)
density('Mouse-Promoter-Density', 1)
density('Mouse-Promoter-Density', 2)
density('Mouse-Promoter-Density', 3)
density('Mouse-Promoter-Density', 4)
density('Mouse-Promoter-Density', 5)
density('Mouse-Promoter-Density', 6)
density('Mouse-Promoter-Density', 7)
density('Mouse-Promoter-Density', 8)
density('Mouse-Promoter-Density', 9)
density('Mouse-Promoter-Density', 10)
