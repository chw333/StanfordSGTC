import numpy as np
D = {}
inFile = open('expression_atlas-retinoic_acid_AND_Homo_sapiens.tsv')

for n in range(4):
    head = inFile.readline()

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[0]
    fc = float(fields[5])
    D.setdefault(gene, [])
    D[gene].append(fc)

inFile.close()

d = D.items()
d.sort(cmp = lambda x,y:cmp(np.median(x[1]), np.median(y[1])), reverse=True)
ouFile = open('expression_atlas-retinoic_acid_AND_Homo_sapiens_median_sorted', 'w')
for item in d:
    ouFile.write(item[0] + '\t' + str(np.median(item[1])) + '\n')
ouFile.close()

