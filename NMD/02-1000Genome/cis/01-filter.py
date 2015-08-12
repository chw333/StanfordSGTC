D = {}
inFile = open('1000Genome-462LCLs-Position-cis')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = 'snp_' + fields[0].strip('chr') + '_' + fields[1]
    D[k] = 1
inFile.close()

inFile = open('1000Genome-465LCLs-Genotype-FiltTrans-Ref')
ouFile = open('1000Genome-465LCLs-Genotype-Filt','w')
head = inFile.readline().strip()
ouFile.write(head + '\n')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] in D:
        ouFile.write(line + '\n')

inFile.close()
ouFile.close()
