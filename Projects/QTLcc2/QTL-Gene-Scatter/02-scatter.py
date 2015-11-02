import matplotlib 
matplotlib.use('Agg')
import pandas as pd
import pylab as plt

#chrM_Len = 85779.0
L1 = []
L2 = []
inFile = open('Yeast-Chr-Cummulate')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L1.append(fields[0][3:])
    L2.append(float(fields[1])/1000000)
inFile.close()
X = [0]*len(L1)
for i in range(len(L1)-1):
    X[i] = (L2[i] + L2[i+1])/2
#X[-1] = L2[-1] + (chrM_Len/1000000)/2

def scatter(inF):
    df = pd.read_table(inF, header=None)
    df.ix[:,0] = df.ix[:,0]/1000000
    df.ix[:,1] = df.ix[:,1]/1000000
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    df.plot(kind='scatter', ax= ax, x=0, y=1,color='g', edgecolor='g',s=60)
    ax.set_xlim(0,L2[-1])
    ax.set_ylim(0,L2[-1])
    ax.set_xlabel('QTL position (Mb)')
    ax.set_ylabel('Gene position (Mb)')
    ax.set_xticks(X)
    ax.set_xticklabels(L1[0:-1])
    ax.set_yticks(X)
    ax.set_yticklabels(L1[0:-1])
    plt.grid(False)
    plt.savefig(inF+'.pdf')
scatter('Yeast-RNA-ProteinLight-AnyEffect-Sig-noCov.pos')
scatter('Yeast-RNA-ProteinLight-CommonEffect-Sig-noCov.pos')
scatter('Yeast-RNA-ProteinLight-SpecificEffect-Sig-Cov.pos')
