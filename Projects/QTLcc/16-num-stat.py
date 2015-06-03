def num(inF):
    Q = set()
    G = set()
    inFile = open(inF)
    ouFile = open(inF + '-num', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        qtl = fields[0]
        gene = fields[-1].split(':')[0]
        Q.add(qtl)
        G.add(gene)
    inFile.close()
    inFile.close()
    ouFile.write('QTL\t' + str(len(Q)) + '\n')
    ouFile.write('Gene\t' + str(len(G)) + '\n')

#num('Yeast-Single-Trait-Merged-ProteinLightSpecific')
#num('Yeast-Single-Trait-Merged-RNASpecific')
#num('Yeast-RNA-ProteinLight-CommonEffect-Sig-noCov-Merged')


def num2(inF, tp):
    Q = set()
    G = set()
    inFile = open(inF)
    ouFile = open(inF+'-' + tp + '-num', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        qtl = fields[0]
        gene = fields[-1].split(':')[0]
        if fields[-1].find(tp) != -1: 
            Q.add(qtl)
            G.add(gene)
    inFile.close()
    inFile.close()
    ouFile.write('QTL\t' + str(len(Q)) + '\n')
    ouFile.write('Gene\t' + str(len(G)) + '\n')
num2('Yeast-Single-Trait-Merged', 'ProteinLight')
num2('Yeast-Single-Trait-Merged', 'RNA')


