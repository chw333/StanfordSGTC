CH = ['chr' + str(i) for i in range(1,23)]

def sample():
    L = []
    inFile = open('../../GEUVADIS.chr1.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Head')
    head = inFile.readline().strip().split('\t')
    for x in head[8:]:
        L.append(x)
    inFile.close()
    ouFile = open('1000Genome-465LCLs-Samples', 'w')
    for x in L:
        ouFile.write(x + '\n')
    ouFile.close()
    return L
S = sample()


def sampleGenotype():
    D = {}
    G = []
    for ch in CH:
        inFile = open('../../GEUVADIS.%s.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype'%ch)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            geno = fields[8:]
            if len(geno) == len(S):
                G.append(fields[5])
                for i in range(len(geno)):
                    D.setdefault(S[i], [])
                    D[S[i]].append(geno[i])
        inFile.close()
        ouFile = open('1000Genome-465LCLs-Genotype', 'w')
        ouFile.write('\t'.join(['Sample'] + G) + '\n')
        for s in S:
            ouFile.write(s + '\t' + '\t'.join(D[s]) + '\n')
        ouFile.close()
        print(len(S))
        print(len(G))
        

sampleGenotype()
