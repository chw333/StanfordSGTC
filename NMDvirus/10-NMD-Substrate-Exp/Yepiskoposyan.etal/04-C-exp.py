import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import pylab as plt


def Gene(inF):
    G = {}
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        G[fields[5]] = 1
    inFile.close()
    return G

def exp(inF1,inF2):
    G = Gene(inF1)
    ouFile = open(inF1 + '.exp', 'w')
    ouFile.write('Gene\tMock\tHSV\n')
    D = {}
    inFile = open(inF2)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        D.setdefault(gene, [])
        #Mock = (float(fields[2]) + float(fields[3]))/2
        #HSV = (float(fields[4]) + float(fields[5]))/2
        Mock = np.median([float(fields[2]), float(fields[3])])
        HSV = np.median([float(fields[4]), float(fields[5])])
        D[gene].append([Mock, HSV])
    inFile.close()
    for g in G:
        if g in D:
            if len(D[g]) > 1:
                #print(D[g])
                pass
            ouFile.write(g + '\t' + str(D[g][0][0]) + '\t' + str(D[g][0][1]) + '\n')
    ouFile.close()

exp('UPF1SMG6SMG7-KnockDown-UP-Yepiskoposyan.etal', '/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HSV/geneCounts-HSV8h-Normalized.txt')

def plot(inF, ouF):
    df = pd.read_table(inF)
    dfx = df[(df.Mock > 20) & (df.HSV > 20)]
    dfx.HSV = np.log(dfx.HSV)
    dfx.Mock = np.log(dfx.Mock)
    fig = plt.figure()

    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    p = dfx.plot(kind='scatter', x='HSV', y='Mock', color='blue',edgecolor='blue', ax=ax)
    p.set_xlim(2,14)
    p.set_ylim(2,14)
    p.set_xlabel('HSV-1')
    p.text(8, 13, 'p-value = 0.42', va='center', ha='center', fontsize=14, color='r')
    p.plot([2,14],[2,14])
    plt.title('NMD substrates normalized expression (log2)')
    plt.savefig(ouF)


plot('UPF1SMG6SMG7-KnockDown-UP-Yepiskoposyan.etal.exp', 'HSV-NMD-Substrates-UPF1SMG6SMG7-KnockDown.pdf')





