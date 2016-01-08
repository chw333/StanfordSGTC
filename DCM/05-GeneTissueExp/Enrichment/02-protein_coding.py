D = {}
inFile = open('hg19_refGene.txt')
for line in inFile:
    fields = line.split('\t')
    if fields[1][0:3] == 'NM_':
        D[fields[12]] = 1
inFile.close()

inFile = open('GTEx_Genes')
ouFile = open('GTEx_Genes_ProteinCoding', 'w')
L = []
for line in inFile:
    line = line.strip()
    if line in D:
        L.append(line)
inFile.close()

for item in set(L):
    ouFile.write(item + '\n')
ouFile.close()
