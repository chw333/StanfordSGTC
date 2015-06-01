def stopgain(inF1, inF2):
    D = {}
    inFile = open(inF1)
    ouFile = open(inF1 + '.NonSynonymous', 'w')
    ouFile2 = open(inF1 + '.NonSynonymous.unmapped', 'w')
    head = inFile.readline()
    ouFile.write(head)
    for line in inFile:
        line = line.strip()
        fields = line.split()
        gene = fields[0]
        D.setdefault(gene, [])
        D[gene].append(line)
    inFile.close()

    G = []
    inFile = open(inF2)
    hd = inFile.readline()
    for line in inFile:
        fields = line.split('\t')
        gene = fields[0]
        if gene not in G:
            G.append(gene)
    inFile.close()

    UG = []
    for g in G:
        if g in D:
            ouFile.write('\n'.join(D[g]) + '\n')
        else:
            ouFile2.write(g + '\n')
            UG.append(g)
    ouFile.close()
    ouFile2.close()

    inFile = open(inF2)
    ouFile1 = open(inF2 + '-mapped', 'w')
    ouFile2 = open(inF2 + '-unmapped', 'w')
    head = inFile.readline()
    ouFile1.write(head)
    ouFile2.write(head)
    for line in inFile:
        fields = line.split('\t')
        gene = fields[0]
        if gene in UG:
            ouFile2.write(line)
        else:
            ouFile1.write(line)

    inFile.close()
    ouFile1.close()
    ouFile2.close()

stopgain('GD462.GeneQuantRPKM.50FN.samplename.resk10.expression','GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-nonSynonymous-formated-sorted')
