def combine(inF1, inF2, ouF):
    D = {}
    inFile = open(inF1)
    head1 = inFile.readline().strip()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = '\t'.join(['%.2f'%float(x) for x in fields[1:]])
    inFile.close()
    inFile = open(inF2)
    ouFile = open(ouF, 'w')
    head2 = inFile.readline().strip()
    ouFile.write('Gene\t' + head2 + '\t' + head1 + '\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ouFile.write(line + '\t' + D[fields[0]] + '\n')
    inFile.close()
    ouFile.close()

combine('Tspan8_Negative_MHCII_Low_vs_Other-Counts-Normalized.txt', 'Tspan8_Negative_MHCII_Low_vs_Other_sig.txt', 'Tspan8_Negative_MHCII_Low_vs_Other_sig.exp')
combine('Tspan8_Negative_MHCII_Low_vs_Other-Counts-raw.txt', 'Tspan8_Negative_MHCII_Low_vs_Other_sig.txt', 'Tspan8_Negative_MHCII_Low_vs_Other_sig.raw.exp')
