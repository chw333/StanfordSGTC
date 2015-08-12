import numpy as np


def StopGain(L):
    #### sum
    s0 = 0
    s1 = 0
    for item in L:
        if item[0] == -1 or item[1] == -1:
            pass
        elif item[0] == 0 or item[1] == 0:
            pass
        #elif item[0] + item[1] < 20:
        #    pass
        else:
            s0 += item[0]
            s1 += item[1]
    if s0 >0 and s1 > 0:
        return(float(s1) / float(s0))
    else:
        return(-1)





def snv(inF):
    inFile = open(inF)
    ouFile = open(inF + '-SumSNV', 'w')
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


snv('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
    
