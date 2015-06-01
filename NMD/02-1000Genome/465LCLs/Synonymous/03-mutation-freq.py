def freq(inF):
    ouFile = open(inF + '-mutationFreq', 'w')
    D = {}
    inFile = open(inF)
    head = inFile.readline()
    ouFile.write('No.0\tNo.1\tNo.2\t' + head)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gn = fields[10:]
        mt = fields[1]
        D.setdefault(mt,[line])
        gn1 = gn.count('0')
        gn2 = gn.count('1')
        gn3 = gn.count('2')
        D[mt] += [gn1, gn2, gn3]
    inFile.close()
    d = D.items()
    d.sort(cmp = lambda x, y: cmp(x[1][2] + x[1][3], y[1][2] + y[1][3]), reverse=True)
    for item in d:
        ouFile.write('\t'.join([str(item[1][1]), str(item[1][2]), str(item[1][3]), item[1][0]]) + '\n')

    ouFile.close()
freq('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-synonymous-formated-sorted-mapped')
