def specificEffect(inF):
    D = {}
    inFile = open(inF)
    ouFile1 = open(inF + '-ProteinLightSpecific', 'w')
    ouFile2 = open(inF + '-RNASpecific', 'w')
    L1 = []
    L2 = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        marker = fields[0]
        gene = fields[-1].split(':')[0]
        k = marker + '-' + gene
        D.setdefault(k, [])
        D[k].append(fields)
    for k in D:
        if len(D[k]) == 1:
            if D[k][0][-1][-4:] == ':RNA':
                L1.append(D[k][0])
            elif D[k][0][-1][-13:] == ':ProteinLight':
                L2.append(D[k][0])
    L1.sort(cmp = lambda x,y :cmp(float(x[-2]), float(y[-2])))
    L2.sort(cmp = lambda x,y :cmp(float(x[-2]), float(y[-2])))
    for x in L1:
        ouFile2.write('\t'.join(x) + '\n')
    for x in L2:
        ouFile1.write('\t'.join(x) + '\n')
    inFile.close()
    ouFile1.close()
    ouFile2.close()


specificEffect('Yeast-Single-Trait-Merged')
