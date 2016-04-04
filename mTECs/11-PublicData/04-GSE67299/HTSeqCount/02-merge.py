Sample = ['SRR1930167_NF.count', 'SRR1930169_NF.count', 'SRR1930171_NF.count', 'SRR1930173_NF.count']
Sample2 = ['EmbryonicFibroblastst','NeuralStem','InducedPluripotentStem','EmbryonicStem']

D = {}
for sample in Sample:
    G = []
    D.setdefault(sample, {})

    inFile = open(sample)
    for line in inFile:
        line = line.strip()
        if line.find('__') != 0:
            fields = line.split('\t')
            gene = fields[0]
            num = fields[1]
            D[sample][gene] = num
            G.append(gene)
    inFile.close()

ouFile = open('Mouse_Gene_Promoter_Cov', 'w')
ouFile.write('chr\tstart\tend\tgene' + '\t' + '\t'.join(Sample2) + '\n')

for gene in G:
    L = []
    for sample in Sample:
        L.append(D[sample][gene])
    gs = gene.split('_')
    ouFile.write('\t'.join([gs[1],gs[2], gs[3], gs[0]]) + '\t' + '\t'.join(L) + '\n')

ouFile.close()



