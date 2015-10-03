def yjm(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.vcf')[0] + '.flted', 'w')
    for line in inFile:
        line = line.strip()
        if line[0] != '#':
            fields = line.split('\t')
            k = '\t'.join([fields[0], fields[1], fields[3], fields[4]])
            DP4 = fields[7].split('DP4=')[1].split(';')[0].split(',')
            DP4ref = int(DP4[0]) + int(DP4[1])
            DP4alt = int(DP4[2]) + int(DP4[3])
            if DP4ref <= 5 and DP4alt >= 20:
                ouFile.write(k + '\t' + str(DP4ref) + '\t' + str(DP4alt) + '\n')
    inFile.close()
    ouFile.close()

yjm('YJM789a.flt.vcf')
yjm('YJM789b.flt.vcf')

def intersection(inF1, inF2, ouF):
    ouFile = open(ouF, 'w')
    D = {}
    inFile = open(inF2)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = '\t'.join(fields[0:4])
        D[k] = fields[4:6]
    inFile.close()

    inFile = open(inF1)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = '\t'.join(fields[0:4])
        if k in D:
            ouFile.write(k + '\t' + fields[4] + '\t' + fields[5] + '\t' + str(D[k][0]) + '\t' + str(D[k][1]) + '\n')
    inFile.close()
    ouFile.close()


intersection('YJM789a.flt.flted', 'YJM789b.flt.flted', 'YJM789ab.flted')
