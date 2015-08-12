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
    ouFile = open(inF + '-Sum', 'w')
    ouFile.write('Sample\tNMD\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        for item in fields[2:]:
            snp = item.split(':')[0].split('#')[1]
            val = item.split('#')[-1].split(':')
            #if snp in D:
            L.append([int(val[0]), int(val[1])])
        if L:
            s0 = 0
            s1 = 0
            for item in L:
                s0 += item[0]
                s1 += item[1]
            if s0 >0 and s1 >0:
                ouFile.write(sample + '\t' + str(float(s1)/float(s0)) + '\n')


    inFile.close()
    ouFile.close()


median('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-SumSNV')
