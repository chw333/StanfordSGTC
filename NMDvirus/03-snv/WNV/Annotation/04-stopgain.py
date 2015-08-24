Sample = []
for x in range(1, 11):
    Sample.append('S' + str(x) + '-WNV.flt.anno.exonic_variant_function')
    Sample.append('S' + str(x) + '-Mock.flt.anno.exonic_variant_function')

L = []
for s in Sample:
    sa = s.split('.')[0]
    inFile = open(s)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[2].split(':')[0]
        if fields[1] == 'stopgain':
            L.append([sa, gene] + fields[1:])
    inFile.close()

ouFile = open('WNV-Stopgain', 'w')
for item in L:
    ouFile.write('\t'.join(item) + '\n')
ouFile.close()

