D = {}
inFile = open('../5a.raw.vcf')
for line in inFile:
    line = line.strip()
    if line[0] != '#':
        fields = line.split('\t')
        k = fields[0] + '\t' + fields[1]
        D[k] = 1
inFile.close()

inFile = open('../5b.raw.vcf')
for line in inFile:
    line = line.strip()
    if line[0] != '#':
        fields = line.split('\t')
        k = fields[0] + '\t' + fields[1]
        D[k] = 1
inFile.close()

inFile = open('../S96a.raw.vcf')
for line in inFile:
    line = line.strip()
    if line[0] != '#':
        fields = line.split('\t')
        k = fields[0] + '\t' + fields[1]
        D[k] = 1
inFile.close()

inFile = open('../S96b.raw.vcf')
for line in inFile:
    line = line.strip()
    if line[0] != '#':
        fields = line.split('\t')
        k = fields[0] + '\t' + fields[1]
        D[k] = 1
inFile.close()



inFile = open('YJM789ab.flted')
ouFile = open('YJM789ab.flted.onlyYJM', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[0] + '\t' + fields[1]
    if k not in D:
        ouFile.write(line + '\n')
inFile.close()
ouFile.close()




