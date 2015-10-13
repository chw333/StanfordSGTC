# coding: utf-8
import pandas as pd
import numpy as np
from scipy import stats
import pylab as plt
df = pd.read_table('RSV2-Stopgain-SNV-ReadCount-Filtered', header=None)
Mock = (df.ix[:,3]+df.ix[:,4])/2
RSV = (df.ix[:,5]+df.ix[:,6])/2
pv = stats.ttest_rel(Mock, RSV)[1]
df2 = pd.DataFrame(zip(Mock, RSV), columns=['Mock', 'RSV'])
fig = plt.figure()
ax = df2.plot(kind='box')
ax.set_ylabel('Stopgain/Reference')
ax.set_title('Allele specfic expression of stopgain genes (p-value=%.2f)'%pv)
plt.savefig('RSV-ASE.pdf')
