EX = ['HG00237', 'NA07000', 'HG00107']
def num(inF1, inF2, inF3):
    ouFile = open('G462-Sample-Stopgain-Num', 'w')
    D = {}
    inFile = open(inF1)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        n = int(fields[1])
        if sample not in EX:
            D.setdefault(sample, [n, -1, -1])
    inFile.close()

    inFile = open(inF2)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        n = int(fields[1])
        if sample not in EX:
            D[sample][1] = n
    inFile.close()

    inFile = open(inF3)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        n = int(fields[1])
        if sample not in EX:
            D[sample][2] = n
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y: cmp(x[1][0], y[1][0]))
    #d.sort(cmp = lambda x,y: cmp(x[1][2], y[1][2]))
    for item in d:
        ouFile.write(item[0] + '\t' + '\t'.join([str(x) for x in item[1]]) + '\n')

    ouFile.close()


num('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample', 'G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype', 'G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed')
