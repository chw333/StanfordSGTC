def num(inF):
    ouFile = open(inF + '-gene_mt_num', 'w')
    D = {}
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0]
        D.setdefault(gene, 0)
        D[gene] += 1
    inFile.close()
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(x[1],y[1]), reverse=True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(item[1]) + '\n')
    ouFile.close()

num('1000Genome-GEUVADIS465-Stopgain-Genotype')
