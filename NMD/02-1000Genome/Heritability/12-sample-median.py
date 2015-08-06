import numpy
def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Sample', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        for item in fields[2:]:
            val = float(item.split('#')[-1])
            L.append(val)
        L.sort()
        med = numpy.median(L)
        ouFile.write(sample + '\t' + str(med) + '\n')


    inFile.close()
    ouFile.close()

median('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Median')
