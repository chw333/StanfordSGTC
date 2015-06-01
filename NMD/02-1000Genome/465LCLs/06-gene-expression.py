def ensembl():
    E = {}
    inFile = open('HumanGTF-ids')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        E[fields[0]] = fields[1]
    inFile.close()
    return E
ensembl()
def expression(inF, inF2, ouF):
    E = ensembl()
    ouFile = open(ouF, 'w')
    D = {}
    G = []
    inFile = open(inF)
    heads = inFile.readline().strip().split('\t')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1].split('.')[0]
        G.append(gene)
        D[gene] = {}
        for i in range(4, len(heads)):
            D[gene][heads[i]] = fields[i]
    inFile.close()

    inFile = open(inF2)
    hds = inFile.readline().strip().split('\t')
    sample = hds[10:]

    ouFile.write('GeneSymbol' +'\t' + 'GeneID'+ '\t' + '\t'.join(sample) + '\n')

    for g in G:
        L = []
        for s in sample:
            L.append(D[g].get(s,'-1'))

        ouFile.write(E.get(g,'NA') + '\t' + g + '\t' + '\t'.join(L) + '\n')
            
            
    inFile.close()
    ouFile.close()


expression('GD462.GeneQuantRPKM.50FN.samplename.resk10.txt', 'GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated', 'GD462.GeneQuantRPKM.50FN.samplename.resk10.expression')
