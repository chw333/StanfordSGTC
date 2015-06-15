import matplotlib
matplotlib.use('Agg')
import pylab as pl
import scipy as sp
import random

def boxplot(data, marker, gene):
    if len(data[2]) > 0:
        title = marker + ':' + gene
        group = ['0/0', '0/1', '1/1']
    
        fig = pl.figure()
        ax = fig.add_subplot(111)
        pl.boxplot([data[0], data[1]], data[2])
        #pl.boxplot([data[2], data[3]])
        X1 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[0]))]
        X2 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[1]))]
        X3 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[2]))]
        #X4 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[3]))]
        ax.set_xlim(0,4)
        ax.set_xticks(range(5))
        pl.plot(X1,data[0],'r.')
        pl.plot(X2,data[1],'r.')
        pl.plot(X3,data[2],'r.')
        #pl.plot(X4,data[3],'g.')
        ax.set_xticklabels(['']+group+[''])
        ax.set_ylabel('NMD Efficiency')
        ax.set_title(title)
        pl.savefig('NMD-QTL-boxplot-%s-%s.pdf'%(marker,gene))
    else:
        title = marker + ':' + gene
        group = ['0/0', '0/1']
    
        fig = pl.figure()
        ax = fig.add_subplot(111)
        pl.boxplot([data[0], data[1]])
        #pl.boxplot([data[2], data[3]])
        X1 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[0]))]
        X2 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[1]))]
        #X3 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[2]))]
        #X4 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[3]))]
        ax.set_xlim(0,3)
        ax.set_xticks(range(4))
        pl.plot(X1,data[0],'r.')
        pl.plot(X2,data[1],'r.')
        #pl.plot(X3,data[2],'r.')
        #pl.plot(X4,data[3],'g.')
        ax.set_xticklabels(['']+group+[''])
        ax.set_ylabel('NMD Efficiency')
        ax.set_title(title)
        pl.savefig('NMD-QTL-boxplot-%s-%s.pdf'%(marker,gene))


def geno(pos, snp):

    Sample = []
    inFile = open('1000Genome-462LCLs-Samples')
    for line in inFile:
        line = line.strip()
        Sample.append(line)


    D = {}
    ouFile = open('1000Genome-462LCLs-Genotype-' + pos, 'w')
    inFile = open('1000Genome-465LCLs-Genotype-FiltTrans-Ref')
    head = inFile.readline().strip().split('\t')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0].find('_'+pos) != -1:
            SNP = fields[0]
            for i in range(1, len(fields)):
                D[head[i]] = fields[i]
            break
    inFile.close()

    
    G = []
    for s in Sample:
        G.append(D[s])
    ouFile.write(SNP + '\t' + '\t'.join(G) + '\n')

    inFile = open('1000Genome-462LCLs-Phenotype-Trans')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == snp:
            P = fields[1:]
    inFile.close()

    L00 = []
    L01 = []
    L11 = []
    for i in range(len(G)):
        if G[i] == '0':
            if P[i] != 'nan': 
                L00.append(float(P[i]))
            
        if G[i] == '1':
            if P[i] != 'nan': 
                L01.append(float(P[i]))
        if G[i] == '2':
            if P[i] != 'nan': 
                L11.append(float(P[i]))
 

    data = [L00, L01, L11]
    boxplot(data,pos, snp)
    inFile.close()
    ouFile.close()

geno('6_31125705','snp_6_31124849')
