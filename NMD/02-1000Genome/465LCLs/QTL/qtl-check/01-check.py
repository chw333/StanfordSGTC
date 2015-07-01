def check(inF, inF2):
    ouFile = open(inF + '_genotype', 'w')
    D = {}
    L = []
    S = []
    inFile = open(inF)
    for n in range(20):
        line = inFile.readline().strip()
        fields = line.split()
        k = 'snp_' + fields[0][3:] + '_' + fields[1]
        D[k] = 1
        S.append(k)

    inFile.close()
    inFile = open(inF2)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[0]
        if snp in D:
            L.append(fields)
    inFile.close()
    L.sort(cmp = lambda x,y:cmp(S.index(x[0]), S.index(y[0])))
    for item in L:
        ouFile.write('\t'.join(item) + '\n')
    ouFile.close()

check('snp_6_31124849', '1000Genome-462LCLs-Genotype-Trans')


