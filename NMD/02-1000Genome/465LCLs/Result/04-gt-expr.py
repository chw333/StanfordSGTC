def expr(inF):
    D = {}

    inFile = open(inF)
    head = inFile.readline().strip().split('\t')
    sample = head[2:]
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0]
        D[gene] = fields[2:]
    inFile.close()
    return [D,sample]

def geno(inF):
    E,S = expr('1000Genome-GEUVADIS465-Stopgain-Expression')

    inFile = open(inF)
    ouFile = open(inF + '-Expression', 'w')
    ouFile2 = open(inF + '-ExpressionAL50', 'w')
    head = inFile.readline().strip().split('\t')
    sample = head[13:]
    for line in inFile:
        L0 = []
        L1 = []
        L2 = []
        line = line.strip()
        fields = line.split('\t')
        gene = fields[3]
        G = fields[13:]
        EX = E[gene]

        for i in range(len(G)):
            if G[i] == '0':
                L0.append(EX[i])
            elif G[i] == '1':
                L1.append(EX[i])
            elif G[i] == '2':
                L2.append(EX[i])
            elif G[i] == '-1':
                pass
            else:
                print('Warning')
        ouFile.write('>' + line + '\n')
        ouFile.write('\t'.join(L0) + '\n')
        ouFile.write('\t'.join(L1) + '\n')
        ouFile.write('\t'.join(L2) + '\n')
        if int(fields[0]) >= 50 and int(fields[1]) >= 50:
            ouFile2.write('>' + line + '\n')
            ouFile2.write('\t'.join(L0) + '\n')
            ouFile2.write('\t'.join(L1) + '\n')
            ouFile2.write('\t'.join(L2) + '\n')

    inFile.close()
    ouFile.close()
    ouFile2.close()


geno('1000Genome-GEUVADIS465-Stopgain-Genotype-mutationFreq')




