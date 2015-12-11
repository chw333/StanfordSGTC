# coding: utf-8
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd
import numpy as np
import pylab as plt
df = pd.read_table('Tspan8_negative_MHCII_HighLow-Counts-Normalized.txt')
x = (df.ix[:,1]+df.ix[:,2])/2
y = (df.ix[:,3] + df.ix[:,4])/2
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.scatter(np.log2(x),np.log2(y),color='b', edgecolor='b')


df = pd.read_table('Tspan8_negative_MHCII_HighLow_sig_exp')
x = (df.ix[:,7]+df.ix[:,8])/2
y = (df.ix[:,9]+df.ix[:,10])/2
ax.scatter(np.log2(x),np.log2(y), color='r', edgecolor='r')
ax.set_xlim(0,12)
ax.set_ylim(0,12)
ax.set_xlabel('Tspan8_negative_MHCII_High (log2)')
ax.set_ylabel('Tspan8_negative_MHCII_Low (log2)')
plt.savefig('Tspan8_negative_MHCII_HighLow.pdf')
