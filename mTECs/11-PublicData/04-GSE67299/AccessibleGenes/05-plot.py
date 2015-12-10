### legend shows replicates

import matplotlib 
matplotlib.use('Agg')
import pylab as plt
import pandas as pd

def LineColor(n):
    COLORS = ['m','b','g','r']
    return(COLORS[n])

df = pd.read_table('Mouse-Gene-Promoter-AccessibleNum_Gene', header=0)
Sample = df.columns[1:]
Sample2 = Sample

fig = plt.figure()
ax = fig.add_axes([0.15,0.1,0.8,0.8])
AX = []
for i in range(1,df.shape[1]):
    AX.append(ax.plot(df.ix[:,0], df.ix[:,i], color=LineColor(i-1)))

legAX = [AX[3][0], AX[0][0], AX[1][0], AX[2][0]]
ax.legend(legAX, [Sample2[3], Sample2[0], Sample2[1], Sample2[2]], loc='upper right', prop={'size':12})
ax.set_xlim(1,100)
xt = ax.get_xticks()
xt[0] = 1
ax.set_xticks(xt)
ax.set_xlabel('Reads number cut off')
ax.set_ylabel('Number of accessible protein coding genes')

plt.savefig('Mouse-Accessible-Genes.pdf')

