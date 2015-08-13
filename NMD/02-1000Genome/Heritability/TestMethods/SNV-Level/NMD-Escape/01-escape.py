import numpy as np
def escape(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '-Escape', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields[2:]:
            esc = item.split('#')[0]
            snp = item.split('#')[1].split(':')[0]
            val = item.split('#')[-1]
            #ouFile.write('\t'.join([snp, val, esc]) + '\n')
            k = snp + '\t' + esc
            D.setdefault(k, [])
            D[k].append(float(val))
    for k in D:
        ouFile.write(k + '\t' + str(np.median(D[k])) + '\n')

    inFile.close()
    ouFile.close()

escape('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Gene-SumSNV')
