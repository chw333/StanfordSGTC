def merge(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '-Merged', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if len(fields) == 6:
            ch = fields[1]
            gene = fields[-1]
            D.setdefault(gene, {})
            D[gene].setdefault(ch, [])
            D[gene][ch].append(fields)
    inFile.close()

    LS = []
    for gene in D:
        for ch in D[gene]:
            L = D[gene][ch]
            L.sort(cmp = lambda x,y:cmp(float(x[-2]),float(y[-2])))
            #ouFile.write('\t'.join(L[0]) + '\n')
            LS.append(L[0])

    LS.sort(cmp = lambda x,y:cmp(float(x[-2]),float(y[-2])))
    for x in LS:
        ouFile.write('\t'.join(x) + '\n')
    ouFile.close()

merge('Yeast-Single-Trait')
merge('Yeast-RNA-ProteinLight-CommonEffect-Sig-noCov')
#merge('Yeast-RNA-ProteinLight-AnyEffect-Sig-noCov')
merge('Yeast-RNA-ProteinLightHeavy-CommonEffect-Sig-noCov')
#merge('Yeast-RNA-ProteinLightHeavy-AnyEffect-Sig-noCov')
