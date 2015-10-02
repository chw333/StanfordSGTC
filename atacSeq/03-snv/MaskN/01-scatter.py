import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import pylab as plt

fig = plt.figure()
df = pd.read_table('5a5b-Allele-Count')
df.columns = ['Chr', 'Pos', 'REF', 'ALT', 'unMask_REF_5a', 'unMask_ALT_5a','Mask_REF_5a', 'Mask_ALT_5a', 'unMask_REF_5b', 'unMask_ALT_5b','Mask_REF_5b', 'Mask_ALT_5b']

dfx = df.ix[(df.unMask_REF_5a >= 5) & (df.unMask_ALT_5a >= 5),]
dfx.unMask_REF_5a = np.log2(dfx.unMask_REF_5a)
dfx.unMask_ALT_5a = np.log2(dfx.unMask_ALT_5a)

ax = dfx.plot(kind='scatter', x='unMask_REF_5a', y='unMask_ALT_5a', color='blue', edgecolor='blue')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xym = max(xlim[1], ylim[1])
xym = 11
ax.set_xlim(0, xym)
ax.set_ylim(0, xym)
ax.plot([0,xym],[0, xym])
ax.set_title('Allele specific reads number(log2), p-value < 2.2e-16')

plt.savefig('Scatter-unMask5a.pdf')


dfx = df.ix[(df.Mask_REF_5a >= 5) & (df.Mask_ALT_5a >= 5),]
dfx.Mask_REF_5a = np.log2(dfx.Mask_REF_5a)
dfx.Mask_ALT_5a = np.log2(dfx.Mask_ALT_5a)

ax = dfx.plot(kind='scatter', x='Mask_REF_5a', y='Mask_ALT_5a', color='blue', edgecolor='blue')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xym = max(xlim[1], ylim[1])
xym = 11
ax.set_xlim(0, xym)
ax.set_ylim(0, xym)
ax.plot([0,xym],[0, xym])
ax.set_title('Allele specific reads number(log2), p-value = 0.38')
plt.savefig('Scatter-Mask5a.pdf')


fig = plt.figure()
dfx = df.ix[(df.unMask_REF_5b >= 5) & (df.unMask_ALT_5b >= 5),]
dfx.unMask_REF_5b = np.log2(dfx.unMask_REF_5b)
dfx.unMask_ALT_5b = np.log2(dfx.unMask_ALT_5b)

ax = dfx.plot(kind='scatter', x='unMask_REF_5b', y='unMask_ALT_5b', color='blue', edgecolor='blue')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xym = max(xlim[1], ylim[1])
xym = 11
ax.set_xlim(0, xym)
ax.set_ylim(0, xym)
ax.plot([0,xym],[0, xym])
ax.set_title('Allele specific reads number(log2), p-value < 2.2e-16')

plt.savefig('Scatter-unMask5b.pdf')

dfx = df.ix[(df.Mask_REF_5b >= 5) & (df.Mask_ALT_5b >= 5),]
dfx.Mask_REF_5b = np.log2(dfx.Mask_REF_5b)
dfx.Mask_ALT_5b = np.log2(dfx.Mask_ALT_5b)

ax = dfx.plot(kind='scatter', x='Mask_REF_5b', y='Mask_ALT_5b', color='blue', edgecolor='blue')
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xym = max(xlim[1], ylim[1])
xym = 11
ax.set_xlim(0, xym)
ax.set_ylim(0, xym)
ax.plot([0,xym],[0, xym])
ax.set_title('Allele specific reads number(log2), p-value = 0.58')
plt.savefig('Scatter-Mask5b.pdf')
