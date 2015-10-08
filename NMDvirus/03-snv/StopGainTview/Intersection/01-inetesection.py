D = {}
inFile = open('RSV-Stopgain-SNV')
for line in inFile:
    line = line.strip()
    fields = line.split()
    gene = fields[1]
    D.setdefault(gene, [])
    D[gene].append(line)
inFile.close()

L = []
ouFile = open('RSV_RSV2-Stopgain-SNV', 'w')
inFile = open('RSV2-Stopgain-SNV')
for line in inFile:
    line = line.strip()
    fields = line.split()
    gene = fields[1]
    if gene in D and gene not in L:
        #ouFile.write(gene + '\t' + D[gene][0] + '\t' + line + '\n')
        ouFile.write(gene + '\n')
        L.append(gene)
inFile.close()
ouFile.close()

