from scipy import stats
import numpy as np

def get_library_size():
    L = [-1, -1 , -1]
    inFile = open('mTECs-Sample-LibrarySize')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L.append(float(fields[2]))
    inFile.close()
    return(L)

LS = get_library_size()

CH = [str(x) for x in range(1, 20)] + ['X','Y','MT']
ouFile = open('Tspan8_positive_MHCII_HighLow', 'w')
sI = [3, 4, 7, 8]
n = 0
for ch in CH:
    n += 1
    F = 'mTECs-Cov-chr' + ch
    inFile = open(F)
    head = inFile.readline().strip().split('\t')
    if n == 1:
        ouFile.write('\t'.join([head[0], head[1], head[2], head[sI[0]], head[sI[1]], head[sI[2]], head[sI[3]], 'fold_change']) + '\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        v1 = int(fields[sI[0]])/LS[sI[0]]
        v2 = int(fields[sI[1]])/LS[sI[1]]
        v3 = int(fields[sI[2]])/LS[sI[2]]
        v4 = int(fields[sI[3]])/LS[sI[3]]
        X = np.mean([v1, v2])
        Y = np.mean([v3, v4])
        fc = X/(Y+1)
        #pv = stats.fisher_exact([[int(v1), int(v2)], [int(v3), int(v4)]])[1]
        #pv = stats.ranksums([np.log2(v1), np.log2(v2)], [np.log2(v3), np.log2(v4)])[1]
        if fc < 0.5 or fc > 2:
            if (v1 >20 and v2 > 20) or (v3>20 and v4>20):
            ###ouFile.write('\t'.join([fields[0], fields[1], fields[2], fields[sI[0]], fields[sI[1]] , fields[sI[2]], fields[sI[3]], str(pv)]) + '\n')
                ouFile.write('\t'.join([fields[0], fields[1], fields[2], '%.2f'%v1, '%.2f'%v2, '%.2f'%v3, '%.2f'%v4, '%.2f'%fc]) + '\n')
    inFile.close()

ouFile.close()
