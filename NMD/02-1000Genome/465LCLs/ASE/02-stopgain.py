inFile = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain')
D = {}
for line in inFile:
    fields = line.split('\t')
    snp = fields[8]
    D[snp] = 1
inFile.close()

def stopgain(inF):
    inFile = open(inF)
    ouFile = open(inF + '.stopgain', 'w')
    for line in inFile:
        fields = line.split('\t')
        snp = fields[0]
        if snp in D:
            ouFile.write(line)
    inFile.close()
    ouFile.close()

stopgain('GD462.ASE.COV8.ANNOT_PTV.count')

