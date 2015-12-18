def gene(inF, inF2, ouF):
    G = []
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0]
        G.append(gene)
    inFile.close()

    inFile = open(inF2)
    ouFile = open(ouF, 'w')
    head = inFile.readline()
    ouFile.write(head)
    for line in inFile:
        fields = line.split('\t')
        gene = fields[6]
        if gene in G:
            ouFile.write(line)
    inFile.close()
    ouFile.close()

#gene('geneTable_GeneNameUpdated.txt','AnnotSNP.hg19_multianno.txt','AnnotSNP.hg19_multianno_gene.txt')
gene('geneTable_GeneNameUpdated.txt','AnnotINDEL.hg19_multianno.txt','AnnotINDEL.hg19_multianno_gene.txt')
