import numpy as np

def number(inF):
    D = {}
    ouFile1 = open(inF + '-SampleNumberTotal', 'w')
    ouFile2 = open(inF + '-SampleNumberHet', 'w')
    df = np.loadtxt(inF, dtype = 'str')
    for i in range(10, df.shape[1]):
        sample = df[0, i]
        num_total = list(df[1:,i]).count('1') + list(df[1:,i]).count('2')
        num_het = list(df[1:,i]).count('1')
        D[sample] = [num_total, num_het]
    d1 = D.items()
    d2 = D.items()
    d1.sort(cmp = lambda x,y : cmp(x[1][0], y[1][0]), reverse = True)
    d2.sort(cmp = lambda x,y : cmp(x[1][1], y[1][1]), reverse = True)

    for item in d1:
        ouFile1.write(item[0] + '\t' + str(item[1][0]) + '\n')

    for item in d2:
        ouFile2.write(item[0] + '\t' + str(item[1][1]) + '\n')

    ouFile1.close()
    ouFile2.close()

number('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated-sorted')


def gene_number(inF):
    D = {}
    ouFile1 = open(inF + '-SampleNumberTotalGene', 'w')
    ouFile2 = open(inF + '-SampleNumberHetGene', 'w')
    df = np.loadtxt(inF, dtype = 'str')
    for i in range(10, df.shape[1]):
        S1 = set()
        S2 = set()
        sample = df[0, i]
        for j,x in  enumerate(df[:,i]):
            gene = df[j,0]
            if x == '1' or x == '2':
                S1.add(gene)
            if x == '1':
                S2.add(gene)


        #num_total = list(df[1:,i]).count('1') + list(df[1:,i]).count('2')
        #num_het = list(df[1:,i]).count('1')
        D[sample] = [S1, S2]
    d1 = D.items()
    d2 = D.items()
    d1.sort(cmp = lambda x,y : cmp(len(x[1][0]), len(y[1][0])), reverse = True)
    d2.sort(cmp = lambda x,y : cmp(len(x[1][1]), len(y[1][1])), reverse = True)

    for item in d1:
        ouFile1.write(item[0] + '\t' + str(len(item[1][0])) + '\t' + '\t'.join(item[1][0]) + '\n')

    for item in d2:
        ouFile2.write(item[0] + '\t' + str(len(item[1][1])) + '\t' + '\t'.join(item[1][1]) + '\n')

    ouFile1.close()
    ouFile2.close()

gene_number('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated-sorted')

def snv_number(inF):
    D = {}
    ouFile1 = open(inF + '-SampleNumberTotalSNV', 'w')
    ouFile2 = open(inF + '-SampleNumberHetSNV', 'w')
    df = np.loadtxt(inF, dtype = 'str')
    for i in range(10, df.shape[1]):
        S1 = set()
        S2 = set()
        sample = df[0, i]
        for j,x in  enumerate(df[:,i]):
            snv = df[j,7]
            if x == '1' or x == '2':
                S1.add(snv)
            if x == '1':
                S2.add(snv)


        #num_total = list(df[1:,i]).count('1') + list(df[1:,i]).count('2')
        #num_het = list(df[1:,i]).count('1')
        D[sample] = [S1, S2]
    d1 = D.items()
    d2 = D.items()
    d1.sort(cmp = lambda x,y : cmp(len(x[1][0]), len(y[1][0])), reverse = True)
    d2.sort(cmp = lambda x,y : cmp(len(x[1][1]), len(y[1][1])), reverse = True)

    for item in d1:
        ouFile1.write(item[0] + '\t' + str(len(item[1][0])) + '\t' + '\t'.join(item[1][0]) + '\n')

    for item in d2:
        ouFile2.write(item[0] + '\t' + str(len(item[1][1])) + '\t' + '\t'.join(item[1][1]) + '\n')

    ouFile1.close()
    ouFile2.close()

snv_number('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated-sorted')
