def sample(inF):
    D = {}
    inFile = open(inF)
    ouFile = open('G462-Sample-Stopgain', 'w')
    head = inFile.readline().strip().split('\t')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i in range(10, len(fields)):
            if fields[i] == '1':
                D.setdefault(head[i], [])
                D[head[i]].append(fields[7])
    inFile.close()
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])), reverse=True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) +  '\t' + '\t'.join(item[1]) + '\n')
    ouFile.close()

sample('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated-sorted')
