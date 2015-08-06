def ase(inF, inF2):
    D = {}
    inFile = open(inF2)
    head = inFile.readline().strip()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0].split('.')[0]
        snv = fields[1]
        k = sample + '\t' + snv
        D[k] = fields[6:8]
    inFile.close()


    D2 = {}
    inFile = open(inF)
    ouFile = open(inF + '-ASE', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        L = [fields[0]]
        for snv in fields[2:]:
            k = sample + '\t' + snv
            if k in D:
                D2.setdefault(sample, [])
                D2[sample].append(snv + ':' + ':'.join(D[k]))

    d = D2.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])), reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) + '\t' + '\t'.join(item[1]) + '\n')

    inFile.close()
    ouFile.close()

ase('G462-Sample-Stopgain', 'GD462.ASE.COV8.ANNOT_PTV.txt')
