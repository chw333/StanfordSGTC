D = {}
inFile = open('G462-Sample-Stopgain-Exon-Escape')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields[4]
inFile.close()
print(len(D))

inFile = open('G462-Sample-Stopgain-ASE')
ouFile = open('G462-Sample-Stopgain-ASE-Escape', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L = fields[0:2]
    for item in fields[2:]:
        snp = item.split(':')[0]
        L.append(D[snp] + ':' + item)
    ouFile.write('\t'.join(L) + '\n')

inFile.close()
ouFile.close()
