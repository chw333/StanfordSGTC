import numpy
def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Median', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        num = fields[1]
        S = [sample, num]
        for item in fields[2:]:
            im = item.split('#')
            snp = im[0]
            L = []
            LS = []
            exp = im[1].split('_')
            for ex in exp:
                two = ex.split('%')
                if two[0] == '-1' and two[1] == '-1':
                    pass
                else:
                    L.append(two)
            for item in L:
                LS.append((float(item[1]) + 1)/(float(item[0]) + 1))
            LS.sort()
            m = numpy.median(LS)
            S.append(snp + '#' + str(m))
        ouFile.write('\t'.join(S) + '\n')




    inFile.close()
    ouFile.close()

median('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
