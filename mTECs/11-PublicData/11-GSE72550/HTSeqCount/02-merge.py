Sample = ['NrlKO_retina_rep1_NF.count','NrlKO_retina_rep2_NF.count','rd7_retina_rep1_NF.count','rd7_retina_rep2_NF.count','WT_retina_rep1_NF.count','WT_retina_rep2_NF.count','WT_cones_rep1_NF.count','WT_cones_rep2_NF.count','WT_rods_rep1_NF.count','WT_rods_rep2_NF.count']
Sample2 = [x.split('_NF.count')[0] for x in Sample]

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



