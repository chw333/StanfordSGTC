D = {}
inFile = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated-sorted-SampleNumberHetSNV')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    for snp in fields[2:]:
        D.setdefault(snp, [])
        D[snp].append(sample)
inFile.close()

def het(inF):
    HET = {}
    
    inFile = open(inF)
    ouFile = open(inF + '.het', 'w')

    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        snp = fields[0]
        HET.setdefault(snp, [])
        for item in fields[2:]:
            sample = item.split('.')[0]
            if sample in D[snp]:
                HET[snp].append(item)

    inFile.close()


    d = HET.items()
    d.sort(cmp = lambda x,y: cmp(len(x[1]), len(y[1])), reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t' + str(len(item[1])) + '\t' + '\t'.join(item[1]) + '\n')

    ouFile.close()
het('GD462.ASE.COV8.ANNOT_PTV.count.stopgain')
