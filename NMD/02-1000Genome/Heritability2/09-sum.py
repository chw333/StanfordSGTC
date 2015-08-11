import numpy as np
def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Sum', 'w')
    ouFile.write('Sample\tNMD\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = []
        s1 = 0
        s2 = 0
        for item in fields[2:]:
            if item[0] == 'F':
                v1 = float(item.split(':')[-2])
                v2 = float(item.split(':')[-1])
                #L.append((v2 + 1)/(v1 + 1))
                s1 += v1
                s2 += v2
        ouFile.write(sample + '\t' + str((s2 + 1)/(s1 + 1)) + '\n')

    inFile.close()
    ouFile.close()

median('G462-Sample-Stopgain-ASE-Escape-Filtered')
median('G462-Sample-Stopgain-ASE-Escape-Filtered2')
