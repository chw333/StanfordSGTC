Sample = ['Mock-rep1.count','Mock-rep2.count','delNS1_M0.1-rep1.count','delNS1_M0.1-rep2.count','delNS1_M3-rep1.count','delNS1_M3-rep2.count']
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

ouFile = open('RSVdelNS-GeneCount2', 'w')
ouFile.write('' + '\t' + '\t'.join([x.split('.count')[0] for x in Sample]) + '\n')

for gene in G:
    L = []
    for sample in Sample:
        L.append(D[sample][gene])
    ouFile.write(gene + '\t' + '\t'.join(L) + '\n')

ouFile.close()



