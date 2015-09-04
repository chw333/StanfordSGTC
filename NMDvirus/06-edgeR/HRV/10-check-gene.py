import sys

def NMD():
    G = {}
    DIR = '/mnt/larsix/projects/NMD/hansun/NMDvirus/09-NMD-Substrate'
    inFile = open(DIR + '/' + 'NMD-Substrates-Mocquet.etal')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        gene = fields[0]
        if gene[0] != '#':
            G[gene] = 1
    inFile.close()

    inFile = open(DIR + '/' + 'NMD-Substrates-Nakano.etal')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        gene = fields[0]
        if gene[0] != '#':
            G[gene] = 1
    inFile.close()

    inFile = open(DIR + '/' + 'NMD-Substrates-Ramage.etal')
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
    baseMean = float(fields[2])
    gene = fields[6]
    if baseMean > 4.3:
        if gene in G:
            ouFile.write(line + '\n')
inFile.close()
ouFile.close()
