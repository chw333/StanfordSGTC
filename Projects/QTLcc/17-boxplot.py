import matplotlib
matplotlib.use('Agg')
import pylab as pl
import scipy as sp
import random
def readData(marker, gene):
    geno = sp.loadtxt('Yeast-Genotype-Formated',dtype='str')
    genoT = geno.T
    for item in genoT:
        if item[0] == marker:
            genotype = item[1:]

    pheno = sp.loadtxt('Yeast-Phenotype-Formated',dtype='str')
    phenoT = pheno.T

    phenotype_RNA = []
    phenotype_PL = []
    phenotype_PH = []
    for item in phenoT:
        if item[0] == gene + ':' + 'RNA':
            phenotype_RNA = item[1:]
    for item in phenoT:
        if item[0] == gene + ':' + 'ProteinLight':
            phenotype_PL = item[1:]
    for item in phenoT:
        if item[0] == gene + ':' + 'ProteinHeavy':
            phenotype_PH = item[1:]
    return([genotype, phenotype_RNA, phenotype_PL, phenotype_PH])

def splitSample(data):
    geno = data[0]
    pheno_RNA = data[1]
    pheno_PL = data[2]
    pheno_PH = data[3]
    if len(geno):
        pheno_RNA_0 = []
        pheno_RNA_1 = []
        pheno_PL_0 = []
        pheno_PL_1 = []
        pheno_PH_0 = []
        pheno_PH_1 = []

        if len(pheno_RNA):
            for i in range(len(geno)):
                if geno[i] == '0' and pheno_RNA[i] != 'NA':
                    pheno_RNA_0.append(float(pheno_RNA[i]))
                if geno[i] == '1' and pheno_RNA[i] != 'NA':
                    pheno_RNA_1.append(float(pheno_RNA[i]))

        if len(pheno_PL):
            for i in range(len(geno)):
                if geno[i] == '0' and pheno_PL[i] != 'NA':
                    pheno_PL_0.append(float(pheno_PL[i]))
                if geno[i] == '1' and pheno_PL[i] != 'NA':
                    pheno_PL_1.append(float(pheno_PL[i]))


        if len(pheno_PH):
            for i in range(len(geno)):
                if geno[i] == '0' and pheno_PH[i] != 'NA':
                    pheno_PH_0.append(float(pheno_PH[i]))
                if geno[i] == '1' and pheno_PH[i] != 'NA':
                    pheno_PH_1.append(float(pheno_PH[i]))
        return ([pheno_RNA_0, pheno_RNA_1, pheno_PL_0, pheno_PL_1, pheno_PH_0, pheno_PH_1])


     
def boxplot(marker, gene):
    title = marker + ':' + gene
    rd = readData(marker, gene)
    data = splitSample(rd)
    group = ['Genotype:0', 'Genotype:1']

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
    #pl.plot(X3,data[2],'g.')
    #pl.plot(X4,data[3],'g.')
    ax.set_xticklabels(['']+group+[''])
    ax.set_ylabel('RNA Expression')
    ax.set_title(title)
    pl.savefig('Yeast-QTL-boxplot-RNA-%s-%s.pdf'%(marker,gene))

    fig = pl.figure()
    ax = fig.add_subplot(111)
    #pl.boxplot([data[0], data[1]])
    pl.boxplot([data[2], data[3]])
    #X1 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[0]))]
    #X2 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[1]))]
    X3 = [x/10000.0+1 for x in random.sample(range(-500,500),len(data[2]))]
    X4 = [x/10000.0+2 for x in random.sample(range(-500,500),len(data[3]))]
    ax.set_xlim(0,3)
    ax.set_xticks(range(4))
    #pl.plot(X3,data[0],'r.')
    #pl.plot(X4,data[1],'r.')
    pl.plot(X3,data[2],'g.')
    pl.plot(X4,data[3],'g.')
    ax.set_xticklabels(['']+group+[''])
    ax.set_ylabel('Protein Expression')
    ax.set_title(title)
    pl.savefig('Yeast-QTL-boxplot-Protein-%s-%s.pdf'%(marker,gene))


#common
boxplot('mrk_8844','YML126C')
#protein specific
boxplot('mrk_11043','YDL185W')
boxplot('mrk_7914','YKL006W')
#rna specific
boxplot('mrk_1896','YDL072C')
