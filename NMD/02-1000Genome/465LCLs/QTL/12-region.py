def region(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '-region', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[-1]
        fdr = float(fields[-2])
        ch = fields[0]
        D.setdefault(snp, {})
        D[snp].setdefault(ch, [])
        D[snp][ch].append(fields)
    inFile.close()
    for snp in D:
        for ch in D[snp]:
            D[snp][ch].sort(cmp = lambda x,y:cmp(float(x[-2]), float(y[-2])))
            ouFile.write('\t'.join(D[snp][ch][0]) + '\n')

    ouFile.close()
region('Single-Trait-lm-Sig-fdr-sorted')
