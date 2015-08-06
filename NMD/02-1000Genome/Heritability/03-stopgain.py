def stopgain(inF):
    ouFile = open('G462-Sample-Stopgain-Linkage', 'w')
    D = {}
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        fields = line.split('\t')
        snp = fields[7]
        anno = fields[6].split(',')[0]
        D[snp] = anno
    inFile.close()

    for k in D:
        ouFile.write(k + '\t' + D[k] + '\n')
    ouFile.close()


stopgain('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated-sorted')
