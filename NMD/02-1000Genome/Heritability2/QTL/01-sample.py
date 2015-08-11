D = {}
inFile = open('1000Genome-462LCLs-Genotype')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = line
inFile.close()

inFile = open('G462-Sample-Stopgain-ASE-Escape-Filtered2-Median')
ouFile = open('1000Genome-462LCLs-Genotype-Sample2', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    ouFile.write(D[sample] + '\n')
inFile.close()
ouFile.close()

inFile = open('G462-Sample-Stopgain-ASE-Escape-Filtered-Median')
ouFile = open('1000Genome-462LCLs-Genotype-Sample', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    ouFile.write(D[sample] + '\n')
inFile.close()
ouFile.close()
