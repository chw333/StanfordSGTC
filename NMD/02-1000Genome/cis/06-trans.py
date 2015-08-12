import numpy as np
def transform(inF):
    ouFile = open(inF + '-Trans', 'w')
    ouFile2 = open(inF + '-Pos', 'w')
    data = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        data.append(fields)
    inFile.close()
    data = np.array(data)
    for i in range(data.shape[1]):
        x = data[:,i]
        ouFile.write('\t'.join(x) + '\n')
    for item in data[1:,0]:
        snp = item.split('_')
        ouFile2.write('chr' + snp[1] + '\t' + snp[2] + '\n')
    ouFile.close()
    ouFile2.close()

transform('1000Genome-465LCLs-Genotype-Filt')
