import matplotlib
matplotlib.use('Agg')
def read_data(inF):
    inFile = open(inF)
    L1 = []
    L2 = []
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if fields[4] == 'F':
            L1.append(float(fields[5]))
        else:
            L2.append(float(fields[5]))
    inFile.close()
    return([L1, L2])

data = read_data('G462-Sample-Stopgain-Exon-Escape-Exp')

group = ['UnEscaped', 'Escaped']

import pylab as pl
import random
fig = pl.figure()
ax = fig.add_subplot(111)
pl.boxplot(data)
X1 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[0]))]
X2 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[1]))]
ax.set_ylim(0,2.5)
#ax.set_yticks(range(0,42,2))
pl.plot(X1,data[0],'g.')
pl.plot(X2,data[1],'b.')
ax.set_xticklabels(group)
#ax.set_ylabel('Ct')
#ax.set_title('MmUbc')
pl.savefig('StopGain-Rule55.pdf')
