def fc2cov(inF, ouF):
    inFile = open(inF)
    ouFile = open(ouF, 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if line[0] == '#':
            pass
        elif line.find('Geneid') == 0:
            ouFile.write('\t'.join(['chr','start','end','gene'] + fields[6:]) + '\n')
        else:
            ouFile.write('\t'.join([fields[1], fields[2], fields[3], fields[0].split('_')[0]] + fields[6:]) + '\n')

    inFile.close()
    ouFile.close()

fc2cov('Mouse_Gene_Promoter_CovFC', 'Mouse_Gene_Promoter_Cov')
