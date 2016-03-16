import os
D = {}
G = set()
C = set()

Fs = os.listdir('.')
for F in Fs:
    if F.find('_GE.corrs.csv') != -1:
        inFile = open(F)
        head = inFile.readline()
        compound = F.split('_GE.corrs.csv')[0]
        C.add(compound)
        for line in inFile:
            line = line.strip()
            fields = line.split(',')
            val = '\t'.join(fields[1:])
            gene = fields[0].split('"')[1].split('_')[0]
            D.setdefault(gene, {})
            D[gene][compound] =  val
            G.add(gene)
        inFile.close()
G = sorted(G)
C = sorted(C)

ouFile = open('PRISM_GeneExpression_Compound_Matrix', 'w')
H = []
for x in C:
    H.append(x + '_' + 'Corr_coeff')
    H.append(x + '_' + 'Pval_left')
    H.append(x + '_' + 'Qval_left')
    H.append(x + '_' + 'Pval_right')
    H.append(x + '_' + 'Qval_right')
ouFile.write('Gene' + '\t' + '\t'.join(H) + '\n')
for g in G:
    L = []
    for c in C:
        if c in D[g]:
            L.append(D[g][c])
        else:
            L.append('-1\t-1\t-1\t-1\t-1')
    ouFile.write(g + '\t' + '\t'.join(L) + '\n')

ouFile.close()

        

