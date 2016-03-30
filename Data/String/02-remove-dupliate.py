def dup(inF):
    ouFile = open(inF + '-unique', 'w')
    D = {}
    D2 = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k1 = fields[0] + '\t' + fields[1]
        k2 = fields[1] + '\t' + fields[0]
        score = int(fields[2])
        if k1 not in D and k2 not in D:
            D.setdefault(k1, [])
            D[k1].append(score)
        elif k1 in D:
            D[k1].append(score)
        elif k2 in D:
            D[k2].append(score)
    for k in D:
        D2[k] = max(D[k])
    d = D2.items()
    d.sort(cmp = lambda x,y:cmp(x[1], y[1]), reverse=True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(item[1]) + '\n')
    inFile.close()
    ouFile.close()

dup('String-human-protein-links')
dup('String-human-protein-links-Score400')
