D = {}
inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[2:]:
        snp = item.split('|')[0]
        D[snp] = 1
inFile.close()


ouFile = open('G462-Sample-Stopgain-Exon', 'w')
for k in D:
    ouFile.write(k + '\n')
ouFile.close()


