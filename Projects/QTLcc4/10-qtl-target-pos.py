def chrLen():
    D = {}
    inFile = open('S288C_reference_sequence_R64-2-1_20150113.fsa.fa')
    C = ['chr' + str(x) for x in range(1, 10)]
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            c = line1[1:] 
            if c in C:
                D['chr0'+line1[4:]] = len(line2)
            else:
                D[line1[1:]] = len(line2)
        else:
            break
    inFile.close()
    print(D)
    return D


def cummulativeLen():
    CL = {}
    D = chrLen()
    CH = ['chr0' + str(x) for x in range(1, 10)] + ['chr' + str(x) for x in range(10, 17)] + ['chrM']
    for ch in CH:
        ith = CH.index(ch)
        n = 0
        for i in range(ith):
            n += D[CH[i]]
        CL[ch] = n
    return CL  

def geneAnnot():
    CH = {}
    CH['chrI'] = 'chr01'
    CH['chrII'] = 'chr02'
    CH['chrIII'] = 'chr03'
    CH['chrIV'] = 'chr04'
    CH['chrV'] = 'chr05'
    CH['chrVI'] = 'chr06'
    CH['chrVII'] = 'chr07'
    CH['chrVIII'] = 'chr08'
    CH['chrIX'] = 'chr09'
    CH['chrX'] = 'chr10'
    CH['chrXI'] = 'chr11'
    CH['chrXII'] = 'chr12'
    CH['chrXIII'] = 'chr13'
    CH['chrXIV'] = 'chr14'
    CH['chrXV'] = 'chr15'
    CH['chrXVI'] = 'chr16'
    CH['chrM'] = 'chrM'
    G = {}
    inFile = open('saccharomyces_cerevisiae_R64-2-1_20150113.gff')
    for line in inFile:
        line = line.strip()
        if line[0] != '#':
            fields = line.split('\t')
            try:
                typ = fields[2]
                ch = fields[0]
                start = int(fields[3])
                end = int(fields[4])
                gene = fields[8].split(';')[0].split('ID=')[1]
                if typ == 'gene':
                    if gene not in G:
                        G[gene] = [CH[ch], (start + end)/2]
            except:
                pass
    inFile.close()
    return G

CL = cummulativeLen()
for k in CL:
    print(k + '\t' + str(CL[k]))
G = geneAnnot()


def qtl_gene_pos(inF):
    inFile = open(inF)
    ouFile = open(inF + '.pos', 'w')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[1]
        pos = int(fields[2])
        gene = fields[-1]
        x = CL[ch] + pos 
        y =  CL[G[gene][0]] + G[gene][1]
        ouFile.write(str(x) + '\t' + str(y) + '\n')
    inFile.close()
    ouFile.close()

qtl_gene_pos('Yeast-RNA-ProteinLight-AnyEffect-Sig-Cov')
qtl_gene_pos('Yeast-RNA-ProteinLight-CommonEffect-Sig-Cov')
qtl_gene_pos('Yeast-RNA-ProteinLight-SpecificEffect-Sig-Cov')
