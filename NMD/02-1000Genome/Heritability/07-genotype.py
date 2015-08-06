D = {}
inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Geno')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0] + '\t' + fields[1]
    D[k] = fields[2]
inFile.close()


def geno(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Genotype', 'w')

    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        num = fields[1]
        LS = []
        for item in fields[2:]:
            L = []
            im = item.split('|')[0]
            snp = im.split(':')[0]
            k = sample + '\t' + snp
            if D[k] == '0|1' or D[k] == '1|0':
                L.append(im + ':' + D[k])

                for im in item.split('|')[1:]:
                    snp = im.split(':')[0]
                    k = sample + '\t' + snp
                    if D[k] == '0|1' or D[k] == '1|0':
                        L.append(im + ':' + D[k])
            if L:
                LS.append('+'.join(L))
        ouFile.write(sample + '\t' + str(len(LS)) + '\t' + '\t'.join(LS) + '\n')

    inFile.close()
    ouFile.close()

geno('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample')


