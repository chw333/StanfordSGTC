def annot(inF):
    inFile = open(inF)
    ouFile = open(inF + '.Annot', 'w')
    S = set()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        SL = set()
        for item in fields[7:]:
            feature = item.split('|')[2]
            if feature == 'TF_binding_site':
                gene = item.split('|')[8].split(';')[0].split('Name=')[1]
                SL.add(gene)
                S.add(gene)
        if SL:        
            ouFile.write('\t'.join(fields[0:7]) + '\t' + '\t'.join(SL) + '\n')
    inFile.close()
    ouFile.close()
    print(len(S))

annot('MHCII_low_Tspan8_PositiveNegative_sig.Feature')
annot('Tspan8_negative_MHCII_HighLow_sig.Feature')
