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

def exp(inF):
    V = {}
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[7]
        if gene in G:
            V.setdefault(gene, [])
            V[gene].append([fields[1], fields[2], fields[6]])
    inFile.close()
    return(V)

HCV = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HCV/deHCV1.txt')
WNV = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/WNV/deWNV.txt')
RSV = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/RSV/deHRSV20h.txt')
HSV1 = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HSV/deHSV8h.txt')
KHSV = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/KHSV/deKHSV.txt')
HIV1 = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HIV-1/deHIV1_24h.txt')

print(len(HCV))
print(len(WNV))
print(len(RSV))
print(len(HSV1))
print(len(KHSV))
print(len(HIV1))
