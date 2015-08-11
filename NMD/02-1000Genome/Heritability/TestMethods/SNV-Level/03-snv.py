import numpy as np

'''
def StopGain(L):
    #### sum
    s0 = 0
    s1 = 0
    X = []
    for item in L:
        if item[0] == -1 or item[1] == -1:
            pass
        elif item[0] == 0 or item[1] == 0:
            pass
        elif item[0] + item[1] < 20:
            pass
        else:
            s0 += item[0]
            s1 += item[1]
            if item[0] <= item[1]:
                X.append(0)
            else:
                X.append(1)
    #if 1 not in X or 0 not in X:
    if X.count(0) <= 2 or X.count(1) <= 2:
        if s0 >0 and s1 > 0:
            return((s1 + 1.0) / ( s0 + 1.0))
        else:
            return(-1)
    else:
        return(-1)
        

def StopGain2(L):
    #### median
    #### neigther == 0
    #### consistent direction
    S = []
    X = []
    for item in L:
        if item[0] == -1 or item[1] == -1:
            pass
        elif item[0] == 0 or item[1] == 0:
            pass
        elif item[0] + item[1] < 20:
            pass
        else:
            S.append((item[1] + 1.0)/(item[0] + 1.0))
            #if (item[1] + 1.0)/(item[0] + 1.0) <= 1:
            if X.count(0) <= 2 or X.count(1) <= 2:
                X.append(0)
            else:
                X.append(1)

    if S:
        if 0 not in X or 1 not in X:
            return(np.median(S))
        else:
            return(-1)
    else:
        return(-1)
'''

def StopGain(L, met):
    if met == 'Point':
        v = -1

        if L[0][0] == -1 and  L[0][1] == -1:
            pass
        elif L[0][0] == 0 or  L[0][1] == 0:
            pass
        elif L[0][0] + L[0][1] < 30:
            pass
        else:
            v = (L[0][1] + 1.0)/(L[0][0] + 1.0)
        return v




def snv(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Escape', 'w')
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
            s = StopGain(L, 'Point')
            print(L)
            if s != -1:
                LS.append(item + '#' + str(s))
        if len(LS) > 1:
            ouFile.write('\t'.join(LS) + '\n')

    inFile.close()
    ouFile.close()


snv('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
    
