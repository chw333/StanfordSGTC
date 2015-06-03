inFile = open('HG-U133A_2.na34.annot.txt')
ouFile = open('ProbSetID-Ensembl-GeneSymbol-HG-U133A_2.na34.annot.txt', 'w')

for i in range(26):
    line = inFile.readline()

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ouFile.write(fields[0] + '\t' + fields[14] + '\t' + fields[17] + '\n')
inFile.close()
ouFile.close()
