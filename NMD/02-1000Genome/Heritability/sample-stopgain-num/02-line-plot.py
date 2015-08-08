import matplotlib
matplotlib.use('Agg')
def read_data(inF):
    inFile = open(inF)
    L1 = []
    L2 = []
    L3 = []
    for line in inFile:
        line = line.strip()
        fields = line.split()
        L1.append(int(fields[1]))
        L2.append(int(fields[2]))
        L3.append(int(fields[3]))
    inFile.close()
    return([L1, L2, L3])

data = read_data('G462-Sample-Stopgain-Num')
#group = ['Genotype', 'Phased', 'Phased and Expressed']
group = ['Genotype', 'Expressed']

import pylab as pl
import random
fig = pl.figure()
ax = fig.add_subplot(111)
pl.boxplot([data[0], data[2]])
X1 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[0]))]
X2 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[0]))]
#X3 = [x/10000.0+3 for x in random.sample(range(-500,500),len(data[0]))]
ax.set_ylim(0,100)
#ax.set_yticks(range(0,42,2))
pl.plot(X1,data[0],'g.')
pl.plot(X2,data[2],'g.')
#pl.plot(X3,data[2],'r.')
ax.set_xticklabels(group)
ax.set_ylabel('Number of Stopgain mutations per sample')
#ax.set_title('MmUbc')
pl.savefig('G462-Sample-Stopgain-Num.pdf')
    


