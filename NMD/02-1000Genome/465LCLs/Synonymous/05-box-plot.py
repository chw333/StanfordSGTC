import matplotlib
matplotlib.use('Agg')
import pylab as pl
import random

def boxplot(inF):
    group = ['0/0', '0/1', '1/1'] 
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('\n')
        line2 = inFile.readline().strip('\n')
        line3 = inFile.readline().strip('\n')
        line4 = inFile.readline().strip('\n')
        if line1:
            fields = line1.split('\t')
            gene = fields[3]
            pos = fields[4].split(':')
            name = '_'.join([gene, pos[0], pos[1]]) 
            #print(name)
            print(gene)
            title = gene + ',' + pos[0] + ':' + pos[1] + ',' + fields[7] + '>' + fields[8] + ',' + fields[5]
            L0 = [float(x) for x in line2.split('\t') if x and x != '-1']
            L1 = [float(x) for x in line3.split('\t') if x and x != '-1']
            L2 = [float(x) for x in line4.split('\t') if x and x != '-1']
            data = [L0, L1, L2]
            
            fig = pl.figure()
            ax = fig.add_subplot(111)
            pl.boxplot(data)
            X1 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[0]))]
            X2 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[1]))]
            X3 = [x/10000.0+3 for x in random.sample(range(-500,500),len(data[2]))]
            #ax.set_ylim(0,40)
            #ax.set_yticks(range(0,42,2))
            pl.plot(X1,data[0],'g.')
            pl.plot(X2,data[1],'g.')
            pl.plot(X3,data[2],'g.')
            ax.set_xticklabels(group)
            ax.set_ylabel('RPKM')
            ax.set_title(title)
            pl.savefig(name + '.pdf')

        else:
            break
    inFile.close()

boxplot('1000Genome-GEUVADIS465-Stopgain-Genotype-mutationFreq-ExpressionAL50')
