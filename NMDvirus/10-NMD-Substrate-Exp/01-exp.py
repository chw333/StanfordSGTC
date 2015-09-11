import copy
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
Exp = {}
Exp['HCV'] = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HCV/deHCV1.txt')
Exp['WNV'] = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/WNV/deWNV.txt')
Exp['RSV'] = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/RSV/deHRSV20h.txt')
Exp['HSV1'] = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HSV/deHSV8h.txt')
Exp['KHSV'] = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/KHSV/deKHSV.txt')
Exp['HIV1'] = exp('/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HIV-1/deHIV1_24h.txt')

def sort_gene():
    HCVt = copy.deepcopy(Exp['HCV'])
    Gene = []
    for k in HCVt:
        if len(HCVt[k]) > 1:
            print(HCVt[k])
        if HCVt[k][0][1] == 'NA':
            HCVt[k][0][1] = 0
    print('***')
    HCVs = HCVt.items()
    HCVs.sort(cmp = lambda x,y:cmp(abs(float(x[1][0][1])),abs(float(y[1][0][1]))), reverse=True)
    for item in HCVs:
        Gene.append(item[0])
    return(Gene)
Gs = sort_gene()


ouFile = open('NMD-Substrate-Exp', 'w')
ouFile.write('Virus' + '\t' + '\t'.join(Gs) + '\n')

Virus = ['HCV','WNV','RSV','KHSV','HSV1','HIV1']
for v in Virus:
    L = []
    for gene in Gs:
        L.append(':'.join(Exp[v][gene][0]))
        #L.append(Exp[v][gene][0][1])
    ouFile.write(v + '\t' + '\t'.join(L) + '\n')

ouFile.close()
