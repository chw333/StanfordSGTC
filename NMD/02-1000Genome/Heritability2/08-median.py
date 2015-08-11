import numpy as np
def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Median', 'w')
    ouFile.write('Sample\tNMD\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        for item in fields[2:]:
            if item[0] == 'F':
                v1 = float(item.split(':')[-2])
                v2 = float(item.split(':')[-1])
                L.append((v2 + 1)/(v1 + 1))
        ouFile.write(sample + '\t' + str(np.median(L)) + '\n')

    inFile.close()
    ouFile.close()

median('G462-Sample-Stopgain-ASE-Escape-Filtered')
median('G462-Sample-Stopgain-ASE-Escape-Filtered2')
