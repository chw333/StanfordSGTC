gene = ['RBM20','chr10',112404155,112599227]
inFile = open('GRCh37_AnnotatedFeatures.gff')
ouFile = open(gene[0] + '_' + 'RCh37_AnnotatedFeatures', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[0]
    start = int(fields[3])
    end = int(fields[4])
    if ch == gene[1]:
        if end < gene[2] or start > gene[3]:
            pass
        else:
            ouFile.write(line + '\n')
inFile.close()
ouFile.close()
