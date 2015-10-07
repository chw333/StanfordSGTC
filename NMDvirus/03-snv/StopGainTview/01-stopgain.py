def stopgain(inF, inF2):
    ouFile = open(inF + '-formated', 'w')
    G = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if int(fields[1]) >= 2:
            G[fields[0]] = 0
    inFile.close()
    inFile = open(inF2)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[1] in G and G[fields[1]] == 0:
            ouFile.write('\t'.join(fields[1:2] + fields[3:10]) + '\n')
            G[fields[1]] = 1

    inFile.close()
    ouFile.close()

stopgain('RSV2-Stopgain-SNV-het-gene', 'RSV2-Stopgain-SNV')
stopgain('RSV2-Stopgain-SNV-hom-gene', 'RSV2-Stopgain-SNV')
stopgain('RSV-Stopgain-SNV-hom-gene', 'RSV-Stopgain-SNV')
stopgain('RSV-Stopgain-SNV-het-gene', 'RSV-Stopgain-SNV')
