### exon level
def linkage():
    D = {}
    inFile = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-nonSynonymous')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        anno = fields[2].split(',')
        for an in anno:
            exon = ':'.join(an.split(':')[0:3])
            snp = fields[8]
            D.setdefault(exon, [])
            D[exon].append(snp+':'+an)
    inFile.close()

    inFile = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-synonymous')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        anno = fields[2].split(',')
        for an in anno:
            exon = ':'.join(an.split(':')[0:3])
            snp = fields[8]
            D.setdefault(exon, [])
            D[exon].append(snp+':'+an)
    inFile.close()


    inFile = open('G462-Sample-Stopgain-Linkage')
    ouFile = open('G462-Sample-Stopgain-Linkage-ExonLevel', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[0]
        anno = fields[1]
        exon = ':'.join(anno.split(':')[0:3])
        if exon in D:
            ouFile.write(line + '\t' + '\t'.join(D[exon]) + '\n')
        else:
            ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()


linkage()
