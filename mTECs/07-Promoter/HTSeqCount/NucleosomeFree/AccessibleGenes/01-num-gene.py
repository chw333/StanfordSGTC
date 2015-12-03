def NumGene(inF):
    ouFile = open('mTECs-Gene-Promoter-AccessibleNum_TotalIsoform', 'w')
    inFile = open(inF)
    head = inFile.readline().strip().split('\t')
    Sample = head[4:12]
    ouFile.write('CutOff\t' + '\t'.join(Sample) + '\n')
    inFile.close()

    for CutOff in range(1,101):
        D = {}
        inFile = open(inF)
        head = inFile.readline().strip().split('\t')
        Sample = head[4:12]
        for s in Sample:
            D.setdefault(s, set())
    
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            for x in range(len(fields[4:])):
                if float(fields[x+4]) >= CutOff:
                    k = '\t'.join(fields[0:4])
                    D[Sample[x]].add(k)
        inFile.close()
        L = []
        for s in Sample:
            L.append(str(len(D[s])))
        ouFile.write(str(CutOff) + '\t'+'\t'.join(L) + '\n')
    ouFile.close()

NumGene('Mouse_Gene_Promoter_Cov')
