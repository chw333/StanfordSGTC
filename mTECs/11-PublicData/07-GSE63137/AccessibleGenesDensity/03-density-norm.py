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
def GetLabel(n):
    if n in [0,2,4,6]:
        return(Sample2[n])
    elif n in [1,3,5,7]:
        return('_' + Sample2[n])

AX = []
df = pd.read_table('Mouse_Gene_Promoter_Cov_ProteinCoding', header=0)
LibSize = pd.read_table('mTECs-Sample-LibrarySize', header=None)
LS = LibSize.ix[:,1]
df.ix[:,4:df.shape[1]] = df.ix[:,4:df.shape[1]]/list(LS)*20000000

Sample = df.columns[4:]
Sample2 = [' '.join(x.split('_')[0:-1]) for x in df.columns[4:]]

fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.8,0.8])

for i in range(4,df.shape[1]):
    AX.append(sns.kdeplot(np.log2(df.ix[:,i]), shade=False, color=LineColor(i-4), legend=True, label=GetLabel(i-4), bw=2))
'''
patch1 = mpatches.Patch(color='r', label='Tspan8 negative MHCII low')
patch2 = mpatches.Patch(color='b', label='Tspan8 negative MHCII high')
patch3 = mpatches.Patch(color='g', label='Tspan8 positive MHCII low')
patch4 = mpatches.Patch(color='m', label='Tspan8 positive MHCII high')
plt.legend(handles=[patch1, patch2, patch3, patch4])
'''
ax.set_xlabel('Normalized reads number (log2)')
ax.set_ylabel('Density of gene number')
#ax.set_xlim(0, ax.get_xlim()[1])
ax.set_xlim(0,16)
ax.set_xticks(range(0,18,2))

plt.savefig('Mouse-Promoter-Density-Norm.pdf')
