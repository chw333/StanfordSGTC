D = {}
inFile = open('WNV-Stopgain')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[1]
    sample = fields[0]
    D.setdefault(gene, [])
    D[gene].append(sample)
inFile.close()

d = D.items()
d.sort(cmp = lambda x, y:cmp(len(x[1]), len(y[1])), reverse = True)

for item in d:
    print(item[0] + '\t' + str(len(item[1])) + '\t' + '\t'.join(item[1]))
