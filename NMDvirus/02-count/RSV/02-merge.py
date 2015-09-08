Sample = ['HRSV0h-rep1.count','HRSV0h-rep2.count','HRSV2h-rep1.count','HRSV2h-rep2.count','HRSV4h-rep1.count','HRSV4h-rep2.count','HRSV8h-rep1.count','HRSV8h-rep2.count','HRSV12h-rep1.count','HRSV12h-rep2.count','HRSV16h-rep1.count','HRSV16h-rep2.count','HRSV20h-rep1.count','HRSV20h-rep2.count','HRSV24h-rep1.count','HRSV24h-rep2.count']
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

ouFile = open('HRSV-GeneCount', 'w')
ouFile.write('' + '\t' + '\t'.join([x.split('.count')[0] for x in Sample]) + '\n')

for gene in G:
    L = []
    for sample in Sample:
        L.append(D[sample][gene])
    ouFile.write(gene + '\t' + '\t'.join(L) + '\n')

ouFile.close()



