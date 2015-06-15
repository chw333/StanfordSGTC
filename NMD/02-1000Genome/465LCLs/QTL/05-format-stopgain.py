def format(inF):
    ouFile1 = open('1000Genome-462LCLs-Phenotype', 'w')
    ouFile2 = open('1000Genome-462LCLs-Samples', 'w')
    ouFile3 = open('1000Genome-462LCLs-Stopgains', 'w')
    SNP = []
    Samples = []
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[0]
        count = int(fields[1])
        if count >= 20:
            SNP.append(snp)
        for item in fields[2:]:
            its = item.split(':')
            sample = its[0].split('.')[0]
            ref = float(its[-3])
            alt = float(its[-2])
            val = alt/(ref + 1)
            D.setdefault(sample, {})
            D[sample].setdefault(snp, '')
            #D[sample][snp] = ref + ':' + alt
            D[sample][snp] = '%.2f'%val
    inFile.close()

    for snp in SNP:
        ouFile3.write(snp + '\n')
    for s in D:
        Samples.append(s)
    Samples.sort()
    for s in Samples:
        ouFile2.write(s + '\n')

    ouFile1.write('Sample' + '\t' + '\t'.join(SNP) + '\n')
    for sample in Samples:
        L = []
        for snp in SNP:
            L.append(D[sample].get(snp, 'nan'))
        ouFile1.write(sample + '\t' + '\t'.join(L) + '\n')

    ouFile1.close()
    ouFile2.close()
    ouFile3.close()



format('GD462.ASE.COV8.ANNOT_PTV.count.stopgain.het')

