import numpy as np
def gene(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.txt')[0] + '.gene', 'w')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0].split('_')[0]
        ouFile.write(gene + '\n')
    inFile.close()
    ouFile.close()


def gene2(inF):
    inFile = open(inF)
    head = inFile.readline()
    ouFile = open(inF.split('.txt')[0] + '.Exp', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[3]
        L = [int(x) for x in fields[4:]]
        if np.sum(L) > 20:
            ouFile.write(gene + '\n')
    inFile.close()
    ouFile.close()

gene('MHCII_low_Tspan8_PositiveNegative_sig.txt')
gene('Tspan8_negative_MHCII_HighLow_sig.txt')
gene2('Mouse_Gene_Promoter_Cov')
