def seq(inF):
    D = {}
    F = '../' + inF.split('.fa')[0]
    inFile = open(F)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = fields[9]
    inFile.close()

    inFile = open(inF)
    ouFile = open(inF + '.seq', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ouFile.write(fields[0] + '\t' + D[fields[0]] + '\t' + '\t'.join(fields[1:])+ '\n')
    inFile.close()
    ouFile.close()
#seq('SRR1258470-soft-filtered.fa.blated.filtered')
seq('SRR1258471-soft-filtered.fa.blated.filtered')
