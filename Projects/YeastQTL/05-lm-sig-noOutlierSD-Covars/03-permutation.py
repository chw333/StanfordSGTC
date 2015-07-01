import os
import gzip
from PHENO import NAME

Fs = os.listdir('.')
def permutation(inF, pv, inD):
    D = {}
    inFile = open(inF)
    head = inFile.readline().strip().split('\t')
    pv_i = head.index(pv)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        phenotype = fields[0] + '-mean'
        position = fields[1]
        growth = fields[2]
        pv = float(fields[pv_i])
        k = growth + '-' + phenotype + '-' + position
        D.setdefault(k, [pv, []])
    inFile.close()

    for F in Fs:
        if F[-3:] == '.gz':
            f = gzip.open(F, 'rb')
            content = f.readlines()
            for item in content:
                fields = item.strip().split('\t')
                ind = int(fields[1])
                pv = fields[2]
                pos = fields[0]
                k = NAME[ind] + '-' + pos
                if k in D:
                    D[k][1].append(pv)
            f.close()

    ouFile = open(inF.split('.txt')[0] + '.WA.txt', 'w')
    inFile = open(inF)
    head = inFile.readline().strip()
    ouFile.write(head + '\tPermutation-pvalue-WA' + '\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        phenotype = fields[0] + '-mean'
        position = fields[1]
        growth = fields[2]
        pv = float(fields[pv_i])
        k = growth + '-' + phenotype + '-' + position

        pv2 = D[k][0]
        perm = D[k][1]
        if pv2 != pv:
            print('Error')
        else:
            perm.sort()
            n = 0
            N = 1000.0
            for x in perm:
                if x <= pv:
                    n += 1
            p = n/N
            ouFile.write(line + '\t' + str(p) + '\n')

    inFile.close()


    ouFile.close()





#permutation('Yeast-QTL-lm-Sig-0.001.txt', 'NA-untransformed-pvalue', '/mnt/larsix/projects/NMD/hansun/Projects/YeastQTL/03-linear-regression-noOutlierSD-Covars/GenotypeSA/Permutation')
permutation('Yeast-QTL-lm-Sig-0.001.permutation.NA.SA.txt', 'WA-untransformed-pvalue', '/mnt/larsix/projects/NMD/hansun/Projects/YeastQTL/03-linear-regression-noOutlierSD-Covars/GenotypeWA')

