Sample = ['HIV_12-rep1.count','HIV_12-rep2.count','HIV_12-rep3.count','HIV_24-rep1.count','HIV_24-rep2.count','HIV_24-rep3.count','Mock_12-rep1.count','Mock_12-rep2.count','Mock_12-rep3.count','Mock_24-rep1.count','Mock_24-rep2.count']

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

ouFile = open('HIV1-GeneCount', 'w')
ouFile.write('' + '\t' + '\t'.join([x.split('.count')[0] for x in Sample]) + '\n')

for gene in G:
    L = []
    for sample in Sample:
        L.append(D[sample][gene])
    ouFile.write(gene + '\t' + '\t'.join(L) + '\n')

ouFile.close()



