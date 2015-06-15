def number(inF):
    ouFile = open(inF + '-SampleNumber', 'w')
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[0]
        for item in fields[2:]:
            s = item.split('.')[0]
            D.setdefault(s, [])
            D[s].append(snp)
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y : cmp(len(x[1]), len(y[1])), reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) + '\t' + '\t'.join(item[1]) + '\n')
    ouFile.close()

number('GD462.ASE.COV8.ANNOT_PTV.count.stopgain')
