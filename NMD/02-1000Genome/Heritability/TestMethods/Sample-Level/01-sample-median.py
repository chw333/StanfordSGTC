import numpy
D = {}
inFile = open('G462-Sample-Stopgain-Exon-Escape')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[4] == 'F':
        D[fields[0]] = fields[4]
inFile.close()

def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Median', 'w')
    ouFile.write('Sample\tNMD\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        for item in fields[2:]:
            snp = item.split(':')[0].split('#')[1]
            esc = item.split(':')[0].split('#')[0]

            val = float(item.split('#')[-1])
            if esc == 'unEscaped':
                L.append(val)
        if L:
            #L.sort()
            LF = []
            for item in L:
                if item <= 1:
                    LF.append(0)
                else:
                    LF.append(1)
            #if 0 not in LF or 1 not in LF:
            if LF.count(0) < 2 or LF.count(1) < 2:
                med = numpy.median(L)
                ouFile.write(sample + '\t' + str(med) + '\n')
            #else:
            #    print(sample)


    inFile.close()
    ouFile.close()


median('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-SumSNV')
