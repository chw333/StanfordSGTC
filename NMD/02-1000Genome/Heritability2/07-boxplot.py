import matplotlib
matplotlib.use('Agg')
def read_data(inF):
    inFile = open(inF)
    L1 = []
    L2 = []
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if fields[1] == 'F':
            L1.append(float(fields[2]))
        else:
            L2.append(float(fields[2]))
    inFile.close()
    return([L1, L2])

data = read_data('G462-Sample-Stopgain-ASE-Escape-Filtered2-Ratio')
print(data)

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
pl.plot(X2,data[1],'g.')
ax.set_xticklabels(group)
ax.set_ylabel('NMD efficiency (No. mutated reads / No. reference reads)')
ax.set_title('p value = 0.00029')
pl.savefig('StopGain-Rule55-2.pdf')
