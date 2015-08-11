def filter(inF):
    X = []
    inFile = open(inF)
    ouFile = open(inF + '-Filtered', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L = [fields[0]]
        for item in fields[2:]:
            fds = item.split(':')
            v1 = int(fds[-2])
            v2 = int(fds[-1])
            if v1 == -1 or v2 == -1:
                pass
            elif v1 == 0 or v2 == 0:
                pass
            elif v1 + v2 < 30:
                pass
            else:
                L.append(item)
        X.append(L)
    X.sort(cmp = lambda x,y:cmp(len(x), len(y)), reverse=True)
    for item in X:
        ouFile.write(item[0] + '\t' + str(len(item[1:])) + '\t' + '\t'.join(item[1:]) + '\n')

    inFile.close()
    ouFile.close()

filter('G462-Sample-Stopgain-ASE')
