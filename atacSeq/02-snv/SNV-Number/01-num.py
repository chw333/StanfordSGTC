def num(inF):
    n = 0
    inFile = open(inF)
    for line in inFile:
        if line[0:2] != '##':
            n += 1
    inFile.close()
    return n

a5=num('5a.flt.vcf')
b5=num('5b.flt.vcf')
S96a=num('S96a.flt.vcf')
S96b=num('S96b.flt.vcf')
YJM789a=num('YJM789a.flt.vcf')
YJM789b=num('YJM789b.flt.vcf')

print(a5)
print(b5)
print(S96a)
print(S96b)
print(YJM789a)
print(YJM789b)

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import pylab as plt
import numpy as np

#df = pd.DataFrame([np.log10(S96a), np.log10(S96b), np.log10(YJM789a), np.log10(YJM789b), np.log10(a5), np.log10(b5)], index=['S96a','S96b','YJM789a','YJM789b','a5','b5'])
df = pd.DataFrame([S96a, S96b, YJM789a, YJM789b, a5, b5], index=['S96a','S96b','YJM789a','YJM789b','a5','b5'])
ax = df.plot(kind='bar', legend=False, rot=1, logy=True)
ax.set_ylabel('Number of SNVs')
#x0, x1 = ax.get_xlim()
#ax.set_xlim(x0 -0.5, x1 + 0.25)
#x = ax.get_xticks()
#for container in ax.containers:
#    plt.setp(container, width=1)

#plt.axhline(0, color='k')
plt.savefig('SNV-Numer.pdf')



