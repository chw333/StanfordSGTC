def bed(inF):
    ouFile = open(inF + '.bed', 'w')
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[4]
        pos = fields[5]
        k = ch + '\t' + pos
        D[k] = 1
    inFile.close()

    for k in D:
        fds = k.split()
        ouFile.write(fds[0] + '\t' + fds[1] + '\t' + fds[1] + '\n')
    ouFile.close()

bed('RSV-Stopgain-SNV')
