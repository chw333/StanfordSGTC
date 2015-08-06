def exp(inF):
    inFile = open(inF)
    ouFile = open(inF + 'ressed', 'w')
    D = {}
    for line in inFile:
        LS = []
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        for item in fields[2:]:
            ims = item.split('+')
            L = [ims[0]]
            for im in ims[1:]:
                if im[-6:] != ':-1:-1':
                    L.append(im)
            if len(L) > 1 or L[0][-6:] != ':-1:-1':
                LS.append('+'.join(L))
        D[sample] = LS
    d = D.items()
    d.sort(cmp = lambda x,y :cmp(len(x[1]), len(y[1])), reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) + '\t' + '\t'.join(item[1]) + '\n')

    inFile.close()
    ouFile.close()

exp('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Exp')
