def sort(inF):
    L = []
    inFile = open(inF)
    ouFile = open(inF + '-sorted', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L.append(fields)
    inFile.close()
    L.sort(cmp = lambda x,y:cmp(float(x[2]), float(y[2])))
    for item in L:
        ouFile.write('\t'.join(item) + '\n')
    ouFile.close()

sort('Single-Trait-lm-Sig')
