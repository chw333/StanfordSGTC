D = {}
inFile = open('hg19_refGene.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[12]
    start = fields[4]
    end = fields[5]
    ch = fields[2]
    D.setdefault(gene, [])
    D[gene].append([ch, start, end])
inFile.close()


inFile = open('NMD-Genes')
ouFile = open('NMD-Genes-Pos', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    if line in D:
        ouFile.write(line + '\t' + '\t'.join(D[line][0]) + '\n')
inFile.close()
ouFile.close()
