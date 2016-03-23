import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

L1 = []
L2 = []
L3 = []
L4 = []

M = 500

inFile = open('POGK-A01-coverage')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L1.append(int(fields[1]))
    if int(fields[2]) > M:
        L2.append(M)
    else:
        L2.append(int(fields[2]))
inFile.close()

inFile = open('POGK-B01-coverage')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L3.append(int(fields[1]))
    if int(fields[2]) > M:
        L4.append(M)
    else:
        L4.append(int(fields[2]))
inFile.close()


MIN = 166808681
MAX = 166823709
fig = plt.figure()
ax = fig.add_axes([0.1,0.6,0.8,0.38])
ax.set_xlim(MIN,MAX)
ax.set_ylim(min(L2),int(max(L2)*1.1))
ax.set_xticklabels([])
ax.set_ylabel('A01')
ax.plot(L1, L2,'r.')

ax = fig.add_axes([0.1,0.2,0.8,0.38])
ax.set_xlim(MIN,MAX)
ax.set_ylim(min(L4),int(max(L4)*1.1))
ax.set_xticklabels([])
ax.set_ylabel('B01')
ax.plot(L3, L4, 'b.')

ax = fig.add_axes([0.1,0.02,0.8,0.16])
ax.set_ylim(0,1)
ax.set_xlim(MIN,MAX)
ax.set_ylabel('POGK')
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_yticks([])
#ax.axes.get_yaxis().set_visible(False)
#ax.axes.get_xaxis().set_visible(False)

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]   

exon_start = '166808723,166810191,166815848,166816730,166818174,166821821,'.split(',')
exon_end = '166808841,166810325,166815975,166816829,166819660,166823709,'.split(',')
for i in range(len(exon_start)-1):
    exon = [(exon_start[i],0.3),(exon_start[i],0.7),(exon_end[i],0.7),(exon_end[i],0.3),(0,0)]
    path = Path(exon, codes)
    patch = patches.PathPatch(path, facecolor='green', lw=1)
    ax.add_patch(patch)

cds = [166810193,166819646]
ax.plot([cds[0],cds[0]],[0.3,0.7],'m-',linewidth=2)
ax.plot([cds[1],cds[1]],[0.3,0.7],'m-',linewidth=2)




#ax.text((105+581)/2.0,-0.25,'E6',horizontalalignment='center',verticalalignment='center',fontsize=6)

plt.savefig('POGK-Expression-Max.pdf')
