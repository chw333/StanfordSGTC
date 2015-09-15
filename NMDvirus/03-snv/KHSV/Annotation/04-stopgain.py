Sample = ['Mock-rep1.flt.anno.exonic_variant_function','Mock-rep2.flt.anno.exonic_variant_function','Mock-rep3.flt.anno.exonic_variant_function','KHSV-rep1.flt.anno.exonic_variant_function','KHSV-rep2.flt.anno.exonic_variant_function','KHSV-rep3.flt.anno.exonic_variant_function']
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

ouFile = open('KHSV-Stopgain', 'w')
for item in L:
    ouFile.write('\t'.join(item) + '\n')
ouFile.close()

