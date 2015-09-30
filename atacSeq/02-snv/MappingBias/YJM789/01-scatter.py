import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import pylab as plt

fig = plt.figure()
df = pd.read_table('5a.flt.bias', header=None)
df.columns = ['SNV', 'REF','ALT']
df.REF = df.REF[df.REF >= 5]
df.ALT = df.ALT[df.ALT >= 5]
df.REF = np.log2(df.REF)
df.ALT = np.log2(df.ALT)

ax = df.plot(kind='scatter', x='REF', y='ALT', color='blue', edgecolor='blue')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xym = max(xlim[1], ylim[1])
ax.set_xlim(0, xym)
ax.set_ylim(0, xym)
ax.plot([0,xym],[0, xym])

plt.savefig('Scatter-5a.pdf')


fig = plt.figure()
df = pd.read_table('5b.flt.bias', header=None)
df.columns = ['SNV', 'REF','ALT']
df.REF = df.REF[df.REF >= 5]
df.ALT = df.ALT[df.ALT >= 5]
df.REF = np.log2(df.REF)
df.ALT = np.log2(df.ALT)

ax = df.plot(kind='scatter', x='REF', y='ALT', color='blue', edgecolor='blue')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xym = max(xlim[1], ylim[1])
ax.set_xlim(0, xym)
ax.set_ylim(0, xym)
ax.plot([0,xym],[0, xym])

plt.savefig('Scatter-5b.pdf')



