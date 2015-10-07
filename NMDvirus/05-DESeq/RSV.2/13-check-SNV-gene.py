import sys

def NMD():
    G = {}
    inFile = open('SNV-Genes')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        gene = fields[0]
        if gene[0] != '#':
            G[gene] = 1
    inFile.close()
    return G

G = NMD()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1].split('.txt')[0] + '.checkGene2', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    baseMean = float(fields[1])
    gene = fields[7]
    if baseMean > 20:
        #if float(fields[5]) < 0.05:
        if gene in G:
            ouFile.write(line + '\n')
inFile.close()
ouFile.close()
