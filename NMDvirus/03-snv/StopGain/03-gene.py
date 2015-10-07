def gene(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '-gene', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        sample = fields[0]
        D.setdefault(gene, [])
        D[gene].append(sample)
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])), reverse=True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) +'\t'+ '\t'.join(item[1]) + '\n')
    ouFile.close()

gene('HCV-Stopgain-SNV-het')
gene('HCV-Stopgain-SNV-hom')
gene('HIV-Stopgain-SNV-het')
gene('HIV-Stopgain-SNV-hom')
gene('HSV-Stopgain-SNV-het')
gene('HSV-Stopgain-SNV-hom')
gene('KHSV-Stopgain-SNV-het')
gene('KHSV-Stopgain-SNV-hom')
gene('RSV-Stopgain-SNV-het')
gene('RSV-Stopgain-SNV-hom')
gene('RSV2-Stopgain-SNV-het')
gene('RSV2-Stopgain-SNV-hom')
gene('WNV-Stopgain-SNV-het')
gene('WNV-Stopgain-SNV-hom')
