D = {}
inFile = open('5b-Allele-Count')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:4])
    D[k] = '\t'.join(fields[4:])
inFile.close()

inFile = open('5a-Allele-Count')
ouFile = open('5a5b-Allele-Count', 'w')
ouFile.write('Chr\tPos\tREF\tALT\tunMaskREF5a\tunMaskALT5a\tMaskREF5a\tMaskALT5a\tunMaskREF5b\tunMaskALT5b\tMaskREF5b\tMaskALT5b\n')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:4])
    if k in D:
        ouFile.write(line + '\t' + D[k] + '\n')
inFile.close()
ouFile.close()

