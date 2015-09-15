Sample = ['Mock-Rep1.flt.anno.exonic_variant_function','Mock-Rep2.flt.anno.exonic_variant_function','HSV2h-Rep1.flt.anno.exonic_variant_function','HSV2h-Rep2.flt.anno.exonic_variant_function','HSV4h-Rep1.flt.anno.exonic_variant_function','HSV4h-Rep2.flt.anno.exonic_variant_function','HSV6h-Rep1.flt.anno.exonic_variant_function','HSV6h-Rep2.flt.anno.exonic_variant_function','HSV8h-Rep1.flt.anno.exonic_variant_function','HSV8h-Rep2.flt.anno.exonic_variant_function']
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

ouFile = open('HSV-Stopgain', 'w')
for item in L:
    ouFile.write('\t'.join(item) + '\n')
ouFile.close()

