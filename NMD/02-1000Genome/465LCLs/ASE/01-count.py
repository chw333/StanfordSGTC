def count(inF):
    ouFile = open('GD462.ASE.COV8.ANNOT_PTV.count', 'w')
    D = {}
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[1]
        sample = ':'.join(fields[0:1] + fields[6:9])
        D.setdefault(snp, set())
        D[snp].add(sample)
    inFile.close()
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])), reverse = True)

    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) +'\t' + '\t'.join(item[1]) + '\n')
    ouFile.close()



count('GD462.ASE.COV8.ANNOT_PTV.txt')
