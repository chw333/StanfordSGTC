def check_head():
    S = set()
    CH = ['chr' + str(x) for x in range(1,23)]
    for ch in CH:
        inFile = open('GEUVADIS.' + ch + '.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Head')
        h = inFile.readline().strip()
        S.add(h)
        inFile.close()
    if len(S) == 1:
        return list(S)[0]
    else:
        print('Error: multiple heads')
        return S
        
SNP = {}
inFile = open('Phase1.Geuvadis_dbSnp137_idconvert.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    SNP[fields[1]] = fields[0]
inFile.close()
def geneName(gene):
    G = {}
    G['FPGT-TNNI3K'] = 'TNNI3K'
    G['TRIM6-TRIM34'] = 'TRIM34'
    if gene in G:
        gene = G[gene]
    return gene
def format(inF):
    inFile = open(inF)
    ouFile = open(inF + '-formated', 'w')
    head = check_head().split('\t')
    ouFile.write('\t'.join(['Gene', 'Mutation', 'dbSNP', 'Type', 'REF', 'ALT', 'Annotation', 'ID', 'Score', 'Filter'] + head[8:]) + '\n')

    for line in inFile:
        line = line.strip()
        fields = line.split('\t')


        mutation_type = fields[1]
        anno = fields[2]
        ref = fields[6]
        alt = fields[7]
        ID = fields[8]
        score = fields[9]
        filt = fields[10]
        mutation = 'chr' + ':'.join(fields[3:6])
        gene = fields[2].split(':')[0]
        genotype = '\t'.join(fields[11:])
        snp = SNP.get(ID, '.')
        if gene.find('-')!=-1: 
            gene = geneName(gene)
        ouFile.write('\t'.join([gene, mutation, snp, mutation_type, ref, alt, anno, ID, score, filt, genotype]) + '\n')
    inFile.close()
    ouFile.close()

#format('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain')
#format('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stoploss')
#format('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-frameshift')
#format('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-StopGainLossFrameshift')
format('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-synonymous')
format('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-nonSynonymous')
