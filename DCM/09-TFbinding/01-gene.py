#gene = ['RBM20','chr10',112404155,112599227]
#gene = ['EGR1','chr5',137801180,137805004]
gene = ['ZBTB7A','chr19',4045215,4066816]
inFile = open('GRCh37_AnnotatedFeatures.gff')
ouFile = open(gene[0] + '_' + 'GRCh37_AnnotatedFeatures', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[0]
    start = int(fields[3])
    end = int(fields[4])
    if ch == gene[1]:
        if end < gene[2]-2000 or start > gene[3] + 2000:
            pass
        else:
            ouFile.write(line + '\n')
inFile.close()
ouFile.close()
