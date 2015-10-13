import sys

def NMD():
    G = {}
    inFile = open('RSV2-Stopgain-SNV-ReadCount-Filtered')
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
ouFile = open(sys.argv[1].split('.txt')[0] + '.checkGene', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    #baseMean = float(fields[1])
    gene = fields[1]
    #if baseMean > 20:
    if gene in G:
        ouFile.write(line + '\n')
inFile.close()
ouFile.close()
