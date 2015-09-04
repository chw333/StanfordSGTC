import sys

def NMD():
    G = {}
    DIR = '/mnt/larsix/projects/NMD/hansun/NMDvirus/09-NMD-Substrate'
    inFile = open(DIR + '/' + 'NMD-Substrates-Mocquet.etal')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        G[fields[0]] = 1
    inFile.close()

    inFile = open(DIR + '/' + 'NMD-Substrates-Nakano.etal')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        G[fields[0]] = 1
    inFile.close()

    inFile = open(DIR + '/' + 'NMD-Substrates-Balistreri.etal')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        G[fields[0]] = 1
    inFile.close()
    return G

G = NMD()
inFile = open(sys.argv[1])
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[5]
    if gene in G:
        print(line)
inFile.close()
