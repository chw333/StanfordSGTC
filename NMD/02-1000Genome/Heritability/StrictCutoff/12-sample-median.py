import numpy
D = {}
inFile = open('G462-Sample-Stopgain-Exon-Escape-Exp')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[4] == 'F':
        D[fields[0]] = fields[5]
inFile.close()

def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Sample', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        for item in fields[1:]:
            snp = item.split(':')[0]
            val = float(item.split('#')[-1])
            if snp in D:
                L.append(val)
        #if len(L) >= 2:
        if L:
            L.sort()
            LF = []
            for item in L:
                if item <= 1:
                    LF.append(0)
                else:
                    LF.append(1)
            if 0 not in LF or 1 not in LF:
                med = numpy.median(L)
                ouFile.write(sample + '\t' + str(med) + '\n')
            else:
                print(sample)


    inFile.close()
    ouFile.close()

def median2(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Sample2', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        for item in fields[1:]:
            snp = item.split(':')[0]
            val = float(item.split('#')[-1])
            if snp in D:
                L.append(val)
        if len(L) >= 2:
            L.sort()
            LF = []
            for item in L:
                if item <= 1:
                    LF.append(0)
                else:
                    LF.append(1)
            if 0 not in LF or 1 not in LF:
                med = numpy.median(L)
                ouFile.write(sample + '\t' + str(med) + '\n')
            else:
                print(sample)


    inFile.close()
    ouFile.close()


median2('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Filtered-Median')
