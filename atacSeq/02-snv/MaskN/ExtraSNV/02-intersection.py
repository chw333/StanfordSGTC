D = {}
inFile = open('5a.flt.vcf.notIn')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:2])
    D[k] = fields
inFile.close()


def intersection(inF):
    ouFile = open(inF + '.both', 'w')
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if line[0] != '#':
            k = '\t'.join(fields[0:2])
            if k in D:
                ouFile.write(line + '\n')
    inFile.close()

intersection('5b.flt.vcf.notIn')
