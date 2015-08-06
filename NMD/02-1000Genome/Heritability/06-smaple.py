def sample(inF1, inF2):
    D = {}
    ouFile = open(inF2 + '-Sample', 'w')
    inFile = open(inF2)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        stop = fields[0].split(':')[0]
        D[stop] = '|'.join(fields)
    inFile.close()

    inFile = open(inF1)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L = fields[0:2]
        for stop in fields[2:]:
            L.append(D[stop])
        ouFile.write('\t'.join(L) + '\n')

    inFile.close()
    ouFile.close()

sample('G462-Sample-Stopgain', 'G462-Sample-Stopgain-Linkage-TranscriptLevel')
