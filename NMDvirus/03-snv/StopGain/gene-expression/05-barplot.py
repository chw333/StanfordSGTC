# coding: utf-8
import pandas as pd
import numpy as np
from scipy import stats
import pylab as plt
df = pd.read_table('geneCounts-RSV_M3-Normalized.checkGene-mc', header=None)
Mock = np.log2((df.ix[:,2]+df.ix[:,3])/2)
RSV = np.log2((df.ix[:,4]+df.ix[:,5])/2)
pv = stats.ttest_rel(Mock, RSV)[1]
print(pv)
df2 = pd.DataFrame(zip(Mock, RSV), columns=['Mock', 'RSV'])
fig = plt.figure()
ax = df2.plot(kind='box')
ax.set_ylabel('Normalized expression (log2)')
ax.set_title('Expression of stopgain genes (p-value=%.2f)'%pv)
plt.savefig('RSV-Exp.pdf')
