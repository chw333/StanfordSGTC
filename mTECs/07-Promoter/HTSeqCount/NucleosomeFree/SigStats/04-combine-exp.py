def combine(inF1, inF2):
    D = {}
    inFile = open(inF1)
    head1 = inFile.readline().strip()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = '\t'.join(['%.2f'%float(x) for x in fields[1:]])
    inFile.close()
    inFile = open(inF2)
    ouFile = open(inF2.split('.txt')[0] + '_exp', 'w')
    head2 = inFile.readline().strip()
    ouFile.write('Gene\t' + head2 + '\t' + head1 + '\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ouFile.write(line + '\t' + D[fields[0]] + '\n')
    inFile.close()
    ouFile.close()

combine('MHCII_HighLow_Tspan8_PositiveNegative-Counts-Normalized.txt', 'MHCII_HighLow_Tspan8_PositiveNegative_sig.txt')
combine('MHCII_high_Tspan8_PositiveNegative-Counts-Normalized.txt', 'MHCII_high_Tspan8_PositiveNegative_sig.txt')
combine('MHCII_low_Tspan8_PositiveNegative-Counts-Normalized.txt', 'MHCII_low_Tspan8_PositiveNegative_sig.txt')
combine('Tspan8_negative_MHCII_HighLow-Counts-Normalized.txt', 'Tspan8_negative_MHCII_HighLow_sig.txt')
combine('Tspan8_positive_MHCII_HighLow-Counts-Normalized.txt', 'Tspan8_positive_MHCII_HighLow_sig.txt')
combine('Tspan8_PositiveNegative_MHCII_HighLow-Counts-Normalized.txt',  'Tspan8_PositiveNegative_MHCII_HighLow_sig.txt')
