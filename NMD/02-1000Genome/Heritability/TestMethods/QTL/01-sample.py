D = {}
inFile = open('1000Genome-465LCLs-Genotype-Filt-Trans')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = line
inFile.close()


inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Gene-SumSNV-Median')
ouFile = open('1000Genome-462LCLs-Genotype-Sample', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    ouFile.write(D[sample] + '\n')
inFile.close()
ouFile.close()
