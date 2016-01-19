L = []
inFile = open('Motifmap-RBM20')
head = inFile.readline()
for line in inFile:
    fields = line.split('\t')
    tf = fields[14]
    L.append(tf)
inFile.close()


L2 = []
inFile = open('expression_atlas-retinoic_acid_AND_Homo_sapiens_median_sorted')
for line in inFile:
    fields = line.split('\t')
    gene = fields[0]
    L2.append(gene)
inFile.close()
print('\n'.join(L))

for x in L:
    if x in L2:
        print(x)
