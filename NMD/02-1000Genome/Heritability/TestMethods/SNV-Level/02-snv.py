import numpy as np


def StopGain(L):
    #### median
    S = []
    for item in L:
        if item[0] == -1 or item[1] == -1:
            pass
        elif item[0] < 5 or item[1] < 5:
            pass
        #elif item[0] + item[1] < 20:
        #    pass
        else:
            s = float(item[1]) / float(item[0])
            S.append(s)
    LS = []
    for x in S:
        if x <= 1:
            LS.append(0)
        else:
            LS.append(1)
    if 0 not in LS or 1 not in LS:
        if len(S) > 1:
            return(np.median(S))
        else:
            return(-1)
    else





def snv(inF):
    inFile = open(inF)
    ouFile = open(inF + '-MedianSNV', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        LS = [fields[0]]
        for item in fields[2:]:
            L = []
            esc = item.split('#')[0]
            fds = item.split('+')
            for fd in fds:
                exp = fd.split('#')[-1].split(':')
                L.append([int(exp[0]), int(exp[1])])
            s = StopGain(L)
            if s != -1:
                LS.append(item + '#' + str(s))
        if len(LS) > 1:
            ouFile.write(LS[0] + '\t' + str(len(LS[1:])) + '\t' + '\t'.join(LS[1:]) + '\n')

    inFile.close()
    ouFile.close()


snv('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Gene')
    
