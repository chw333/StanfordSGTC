inFile = open('../../GEUVADIS.chr9.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Head')
ouFile = open('1000Genome-462LCLs-Samples', 'w')
head = inFile.readline().strip().split('\t')
for x in head[8:]:
    ouFile.write(x + '\n')
inFile.close()
ouFile.close()
