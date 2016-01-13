# coding: utf-8
import matplotlib
matplotlib.use('Agg')
import pylab as plt
import numpy as np
import pandas as pd

PEAK = pd.read_table('GM12878-NF-TSS-Peak', header=None)
ALL = pd.read_table('GM12878-LibrarySize-ALL',header=None)
NF = pd.read_table('GM12878-LibrarySize-NF',header=None)
Mono = pd.read_table('GM12878-LibrarySize-Mono',header=None)
Di = pd.read_table('GM12878-LibrarySize-Di',header=None)
Tri = pd.read_table('GM12878-LibrarySize-Tri',header=None)

DF = pd.DataFrame([PEAK[1], ALL[1], NF[1], Mono[1], Di[1], Tri[1]]).T
DF.columns=['TSS_Peak', 'ALL','NucleosomeFree','MonoNucleosome','DiNucleosomes','TriNucleosomes']
DF.index=ALL[0]
DF.index.name=None
DF2 = np.log2(DF)

fig = plt.figure()
ax = fig.add_axes([0.1,0.25,0.8,0.65])
DF2.plot(kind='bar',ax=ax, legend=False)
ax.set_ylabel('Number of reads (log2)')

patches, labels = ax.get_legend_handles_labels()
ax.legend(patches, labels, bbox_to_anchor=(0.5, 1), loc='center', ncol=2)
ax.set_xticklabels(DF.index, rotation=60, fontsize=6)
plt.grid(True)
plt.savefig('GM12878-LibrarySize.pdf')

print('PEAK/ALL')
norm = DF.TSS_Peak/DF.ALL
print(norm)
print(np.var(norm))


print('PEAK/NF')
norm = DF.TSS_Peak/DF.NucleosomeFree
print(norm)
print(np.var(norm))


print('PEAK/Mono')
norm = DF.TSS_Peak/DF.MonoNucleosome
print(norm)
print(np.var(norm))


print('PEAK/Di')
norm = DF.TSS_Peak/DF.DiNucleosomes
print(norm)
print(np.var(norm))


print('PEAK/Tri')
norm = DF.TSS_Peak/DF.TriNucleosomes
print(norm)
print(np.var(norm))
