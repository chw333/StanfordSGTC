import matplotlib 
matplotlib.use('Agg')
import pylab as plt
import numpy as np
MAX = 2000


Sample = ['GM12878_50k_Rep1_NF.num','GM12878_50k_Rep2_NF.num','GM12878_50k_Rep3_NF.num','GM12878_50k_Rep4_NF.num']

Sample2 = [' '.join(x.split('.')[0].split('_')[0:-1]) for x in Sample]

def LineColor(n):
    COLORS= ['r','b','g','m']
    return(COLORS[n])

def GetSampleSize(s):
    SampleSizeMedian = []
    SampleSize = {}
    inFile = open('GM12878-LibrarySize-ALL')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        SampleSize[fields[0]] = int(fields[1])
        SampleSizeMedian.append(int(fields[1]))
    inFile.close()
    return [SampleSize[s],np.median(SampleSizeMedian)]

    

TL = []
for S in Sample:
    L = []
    inFile = open(S)
    for line in inFile:
        line = line.strip()
        ss = GetSampleSize('_'.join(S.split('.')[0].split('_')[0:-1]))
        #### time sample size median
        ##L.append(float(line)/ss[0]*ss[1])
        #### per Million
        L.append(float(line)/ss[0]*1000000)
    inFile.close()
    TL.append(L)

fig = plt.figure()
ax = fig.add_axes([0.15,0.1,0.8,0.8])
ax.set_xlim(1,MAX)
ax.set_xticks([0,500,1000,1500,2000])
ax.set_xticklabels([-1000,-500,0,500,1000])
ax.set_xlabel('Distance to TSS (bp)')
ax.set_ylabel('Cumulative coverage per million reads')



AX = []
for i in range(4):
    AX.append(ax.plot(range(1,MAX+1), TL[i], color=LineColor(i)))
legAX = [AX[0][0], AX[1][0], AX[2][0], AX[3][0]]

ax.legend(legAX, [Sample2[0], Sample2[1], Sample2[2], Sample2[3]], loc='upper right', prop={'size':12})

plt.savefig('GM12878-TSS-norm-ALL.pdf')



