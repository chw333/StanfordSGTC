inFile = open('GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads_heart_exp')
head = inFile.readline().strip()
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene_id = fields[0].split('.')[0]
    D[gene_id] = '\t'.join(fields[1:])
inFile.close()


inFile = open('DCM-GeneCountSymbol')
head2 = inFile.readline().strip().split('\t')
D2 = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene_id = fields[1]
    if gene_id in D:
        D2[gene_id] = D[gene_id] + '\t' + '\t'.join(fields[2:])
inFile.close()

d2 = D2.items()
d2.sort(cmp = lambda x,y:cmp(x[0], y[0]))

ouFile = open('GTEx_Heart_S635A_TwoCtrl_exp', 'w')
ouFile.write(head + '\t' + '\t'.join(head2[2:]) + '\n')
for item in d2:
    ouFile.write(item[0] + '\t' + item[1] + '\n')
ouFile.close()





