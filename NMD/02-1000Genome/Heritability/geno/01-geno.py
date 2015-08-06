D = {}
inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample')
ouFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Geno', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    for item in fields[2:]:
        ims = item.split('|')
        for im in ims:
            snp = im.split(':')[0]
            k = sample + '\t' + snp
            D[k] = ''
inFile.close()


CH = ['chr'+str(x) for x in range(1,23)]

for ch in CH:
    inFile = open('GEUVADIS.' + ch + '.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
    for line in inFile:
        line = line.strip()
        if line.find('##') == 0:
            pass
        elif line.find('#CHROM') == 0:
            head = line.split('\t')
        else:
            fields = line.split('\t')
            snp = fields[2]
            for i in range(9, len(fields)):
                genotype = fields[i].split(':')[0]
                k = head[i] + '\t' + snp
                if k in D:
                    D[k] = genotype
    inFile.close()

for k in D:
    ouFile.write(k + '\t' + D[k] + '\n')
ouFile.close()

