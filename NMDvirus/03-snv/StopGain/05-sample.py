import numpy as np
Sample = ['HRSV0h-rep1','HRSV0h-rep2','HRSV2h-rep1','HRSV2h-rep2','HRSV4h-rep1','HRSV4h-rep2','HRSV8h-rep1','HRSV8h-rep2','HRSV12h-rep1','HRSV12h-rep2','HRSV16h-rep1','HRSV16h-rep2','HRSV20h-rep1','HRSV20h-rep2','HRSV24h-rep1','HRSV24h-rep2']

def sample(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '-sample', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        ref = int(fields[-2])
        alt = int(fields[-1])
        if ref > 10 and alt >10:
            D.setdefault(sample, [])
        #D[sample].append([int(fields[-2]), int(fields[-1])])
            D[sample].append([float(alt)/float(ref)])
    inFile.close()
    ouFile.close()
    for k in Sample:
        print(k)
        #print(np.median(D[k]))
        print(D[k])

sample('RSV-Stopgain-SNV-het-ase')
