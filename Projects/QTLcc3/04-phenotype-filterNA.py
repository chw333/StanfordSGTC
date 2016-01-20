import numpy as np
MAX = 50
def filter(inF):
    L = []
    inFile = open(inF)
    ouFile = open(inF + '-Formated', 'w')
    ouFile2 = open(inF + '-TooManyNA', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L.append(fields)
    LN = np.array(L) 
    LN = LN.T

    Y = []
    Y.append(LN[0])
    for item in LN[1:]:
        if list(item).count('NA') > len(LN[0]) - MAX:
            ouFile2.write('\t'.join(item) + '\n')
        else:
            Y.append(item)
    YN = np.array(Y)
    YN = YN.T
    for item in YN:
        ouFile.write('\t'.join(item) + '\n')


    inFile.close()
    ouFile.close()
    ouFile2.close()

filter('Yeast-Phenotype')

