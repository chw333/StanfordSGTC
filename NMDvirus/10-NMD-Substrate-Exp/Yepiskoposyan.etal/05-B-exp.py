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
    ouFile.write('Gene\tMock\tHIV\n')
    D = {}
    inFile = open(inF2)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        D.setdefault(gene, [])
        #Mock = (float(fields[2]) + float(fields[3]) + float(fields[4]))/3
        #HIV = (float(fields[5]) + float(fields[6]) + float(fields[7]))/3
        Mock = np.median([float(fields[11]), float(fields[12])])
        HIV = np.median([float(fields[5]), float(fields[6]), float(fields[7])])
        D[gene].append([Mock, HIV])
    inFile.close()
    for g in G:
        if g in D:
            if len(D[g]) > 1:
                print(D[g])
            ouFile.write(g + '\t' + str(D[g][0][0]) + '\t' + str(D[g][0][1]) + '\n')
    ouFile.close()

exp('SMG7-KnockDown-UP-Yepiskoposyan.etal', '/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HIV-1/geneCounts-Normalized.txt')

def plot(inF, ouF):
    df = pd.read_table(inF)
    dfx = df[(df.Mock > 20) & (df.HIV > 20)]
    dfx.HIV = np.log(dfx.HIV)
    dfx.Mock = np.log(dfx.Mock)
    fig = plt.figure()

    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    #ax.set_xlim(2,14)
    #ax.set_ylim(2,14)
    p = dfx.plot(kind='scatter', x='HIV', y='Mock', color='blue',edgecolor='blue', ax=ax)
    p.set_xlabel('HIV-1')
    p.set_xlim(2,14)
    p.set_ylim(2,14)
    p.plot([2,14],[2,14])
    plt.title('NMD substrates normalized expression')
    plt.savefig(ouF)


plot('SMG7-KnockDown-UP-Yepiskoposyan.etal.exp', 'HIV-NMD-Substrates-SMG7-KnockDown.pdf')





