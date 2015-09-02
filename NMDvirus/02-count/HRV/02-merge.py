Sample = []
SP = {}
inFile = open('SampleInfo')
for line in inFile:
    line = line.strip()
    fields = line.split()
    s = fields[2] + '.count'
    SP[s] = fields[1]
    Sample.append(s)
inFile.close()

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

ouFile = open('HRV-GeneCount', 'w')
ouFile.write('' + '\t' + '\t'.join([SP[x] for x in Sample]) + '\n')

for gene in G:
    L = []
    for sample in Sample:
        L.append(D[sample][gene])
    ouFile.write(gene + '\t' + '\t'.join(L) + '\n')

ouFile.close()



