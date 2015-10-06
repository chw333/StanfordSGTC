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
    ouFile.write('Gene\tMock\tMERS\n')
    D = {}
    inFile = open(inF2)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        D.setdefault(gene, [])
        #mock = (float(fields[2]) + float(fields[3]))/2
        #rsv20h = (float(fields[14]) + float(fields[15]))/2
        Mock = np.median([float(fields[2]), float(fields[3]), float(fields[4])])
        MERS = np.median([float(fields[5]), float(fields[6]), float(fields[7])])
        D[gene].append([Mock,MERS])
    inFile.close()
    for g in G:
        if g in D:
            if len(D[g]) > 1:
                #print(D[g])
                pass
            ouFile.write(g + '\t' + str(D[g][0][0]) + '\t' + str(D[g][0][1]) + '\n')
    ouFile.close()

exp('UPF1SMG6SMG7-KnockDown-UP-Yepiskoposyan.etal', 'MERS_high_48h_geneCounts-Normalized.txt')

def plot(inF, ouF):
    df = pd.read_table(inF)
    dfx = df[(df.Mock > 20) & (df.MERS > 20)]
    dfx.MERS = np.log(dfx.MERS)
    dfx.Mock = np.log(dfx.Mock)
    fig = plt.figure()

    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    #ax.set_xlim(2,14)
    #ax.set_ylim(2,14)
    p = dfx.plot(kind='scatter', x='MERS', y='Mock', color='blue',edgecolor='blue', ax=ax)
    p.set_xlim(2,14)
    p.set_ylim(2,14)
    p.text(8, 13, 'p-value = 5.37e-12', va='center', ha='center', fontsize=14, color='r')
    p.plot([2,14],[2,14])
    plt.title('NMD substrates normalized expression (log2)')
    plt.savefig(ouF)


plot('UPF1SMG6SMG7-KnockDown-UP-Yepiskoposyan.etal.exp', 'MERS_high48h-NMD-Substrates-UPF1SMG6SMG7-KnockDown.pdf')





