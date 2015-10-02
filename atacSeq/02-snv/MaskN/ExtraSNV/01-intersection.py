D = {}
inFile = open('5a5b-Allele-Count')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:2])
    D[k] = fields
inFile.close()


def intersection(inF):
    ouFile = open(inF + '.notIn', 'w')
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if line[0] != '#':
            k = '\t'.join(fields[0:2])
            if k not in D:
                ouFile.write(line + '\n')
    inFile.close()

def intersection2(inF):
    ouFile = open(inF + '.In', 'w')
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if line[0] != '#':
            k = '\t'.join(fields[0:2])
            if k in D:
                ouFile.write(line + '\n')
    inFile.close()


intersection('5a.flt.vcf')
intersection('5b.flt.vcf')
intersection2('S96a.raw.vcf')
intersection2('S96b.raw.vcf')
intersection('YJM789a.flt.vcf')
intersection('YJM789b.flt.vcf')
