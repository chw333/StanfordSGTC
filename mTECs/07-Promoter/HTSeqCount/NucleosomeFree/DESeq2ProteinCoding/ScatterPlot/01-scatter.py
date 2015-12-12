# coding: utf-8
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd
import numpy as np
import pylab as plt
df = pd.read_table('Tspan8_Negative_MHCII_Low_vs_Other-Counts-Normalized.txt')
y = (df.ix[:,1]+df.ix[:,2]+df.ix[:,3]+df.ix[:,4]+df.ix[:,5]+df.ix[:,6])/6
x = (df.ix[:,7] + df.ix[:,8])/2
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.scatter(np.log2(x),np.log2(y),color='b', edgecolor='b')


df = pd.read_table('Tspan8_Negative_MHCII_Low_vs_Other_sig_exp')
y = (df.ix[:,7]+df.ix[:,8]+df.ix[:,9]+df.ix[:,10]+df.ix[:,11]+df.ix[:,12])/6
x = (df.ix[:,13]+df.ix[:,14])/2
ax.scatter(np.log2(x),np.log2(y), color='r', edgecolor='r')
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.plot([0,10],[0,10], color='g', linestyle='--')
ax.set_xlabel('Tspan8_negative_MHCII_low (log2)')
ax.set_ylabel('Other samples (log2)')
plt.savefig('Tspan8_Negative_MHCII_Low_vs_Other.pdf')
