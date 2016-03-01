import matplotlib
matplotlib.use('Agg')

import pylab as plt
MAX = 2000

Sample = ['Tspan8_negative_MHCII_low_rep1.NF.num', 'Tspan8_negative_MHCII_low_rep2.NF.num', 'Tspan8_negative_MHCII_high_rep1.NF.num', 'Tspan8_negative_MHCII_high_rep2.NF.num', 'Tspan8_positive_MHCII_low_rep1.NF.num', 'Tspan8_positive_MHCII_low_rep2.NF.num', 'Tspan8_positive_MHCII_high_rep1.NF.num', 'Tspan8_positive_MHCII_high_rep2.NF.num']

Sample2 = [' '.join(x.split('.')[0].split('_')[0:-1]) for x in Sample]

def LineColor(n):
    COLORS= ['r','b','g','m']
    if n in [0,2,4,6]:
        return(COLORS[n/2])
    elif n in [1,3,5,7]:
        return(COLORS[(n-1)/2])
    

TL = []
for S in Sample:
    L = []
    inFile = open(S)
    for line in inFile:
        line = line.strip()
        L.append(float(line))
    inFile.close()
    TL.append(L)

fig = plt.figure()
ax = fig.add_axes([0.15,0.1,0.8,0.8])
ax.set_xlim(1,MAX)
ax.set_xticks([0,500,1000,1500,2000])
ax.set_xticklabels([-1000,-500,0,500,1000])
ax.set_xlabel('Distance to TSS (bp)')
ax.set_ylabel('Number of reads')



AX = []
for i in range(8):
    AX.append(ax.plot(range(1,MAX+1), TL[i], color=LineColor(i)))
legAX = [AX[0][0], AX[2][0], AX[4][0], AX[6][0]]

ax.legend(legAX, [Sample2[0], Sample2[2], Sample2[4], Sample2[6]], loc='upper right', prop={'size':12})

plt.savefig('mTECs-TSS-raw.pdf')



