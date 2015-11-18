import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import pylab as plt

df = pd.read_table('mTECs-Sig-Stats')
df2 = pd.DataFrame(data=[df.ix[:,2],df.ix[:,3]])
df2 = df2.T
df2 = np.log2(df2)
df2=df2.replace(-np.inf,0)
df2.columns = ['High > Low or Positive > Negative','High < Low or Positive < Negative']

fig = plt.figure()
ax = fig.add_axes([0.07,0.12,0.91,0.85])
df2.plot(kind='bar',ax=ax)
ax.set_xticklabels(['Tspan8 Positive\nMHCII\nHigh vs Low','Tspan8 Negative\nMHCII\nHigh vs Low','MHCII High\nTspan8\nPositive vs Negative','MHCII Low\nTspan8\nPositive vs Negative'], rotation=0)
ax.set_ylabel('Number of significant promoter regions (log2)')
ax.legend(loc='upper center')
ax.set_ylim(0,15)
plt.savefig('mTECs-Sig-Promoter.pdf')
