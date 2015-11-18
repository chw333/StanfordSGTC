def matrix(inF):
    L = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L += fields[7:]
    inFile.close()
    L = list(set(L))
    L.sort()

    inFile = open(inF)
    ouFile = open(inF + '.matrix', 'w')
    head = 'gene\tbaseMean\tlog2FoldChange\tlfcSE\tstat\tpvalue\tpadj'
    ouFile.write(head + '\t' + '\t'.join(L) + '\n')
    for line in inFile:
        LX = []
        line = line.strip()
        fields = line.split('\t')
        TF = fields[7:]
        for item in L:
            if item in TF:
                LX.append('1')
            else:
                LX.append('0')
        ouFile.write('\t'.join(fields[0:7]) + '\t' + '\t'.join(LX) + '\n')
    inFile.close()
    ouFile.close()



matrix('MHCII_low_Tspan8_PositiveNegative_sig.Feature.Annot')
matrix('Tspan8_negative_MHCII_HighLow_sig.Feature.Annot')


