def region(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.')[0] + '-region.bed', 'w')
    for line in inFile:
        line = line.strip()
        if line[0] != '#':
            fields = line.split('\t')
            ouFile.write(fields[0] + '\t' + fields[1] + '\t' + fields[1] + '\n')

    inFile.close()
    ouFile.close()


region('5a.flt.vcf')
region('5b.flt.vcf')

